# EbiUI Hub: Interactive Mobile UI Emulator & Learning Portal

EbiUI is a modern, high-fidelity web-based Android 14 Custom ROM emulator. In this version, the phone emulator is wrapped in a premium modern web dashboard. The project now features a public review feed with star ratings and social media sharing integration, alongside a secure, dedicated student portal for accessing educational resources.

The application uses a **Flask** backend with **SQLAlchemy** (supporting both SQLite for local development and PostgreSQL for production deployments).

---

## Key Features

- 📱 **Realistic Device Chassis Mockup**: Physical-looking bezels, camera notch/punch-hole, side power/volume keys, speaker grille details, and responsive collapse.
- 🌐 **Multi-Language Support (i18n)**: Toggle system languages dynamically between English (🇺🇸), Dutch (🇳🇱), German (🇩🇪), Spanish (🇪🇸), and French (🇫🇷).
- 🎨 **Material You Dynamic Theming**: Shift the entire accent color system (buttons, headers, inputs) via Settings App.
- 🌗 **Light / Dark Mode Selector**: Instantly switches theme configurations and display contrasts.
- 🖼️ **Interactive Wallpaper Chooser**: Cycle through custom abstract backgrounds, including a premium default neon liquid wave gradient.
- 💬 **Gemini AI Assistant**: A built-in terminal chat bot that handles interactive commands (`joke`, `wallpaper`, `dark`, `light`, etc.).
- 📞 **Dialer / Phone App**: Operable number dial keypad emitting synthesized DTMF beep tones (Web Audio API) and call connect overlays.
- 💬 **WhatsApp Simulation**: Select Mr. Boss, Mom, or Gemini AI Bot from the chat log and interact using automated message delays and response scripts.
- 📷 **Camera Viewfinder Filter Mode**: Toggle visual styles (grayscale, retro sepia, neon hue-rotate) with simulated photo capture screen flashes.
- 🛒 **Web Preview Mode**: Simulates app launcher grids leading to official Google Play Store, PayPal, TikTok, and Chrome previews.

### New Features in this Version
- 💬 **Public Review System (No Login Required)**:
  - Users can submit feedback directly using an interactive **1-to-5 star rating selector** and a review comment box.
  - Optional custom display names (defaults to "Anonymous Guest" if left blank).
- 📢 **Social Media Sharing**:
  - Automatically pops up a sharing dialog after a review is submitted.
  - Includes custom, encouraging labels: `share on WhatsApp`, `share on Facebook`, and `share on Instagram`.
- 🎓 **Student Learning Portal & Dynamic Navbar Dropdown**:
  - Secure authentication and registration forms separated into a dedicated portal card.
  - Unlocks a modern student dashboard with downloadable course syllabi, lecture video launch buttons, and coding sandboxes once logged in.
  - **Courses Navbar Dropdown**: Automatically populates courses (HTML5, CSS3, JavaScript, Python, SQL Database) in the header navigation upon student login. Clicking any course item redirects the page to the portal view and opens its details modal.
- 💳 **Premium Live Tutoring Upgrade**:
  - Integrated a direct premium payment checkout modal for live 1-on-1 mentorship with Mr. Bolokaiemi Ebi.
  - Accessible via dashboard checkboxes, details modals, and footer shortcuts.
- 🌅 **Premium Glassmorphic Footer**:
  - Displays a clean copyright showing the year **2026** (when EbiUI was created).
  - Contains an About section, list of course details links (restricted to logged-in students), and quick contact credentials (phone, email, academy location).
  - Features a **"Book Live Session"** call-to-action button that triggers the mentorship payment gateway directly.
- ⚠️ **Disclaimer Notice**:
  - Added a notice to the Emulator Tips panel advising users that the site is an interactive web preview and that they should view links online rather than downloading files onto their local machines.
- 🛠️ **Admin Dashboard Cross-Origin Support**:
  - Resolved dynamic `API_BASE` links inside the Admin Dashboard. Total comments, student accounts, rating stats, database downloads, and CSV exports load successfully regardless of whether the console is run via Flask, local file protocol (`file://`), or local preview web servers.

---

## Technical Stack

- **Frontend Core**: Semantic HTML5, Vanilla CSS3 (flexbox, grid, glassmorphic card components, keyframe animations), ES6 JavaScript
- **Backend Core**: Python, Flask, Flask-SQLAlchemy (supporting dynamic CORS configurations)
- **Database**: SQLite (local dev), PostgreSQL (production)
- **Icons**: Font Awesome 6.6.0
- **Typography**: Google Fonts (Outfit)

---

## Getting Started Locally

### Prerequisites
Make sure you have **Python 3.x** installed.

### Installation & Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Bolokaiemi/mobile-phone-userinterface.git
   cd mobile-phone-userinterface
   ```
2. Set up a virtual environment and activate it:
   ```bash
   python -m venv .venv
   # Windows (CMD):
   .venv\Scripts\activate.bat
   # Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   # macOS/Linux:
   source .venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask development server:
   ```bash
   python app.py
   ```
5. Open your browser and navigate to **`http://localhost:8080`**.

---

## Project Structure

```text
mobile-phone-userinterface/
├── app.py              # Flask server with SQL models and REST API routes
├── app.js              # State management, emulator applications, and API fetch events
├── index.html          # Main HTML structure and dashboard wrapper layout
├── wallpaper_neon.png  # Neon liquid wallpaper asset
├── requirements.txt    # Python packages (Flask, Flask-SQLAlchemy, etc.)
├── README.md           # Project documentation
├── instance/
│   └── ebiui.db        # Local SQLite database
├── static/
│   └── styles.css      # Custom dashboard tokens, glassmorphism, responsive styles
└── templates/
    ├── index.html      # Synchronized template backup of index.html
    ├── admin.html      # Admin Feedback & Student Dashboard console
    └── mobilephone.html # Original static reference design file
```

---

## Author
- **Bolokaiemi Ebi** - *Initial UI design & Android 14 EbiUI ROM emulation*
