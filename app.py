from flask import Flask, send_from_directory
import os

# Initialize Flask app, pointing the static files folder to the root directory
# to match the native structure of your GitHub Pages deployment.
app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    # Serve the main index.html file from the root directory
    return app.send_static_file('index.html')

@app.route('/templates/<path:path>')
def send_template(path):
    # Serve reference files like templates/mobilephone.html
    return send_from_directory('templates', path)

if __name__ == '__main__':
    # Capture PORT from environment variables (defaults to 8000 for local development)
    PORT = int(os.environ.get('PORT', 8000))
    print(f"Starting Flask development server at http://localhost:{PORT}")
    app.run(host='0.0.0.0', port=PORT, debug=True)
