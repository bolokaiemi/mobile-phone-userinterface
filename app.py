from flask import Flask, send_from_directory, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    text = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to user
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.user.username,
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
        # Reject creation if user is not authenticated
        if 'user_id' not in session:
            return jsonify({'error': 'Authentication required. Please log in.'}), 401
            
        data = request.get_json() or {}
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({'error': 'Comment content cannot be empty.'}), 400
            
        if len(text) > 500:
            return jsonify({'error': 'Comment exceeds the 500 character limit.'}), 400
            
        new_comment = Comment(user_id=session['user_id'], text=text)
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

if __name__ == '__main__':
    # Capture PORT from environment variables (defaults to 8000 for local development)
    PORT = int(os.environ.get('PORT', 8000))
    print(f"Starting Flask development server at http://localhost:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
