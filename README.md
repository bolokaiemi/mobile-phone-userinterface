# Android 14 EbiUI - Interactive Mobile UI Emulator

EbiUI is a modern, high-fidelity web-based Android 14 Custom ROM emulator. Built using HTML5, Vanilla CSS3, and ES6 JavaScript, this application wraps a simulated Android launcher inside a realistic physical smartphone bezel mockup. On mobile devices, it responsively collapses the outer chassis to act as a native fullscreen web app.

[View Live Project Demo (GitHub Pages)](https://YOUR_USERNAME.github.io/mobileuserinterfaceProject6/)

---

## Key Features

- 📱 **Realistic Device Chassis Mockup**: Physical-looking bezels, camera notch/punch-hole, side power/volume keys, and speaker grille details.
- 🌐 **Multi-Language Support (i18n)**: Toggle system languages between English (🇺🇸), Dutch (🇳🇱), German (🇩🇪), Spanish (🇪🇸), and French (🇫🇷) dynamically using the status bar globe icon or the Settings App.
- 🎨 **Material You Dynamic Theming**: Shift the entire accent color system (buttons, headers, inputs) dynamically via settings, inspired by Android 14 design language.
- 🌗 **Light / Dark Mode Selector**: Instantly switches theme configurations and display contrasts.
- 🖼️ **Interactive Wallpaper Chooser**: Cycle through custom abstract backgrounds, including a premium default neon liquid wave gradient.
- ⚙️ **Status Bar Toggles**: Click the battery icon to simulate charging animations, or toggle the WiFi indicator state with live status toast alerts.
- 💬 **Gemini AI Assistant**: A built-in terminal chat bot that handles interactive commands:
  - Type `help` to list commands.
  - Type `wallpaper [1-4]` to change launcher wallpaper dynamically.
  - Type `joke` to receive funny programmer jokes.
  - Type `dark` or `light` to swap visual layouts.
- 📞 **Dialer / Phone App**: Operable number dial keypad emitting simulated DTMF beep tones (using Web Audio synthesizer) and simulated call connect overlay.
- 💬 **WhatsApp Simulation**: Select Mr. Boss, Mom, or Gemini AI Bot from the chat log and interact using automated message delays and response scripts that translate dynamically!
- 📝 **Notes App**: Create note titles and descriptions, save notes, and delete them. Notes are fully stored and persisted across page reloads via `localStorage`.
- 🧮 **Calculator App**: Operable mathematical calculation grid.
- 📷 **Camera Viewfinder Filter Mode**: Toggle different visual styles (grayscale, retro sepia, neon hue-rotate) in the viewfinder stream, with simulated photo capture screen flashes.
- 🛍️ **Direct Download / Installation Links**: Non-simulated apps (such as PayPal, Google Drive, Gmail, Gboard, Yahoo Mail, etc.) redirect directly to their official Google Play Store download listings in the current browser window, matching standard launcher behaviors.

---

## Technical Stack

- **Frontend Core**: Semantic HTML5 & ES6 JavaScript
- **Styling**: Modern CSS3 (CSS Variables, Flexbox, CSS Grid, Glassmorphism, Keyframe Animations)
- **Icons**: Font Awesome 6.6.0
- **Typography**: Google Fonts (Outfit)
- **Web APIs**: Web Audio API (Synthesized tone pad beeps), Web Storage API (`localStorage` for note persistence)
- **Local Dev Server**: Python HTTP Server

---

## Getting Started Locally

### Prerequisites
Make sure you have Python installed on your machine to host the local directory.

### Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/mobileuserinterfaceProject6.git
   ```
2. Navigate into the project folder:
   ```bash
   cd mobileuserinterfaceProject6
   ```
3. Run the development server script:
   ```bash
   python app.py
   ```
   *(Or if using the PyCharm local virtual environment on Windows)*:
   ```bash
   .\.venv\Scripts\python.exe app.py
   ```
4. Open your browser and navigate to **`http://localhost:8000`**.

---

## Project Structure

```text
mobileuserinterfaceProject6/
├── index.html          # Main HTML structure & phone chassis skeleton
├── app.js              # State management, clock tasks, mini-app logic & simulated databases
├── app.py              # Light Python caching-disabled local preview server
├── wallpaper_neon.png  # Generated abstract default UI wallpaper asset
├── README.md           # Documentation for Github profiles
├── static/             # Static assets folder
│   └── styles.css      # Theme tokens, glassmorphism, app views, responsive media queries
└── templates/          # Templates folder (e.g. for Flask deployment)
    ├── index.html      # Synchronized copy of main HTML
    └── mobilephone.html # Original static reference file
```

---

## Author
- **Bolokaiemi Ebi** - *Initial UI design & Android 14 EbiUI ROM emulation*
