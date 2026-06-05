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

# Automatically create SQL tables on application start
with app.app_context():
    db.create_all()

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
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()
    
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400
        
    if len(username) < 3 or len(password) < 4:
        return jsonify({'error': 'Username must be at least 3 characters and password at least 4.'}), 400

    # Ensure username is unique
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'error': 'Username is already taken.'}), 400
        
    # Store hashed password to protect credentials
    password_hash = generate_password_hash(password)
    new_user = User(username=username, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()
    
    # Auto-login session after registration
    session['user_id'] = new_user.id
    session['username'] = new_user.username
    
    # Send email notification alert
    send_notification_email(
        subject="[EbiUI Alert] New Student Registered",
        body=f"Hello,\n\nA new student has registered on EbiUI!\n\nUsername: {new_user.username}\nTime: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC\n\nBest regards,\nEbiUI Auto-Notification System"
    )
    
    return jsonify({
        'message': 'Registration successful!',
        'user': {'username': new_user.username}
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

        # Save comment: link user_id if logged in, otherwise save guest name
        if 'user_id' in session:
            new_comment = Comment(user_id=session['user_id'], text=text, rating=rating)
        else:
            if not guest_name:
                guest_name = 'Anonymous Guest'
            new_comment = Comment(user_id=None, guest_name=guest_name, text=text, rating=rating)
            
        db.session.add(new_comment)
        db.session.commit()
        
        return jsonify({
            'message': 'Comment posted!',
            'comment': new_comment.to_dict()
        }), 201

@app.route('/api/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Authentication required.'}), 401
        
    comment = Comment.query.get_or_404(comment_id)
    
    # Enforce database owner security checks
    if comment.user_id != session['user_id']:
        return jsonify({'error': 'Permission denied. You can only delete your own comments.'}), 403
        
    db.session.delete(comment)
    db.session.commit()
    
    return jsonify({'message': 'Comment deleted successfully.'})

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
        
    return jsonify({
        'total_reviews': total_comments,
        'total_students': total_users,
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

if __name__ == '__main__':
    # Capture PORT from environment variables (defaults to 8000 for local development)
    PORT = int(os.environ.get('PORT', 8080))
    print(f"Starting Flask development server at http://localhost:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
