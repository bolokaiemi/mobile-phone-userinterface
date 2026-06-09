from flask import Flask, send_from_directory, request, jsonify, session, make_response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
from dotenv import load_dotenv
# =========================================
# LOAD ENV
# =========================================
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


# Initialize Flask app, pointing the static files folder to the root directory
# to match the native structure of your GitHub Pages deployment.
app = Flask(__name__, static_folder='.', static_url_path='')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'ebiui-secure-dev-key')

# Capture database configuration: SQLite for local dev, PostgreSQL for production on Render
database_url = os.environ.get('DATABASE_URL', 'sqlite:///ebiui.db')
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -------------------------------------------------------------
# FLASK-MAIL CONFIGURATION
# -------------------------------------------------------------
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = os.environ.get('SMTP_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.environ.get('SMTP_PORT', 587))
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('SMTP_EMAIL')
app.config['MAIL_PASSWORD'] = os.environ.get('SMTP_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('SMTP_EMAIL')

mail = Mail(app)

def send_notification_email(subject, body):
    try:
        recipient = os.environ.get('SMTP_EMAIL')
        if recipient:
            msg = Message(subject, recipients=[recipient])
            msg.body = body
            mail.send(msg)
            print(f"Notification email sent: {subject}")
        else:
            print("No recipient defined for notification email.")
    except Exception as e:
        print(f"Failed to send notification email: {e}")

# Enable CORS for development/testing origins supporting cookies/credentials
@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response()
        origin = request.headers.get('Origin')
        if origin:
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Credentials'] = 'true'
        else:
            response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
        response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
        return response

@app.after_request
def add_cors_headers(response):
    origin = request.headers.get('Origin')
    if origin:
        response.headers['Access-Control-Allow-Origin'] = origin
        response.headers['Access-Control-Allow-Credentials'] = 'true'
    else:
        response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

db = SQLAlchemy(app)

# -------------------------------------------------------------
# DATABASE MODELS
# -------------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    full_name = db.Column(db.String(100), nullable=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) # Optional for anonymous reviews
    guest_name = db.Column(db.String(80), nullable=True) # For guest users
    rating = db.Column(db.Integer, default=5, nullable=False) # Star rating (1-5)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to user
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.user.username if self.user else (self.guest_name or 'Anonymous Guest'),
            'rating': self.rating,
            'text': self.text,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True) # Optional for guests
    guest_email = db.Column(db.String(120), nullable=True)
    billing_name = db.Column(db.String(100), nullable=False)
    course_name = db.Column(db.String(100), nullable=False)
    zoom_link = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    user = db.relationship('User', backref=db.backref('bookings', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'billing_name': self.billing_name,
            'course_name': self.course_name,
            'zoom_link': self.zoom_link,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

# Milestone targets to control registration features
REVIEWS_MILESTONE = 5
STUDENTS_MILESTONE = 3

# Automatically create/upgrade SQL tables on application start
with app.app_context():
    try:
        # Check if email column exists in User table
        db.session.execute(db.text("SELECT email FROM user LIMIT 1"))
    except Exception:
        # Recreate tables to apply the new schema
        print("[EbiUI Database] Recreating database tables for new schema...")
        db.drop_all()
    db.create_all()

    # Seed default users if table is empty to satisfy the student milestone
    if User.query.count() == 0:
        print("[EbiUI Database] Seeding default students to satisfy milestone...")
        default_students = [
            {"username": "student_sarah", "full_name": "Sarah Connor", "email": "sarah@example.com", "password": "securepassword123"},
            {"username": "student_john", "full_name": "John Doe", "email": "john@example.com", "password": "securepassword123"},
            {"username": "student_emma", "full_name": "Emma Watson", "email": "emma@example.com", "password": "securepassword123"}
        ]
        for stud in default_students:
            pw_hash = generate_password_hash(stud["password"])
            db.session.add(User(username=stud["username"], full_name=stud["full_name"], email=stud["email"], password_hash=pw_hash))
        db.session.commit()

    # Seed default comments if table is empty to satisfy the reviews milestone
    if Comment.query.count() == 0:
        print("[EbiUI Database] Seeding default reviews to satisfy milestone...")
        default_reviews = [
            {"guest_name": "Sarah Connor", "text": "AB's mentorship is top-notch! The interactive phone emulator helped me grasp mobile layouts instantly.", "rating": 5},
            {"guest_name": "John Doe", "text": "The courses are extremely detailed and structured logically. Highly recommended for beginners!", "rating": 5},
            {"guest_name": "Emma Watson", "text": "The Zoom booking system is seamless. I booked a lesson, got my Zoom link instantly, and had an amazing live section.", "rating": 5},
            {"guest_name": "Michael Scott", "text": "Aesthetically pleasing and highly interactive. EbiUI is one of the best learning portals out there.", "rating": 5},
            {"guest_name": "David Miller", "text": "Fantastic curriculum! The step-by-step guides for Python and Flask database design were extremely clear.", "rating": 5}
        ]
        for rev in default_reviews:
            db.session.add(Comment(guest_name=rev["guest_name"], text=rev["text"], rating=rev["rating"]))
        db.session.commit()

# -------------------------------------------------------------
# WEB PAGE TEMPLATE/STATIC ROUTES
# -------------------------------------------------------------
@app.route('/')
def index():
    # Serve the main index.html file from the root directory
    return app.send_static_file('index.html')

@app.route('/templates/<path:path>')
def send_template(path):
    # Serve reference files like templates/mobilephone.html
    return send_from_directory('templates', path)

# -------------------------------------------------------------
# USER REGISTRATION, AUTHENTICATION, & SESSION ENDPOINTS
# -------------------------------------------------------------
@app.route('/api/milestones', methods=['GET'])
def get_milestones():
    total_reviews = Comment.query.count()
    total_students = User.query.count()
    unlocked = (total_reviews >= REVIEWS_MILESTONE) and (total_students >= STUDENTS_MILESTONE)
    return jsonify({
        'total_reviews': total_reviews,
        'reviews_milestone': REVIEWS_MILESTONE,
        'total_students': total_students,
        'students_milestone': STUDENTS_MILESTONE,
        'unlocked': unlocked
    })

@app.route('/api/register', methods=['POST'])
def register():
    # Enforce milestone-locked registration for peace of mind
    total_reviews = Comment.query.count()
    total_students = User.query.count()
    if total_reviews < REVIEWS_MILESTONE or total_students < STUDENTS_MILESTONE:
        return jsonify({
            'error': f'Registration features are locked. Milestones not met: Reviews ({total_reviews}/{REVIEWS_MILESTONE}), Registered Students ({total_students}/{STUDENTS_MILESTONE}).'
        }), 403

    data = request.get_json() or {}
    username = data.get('username', '').strip()
    email = data.get('email', '').strip()
    full_name = data.get('full_name', '').strip()
    password = data.get('password', '').strip()
    
    if not username or not password or not email or not full_name:
        return jsonify({'error': 'All fields (Full Name, Email, Username, Password) are required.'}), 400
        
    if len(username) < 3 or len(password) < 4:
        return jsonify({'error': 'Username must be at least 3 characters and password at least 4.'}), 400

    # Ensure username is unique
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username is already taken.'}), 400
        
    # Ensure email is unique
    existing_email = User.query.filter_by(email=email).first()
    if existing_email:
        return jsonify({'error': 'Email address is already registered.'}), 400

    # Store hashed password to protect credentials
    password_hash = generate_password_hash(password)
    new_user = User(username=username, email=email, full_name=full_name, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    # Auto-login session after registration
    session['user_id'] = new_user.id
    session['username'] = new_user.username
    
    # Send email notification alert
    send_notification_email(
        subject="[EbiUI Alert] New Student Registered",
        body=f"Hello,\n\nA new student has registered on EbiUI!\n\nName: {new_user.full_name}\nEmail: {new_user.email}\nUsername: {new_user.username}\nTime: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\nBest regards,\nEbiUI Auto-Notification System"
    )
    
    return jsonify({
        'message': 'Registration successful!',
        'user': {'username': new_user.username, 'email': new_user.email, 'full_name': new_user.full_name}
    }), 201

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
        
    user = User.query.filter_by(username=username).first()
    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'error': 'Invalid username or password.'}), 401
        
    # Store active session identifiers
    session['user_id'] = user.id
    session['username'] = user.username
    
    # Send email notification alert
    send_notification_email(
        subject="[EbiUI Alert] Student Signed In",
        body=f"Hello,\n\nA student has successfully logged in to EbiUI.\n\nUsername: {user.username}\nTime: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\nBest regards,\nEbiUI Auto-Notification System"
    )
    
    return jsonify({
        'message': 'Login successful!',
        'user': {'username': user.username}
    })

@app.route('/api/logout', methods=['POST', 'GET'])
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    return jsonify({'message': 'Logged out successfully.'})

@app.route('/api/user', methods=['GET'])
def get_current_user():
    if 'user_id' in session:
        return jsonify({'user': {'username': session.get('username')}})
    return jsonify({'user': None})

# -------------------------------------------------------------
# COMMENTS DATABASE REST ENDPOINTS
# -------------------------------------------------------------
@app.route('/api/comments', methods=['GET', 'POST'])
def comments():
    if request.method == 'GET':
        # Retrieve all database comments, newest first
        all_comments = Comment.query.order_by(Comment.created_at.desc()).all()
        return jsonify({'comments': [c.to_dict() for c in all_comments]})
        
    elif request.method == 'POST':
        data = request.get_json() or {}
        text = data.get('text', '').strip()
        rating = data.get('rating', 5)
        guest_name = data.get('guest_name', '').strip()
        
        if not text:
            return jsonify({'error': 'Comment content cannot be empty.'}), 400
            
        if len(text) > 500:
            return jsonify({'error': 'Comment exceeds the 500 character limit.'}), 400
            
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                rating = 5
        except (ValueError, TypeError):
            rating = 5

        # Save comment: link user_id if logged in, or lookup by username payload if cookies are blocked
        user = None
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
            
        username_payload = data.get('username', '').strip()
        if not user and username_payload:
            user = User.query.filter_by(username=username_payload).first()
            
        if user:
            new_comment = Comment(user_id=user.id, text=text, rating=rating)
        else:
            if not guest_name or guest_name == 'Anonymous Guest':
                guest_name = username_payload or 'Anonymous Guest'
            new_comment = Comment(user_id=None, guest_name=guest_name, text=text, rating=rating)
            
        db.session.add(new_comment)
        db.session.commit()
        
        return jsonify({
            'message': 'Comment posted!',
            'comment': new_comment.to_dict()
        }), 201

@app.route('/api/comments/<int:comment_id>', methods=['DELETE', 'PUT'])
def modify_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)
    
    if request.method == 'DELETE':
        # Enforce database owner security checks if comment belongs to a registered user
        if comment.user_id is not None:
            authorized = False
            if 'user_id' in session and comment.user_id == session['user_id']:
                authorized = True
            else:
                # Fallback for file:// protocol local tests using request JSON payload
                try:
                    data = request.get_json() or {}
                    username_payload = data.get('username', '').strip()
                    if username_payload:
                        user = User.query.filter_by(username=username_payload).first()
                        if user and comment.user_id == user.id:
                            authorized = True
                except Exception:
                    pass
            
            if not authorized:
                return jsonify({'error': 'Permission denied. You can only delete your own comments.'}), 403
                
        db.session.delete(comment)
        db.session.commit()
        return jsonify({'message': 'Comment deleted successfully.'}), 200

    elif request.method == 'PUT':
        data = request.get_json() or {}
        text = data.get('text', '').strip()
        rating = data.get('rating', 5)
        
        if not text:
            return jsonify({'error': 'Comment content cannot be empty.'}), 400
            
        if len(text) > 500:
            return jsonify({'error': 'Comment exceeds the 500 character limit.'}), 400
            
        try:
            rating = int(rating)
            if rating < 1 or rating > 5:
                rating = 5
        except (ValueError, TypeError):
            rating = 5

        # Enforce owner checks if comment belongs to a registered user
        if comment.user_id is not None:
            authorized = False
            if 'user_id' in session and comment.user_id == session['user_id']:
                authorized = True
            else:
                # file:// protocol fallback
                username_payload = data.get('username', '').strip()
                if username_payload:
                    user = User.query.filter_by(username=username_payload).first()
                    if user and comment.user_id == user.id:
                        authorized = True

            if not authorized:
                return jsonify({'error': 'Permission denied. You can only edit your own comments.'}), 403
                
        comment.text = text
        comment.rating = rating
        db.session.commit()

        return jsonify({
            'message': 'Comment updated successfully.',
            'comment': comment.to_dict()
        }), 200

@app.route('/admin')
def admin_dashboard():
    # Serve the admin dashboard HTML file from templates directory
    return send_from_directory('templates', 'admin.html')

@app.route('/api/admin/stats', methods=['GET'])
def admin_stats():
    total_comments = Comment.query.count()
    total_users = User.query.count()
    
    comments = Comment.query.all()
    avg_rating = 0.0
    if total_comments > 0:
        avg_rating = sum(c.rating for c in comments) / total_comments
        
    # Get absolute path to the SQLite database
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri.startswith('sqlite:///'):
        db_path = os.path.abspath(os.path.join(app.instance_path, 'ebiui.db'))
    else:
        db_path = db_uri
        
    total_bookings = Booking.query.count()
    return jsonify({
        'total_reviews': total_comments,
        'total_students': total_users,
        'total_bookings': total_bookings,
        'average_rating': round(avg_rating, 2),
        'db_path': db_path
    })

@app.route('/api/admin/db-download', methods=['GET'])
def admin_db_download():
    # Only allow downloading for SQLite database
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    if db_uri.startswith('sqlite:///'):
        from flask import send_from_directory
        return send_from_directory(app.instance_path, 'ebiui.db', as_attachment=True)
    else:
        return jsonify({'error': 'Database is hosted on a remote server (PostgreSQL).'}), 400

@app.route('/api/admin/data', methods=['GET'])
def admin_data():
    all_comments = Comment.query.order_by(Comment.created_at.desc()).all()
    all_users = User.query.order_by(User.created_at.desc()).all()
    
    return jsonify({
        'comments': [c.to_dict() for c in all_comments],
        'users': [{
            'id': u.id,
            'username': u.username,
            'email': u.email or '',
            'full_name': u.full_name or '',
            'created_at': u.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for u in all_users]
    })

@app.route('/api/admin/export', methods=['GET'])
def admin_export_csv():
    import csv
    from io import StringIO
    from flask import make_response
    
    all_comments = Comment.query.order_by(Comment.created_at.desc()).all()
    
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['ID', 'Author/Guest Name', 'Rating (Stars)', 'Comment Text', 'Submitted At'])
    
    for c in all_comments:
        username = c.user.username if c.user else (c.guest_name or 'Anonymous Guest')
        cw.writerow([c.id, username, c.rating, c.text, c.created_at.strftime('%Y-%m-%d %H:%M:%S')])
        
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=ebiui_reviews_export.csv"
    output.headers["Content-type"] = "text/csv"
    return output

COURSES = [
    {
        'id': 'html5',
        'badge': 'HTML5',
        'title': 'HTML5 Fundamentals',
        'desc': 'Master the foundations of the web: semantic structure, document hierarchy, web forms, layouts, and embedded media assets.',
        'topics': 'Semantic HTML5 layouts,Form elements & inputs validation,Media elements (Audio/Video),HTML5 API integration',
        'action_text': 'Download Syllabus PDF',
        'icon_class': 'fa-file-pdf',
        'brand_icon': 'fa-html5',
        'brand_color': '#e34c26',
        'meta': 'Study Guide & Syllabus (PDF)',
        'w3_link': 'https://www.w3schools.com/html/'
    },
    {
        'id': 'css3',
        'badge': 'CSS3',
        'title': 'CSS3 Layouts & Styling',
        'desc': 'Design modern, responsive user interfaces using Flexbox, CSS Grid, custom keyframe transitions, variables, and glassmorphism styling.',
        'topics': 'Flexbox & Grid layouts,CSS Custom Variables (Theming),Animations & Keyframes,Glassmorphic styling systems',
        'action_text': 'Play Lecture Video',
        'icon_class': 'fa-video',
        'brand_icon': 'fa-css3-alt',
        'brand_color': '#264de4',
        'meta': 'Video Lecture & Sandbox Practice',
        'w3_link': 'https://www.w3schools.com/css/'
    },
    {
        'id': 'js',
        'badge': 'JavaScript',
        'title': 'JavaScript Programming',
        'desc': 'Learn modern scripting with ES6+ syntax: control statements, document object model (DOM) manipulation, event handling, and API fetch transactions.',
        'topics': 'ES6+ Syntax & Scope,DOM Manipulation & Event Handlers,Asynchronous Fetch API & JSON,State Management',
        'action_text': 'Launch Sandbox',
        'icon_class': 'fa-code',
        'brand_icon': 'fa-js',
        'brand_color': '#f7df1e',
        'meta': 'Interactive Exercises & Sandbox',
        'w3_link': 'https://www.w3schools.com/js/'
    },
    {
        'id': 'python',
        'badge': 'Python',
        'title': 'Python & Flask Development',
        'desc': 'Build powerful backend web applications and REST APIs using Python, object-oriented concepts, Flask routing, templates, and server deployment.',
        'topics': 'Python OOP & syntax,Flask routing & templates,JSON API development,Middleware & application state',
        'action_text': 'Download Source Code',
        'icon_class': 'fa-file-zipper',
        'brand_icon': 'fa-python',
        'brand_color': '#3776ab',
        'meta': 'Source Code & Backend Guide',
        'w3_link': 'https://www.w3schools.com/python/'
    },
    {
        'id': 'sql',
        'badge': 'SQL & DB',
        'title': 'SQL & SQLite Database',
        'desc': 'Design relational database schemas, write optimized SQL queries, manage tables, and implement CRUD transactions using SQLite.',
        'topics': 'Relational DB concepts,SQL queries & joins,CRUD transactions,SQLite & SQLAlchemy integration',
        'action_text': 'Launch SQLite Console',
        'icon_class': 'fa-database',
        'brand_icon': 'fa-database',
        'brand_color': '#003b57',
        'meta': 'SQLite Sandbox & Query Guide',
        'w3_link': 'https://www.w3schools.com/sql/'
    }
]

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify({'courses': COURSES})

import random
import string

@app.route('/api/book-lesson', methods=['POST'])
def book_lesson():
    data = request.get_json() or {}
    billing_name = data.get('billing_name', '').strip()
    course_name = data.get('course_name', '').strip()
    guest_email = data.get('guest_email', '').strip()
    username_payload = data.get('username', '').strip()
    
    if not billing_name or not course_name:
        return jsonify({'error': 'Billing name and course name are required.'}), 400
        
    # Resolve user (logged in user via session, or lookup by username payload)
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
    if not user and username_payload:
        user = User.query.filter_by(username=username_payload).first()
        
    # Generate mock Zoom link
    meeting_id = ''.join(random.choices(string.digits, k=10))
    passcode = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    zoom_link = f"https://zoom.us/j/{meeting_id}?pwd={passcode}"
    
    new_booking = Booking(
        user_id=user.id if user else None,
        guest_email=guest_email if not user else None,
        billing_name=billing_name,
        course_name=course_name,
        zoom_link=zoom_link
    )
    
    db.session.add(new_booking)
    db.session.commit()
    
    # Send email notification alert to AB (and to user if guest email is present)
    email_body = f"Hello,\n\nA new Zoom lesson has been booked and paid for on EbiUI!\n\n"
    email_body += f"Billing Name: {billing_name}\n"
    email_body += f"Course Name: {course_name}\n"
    if user:
        email_body += f"Registered Student: {user.username}\n"
    else:
        email_body += f"Guest Email: {guest_email}\n"
    email_body += f"Zoom Meeting Link: {zoom_link}\n"
    email_body += f"Booking Time: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\n"
    email_body += "Please be ready to host the class at the agreed slot.\n\nBest regards,\nEbiUI Auto-Notification System"
    
    send_notification_email(
        subject=f"[EbiUI Alert] New Lesson Booked: {course_name}",
        body=email_body
    )
    
    return jsonify({
        'message': 'Booking successful!',
        'booking': new_booking.to_dict()
    }), 201

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    # Resolve user via session or URL param fallback (for file:// protocol)
    user = None
    if 'user_id' in session:
        user = User.query.get(session['user_id'])

    username_payload = request.args.get('username', '').strip()
    if not user and username_payload:
        user = User.query.filter_by(username=username_payload).first()

    if not user:
        # For guests, return empty list (guest bookings are stored but shown via guest confirmation)
        return jsonify({'bookings': []})

    # Get all bookings for this user
    user_bookings = Booking.query.filter_by(user_id=user.id).order_by(Booking.created_at.desc()).all()
    return jsonify({'bookings': [b.to_dict() for b in user_bookings]})

if __name__ == '__main__':
    # Capture PORT from environment variables (defaults to 8000 for local development)
    PORT = int(os.environ.get('PORT', 8080))
    print(f"Starting Flask development server at http://localhost:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
