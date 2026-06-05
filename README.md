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
- 🛍️ **Direct Download / Installation Links**: Simulates redirection to official Google Play Store download listings in the browser.

### New Features in this Version
- 💬 **Public Review System (No Login Required)**:
  - Users can submit feedback directly using an interactive **1-to-5 star rating selector** and a review comment box.
  - Optional custom display names (defaults to "Anonymous Guest" if left blank).
- 📢 **Social Media Sharing**:
  - Automatically pops up a sharing dialog after a review is submitted.
  - Includes custom, encouraging labels: `share on WhatsApp`, `share on Facebook`, and `share on Instagram`.
  - Copy-to-clipboard integration for platforms like Instagram that do not support pre-filled message links.
- 🎓 **Student Learning Portal**:
  - Secure authentication and registration forms separated into a dedicated portal card.
  - Unlocks a modern student dashboard with downloadable course syllabi, lecture video launch buttons, and coding sandboxes once logged in.

---

## Technical Stack

- **Frontend Core**: Semantic HTML5, Vanilla CSS3 (flexbox, grid, glassmorphism, keyframe animations), ES6 JavaScript
- **Backend Core**: Python, Flask, Flask-SQLAlchemy
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
    └── mobilephone.html # Original static reference file
```

---

## Author
- **Bolokaiemi Ebi** - *Initial UI design & Android 14 EbiUI ROM emulation*
