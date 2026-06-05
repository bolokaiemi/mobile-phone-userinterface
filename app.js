/**
 * Android 14 EbiUI - Interactive Emulator Application Logic
 * Created by: Bolokaiemi Ebi
 * Upgraded with Multi-Language Translation and Enhanced Home Navigation
 */

document.addEventListener('DOMContentLoaded', () => {
    // -------------------------------------------------------------
    // MULTI-LANGUAGE TRANSLATION DICTIONARY
    // -------------------------------------------------------------
    const translations = {
        sub_title: {
            en: "Android 14 Custom ROM",
            nl: "Android 14 Aangepaste ROM",
            de: "Android 14 Custom-ROM",
            es: "ROM Personalizada Android 14",
            fr: "ROM Personnalisée Android 14"
        },
        weather_desc: {
            en: "Partly Cloudy",
            nl: "Gedeeltelijk Bewolkt",
            de: "Leicht Bewölkt",
            es: "Parcialmente Nublado",
            fr: "Partiellement Nuageux"
        },
        weather_city: {
            en: "Herne, DE",
            nl: "Herne, Deutschland",
            de: "Herne, Deutschland",
            es: "Herne, Deutschland",
            fr: "Herne, Deutschland"
        },
        sys_bar_title: {
            en: "System Bar",
            nl: "Systeembalk",
            de: "Systemleiste",
            es: "Barra de Control",
            fr: "Barre de Contrôle"
        },
        // Launcher App Labels
        app_playstore: { en: "Play Store", nl: "Play Store", de: "Play Store", es: "Play Store", fr: "Play Store" },
        app_call: { en: "Phone", nl: "Telefoon", de: "Telefon", es: "Teléfono", fr: "Téléphone" },
        app_paypal: { en: "PayPal", nl: "PayPal", de: "PayPal", es: "PayPal", fr: "PayPal" },
        app_drive: { en: "Drive", nl: "Drive", de: "Drive", es: "Drive", fr: "Drive" },
        app_photos: { en: "Photos", nl: "Foto's", de: "Fotos", es: "Fotos", fr: "Photos" },
        app_camera: { en: "Camera", nl: "Camera", de: "Kamera", es: "Cámara", fr: "Appareil photo" },
        app_messages: { en: "Messages", nl: "Berichten", de: "Nachrichten", es: "Mensajes", fr: "Messages" },
        app_chrome: { en: "Chrome", nl: "Chrome", de: "Chrome", es: "Chrome", fr: "Chrome" },
        app_whatsapp: { en: "WhatsApp", nl: "WhatsApp", de: "WhatsApp", es: "WhatsApp", fr: "WhatsApp" },
        app_findmydevice: { en: "Find Device", nl: "Zoek Apparaat", de: "Gerät Finden", es: "Buscar Dispositivo", fr: "Trouver Appareil" },
        app_google: { en: "Google", nl: "Google", de: "Google", es: "Google", fr: "Google" },
        app_yahoomail: { en: "Yahoo Mail", nl: "Yahoo Mail", de: "Yahoo Mail", es: "Yahoo Mail", fr: "Yahoo Mail" },
        app_gmail: { en: "Gmail", nl: "Gmail", de: "Gmail", es: "Gmail", fr: "Gmail" },
        app_ringtones: { en: "Ringtones", nl: "Beltonen", de: "Klingeltöne", es: "Tonos", fr: "Sonneries" },
        app_youtube: { en: "YouTube", nl: "YouTube", de: "YouTube", es: "YouTube", fr: "YouTube" },
        app_tiktok: { en: "TikTok", nl: "TikTok", de: "TikTok", es: "TikTok", fr: "TikTok" },
        app_clock: { en: "Clock", nl: "Klok", de: "Uhr", es: "Reloj", fr: "Horloge" },
        app_otto: { en: "Otto", nl: "Otto", de: "Otto", es: "Otto", fr: "Otto" },
        app_weather: { en: "Weather", nl: "Weer", de: "Wetter", es: "Tiempo", fr: "Météo" },
        app_instagram: { en: "Instagram", nl: "Instagram", de: "Instagram", es: "Instagram", fr: "Instagram" },
        app_map: { en: "Map", nl: "Kaart", de: "Karte", es: "Mapa", fr: "Carte" },
        app_calendar: { en: "Calendar", nl: "Agenda", de: "Kalender", es: "Calendario", fr: "Calendrier" },
        app_microsoft: { en: "Microsoft", nl: "Microsoft", de: "Microsoft", es: "Microsoft", fr: "Microsoft" },
        app_recorder: { en: "Recorder", nl: "Recorder", de: "Recorder", es: "Grabadora", fr: "Enregistreur" },
        app_notes: { en: "Notes", nl: "Notities", de: "Notizen", es: "Notas", fr: "Notes" },
        app_gboard: { en: "Gboard", nl: "Gboard", de: "Gboard", es: "Gboard", fr: "Gboard" },
        app_ytmusic: { en: "YT Music", nl: "YT Music", de: "YT Music", es: "YT Music", fr: "YT Music" },
        app_googletv: { en: "Google TV", nl: "Google TV", de: "Google TV", es: "Google TV", fr: "Google TV" },
        app_gemini: { en: "Gemini AI", nl: "Gemini AI", de: "Gemini AI", es: "Gemini AI", fr: "Gemini AI" },
        app_internet: { en: "Internet", nl: "Internet", de: "Internet", es: "Internet", fr: "Internet" },
        app_files: { en: "Files", nl: "Bestanden", de: "Dateien", es: "Archivos", fr: "Fichiers" },
        app_settings: { en: "Settings", nl: "Instellingen", de: "Einstellungen", es: "Ajustes", fr: "Paramètres" },
        
        // Navigation & Search placeholders
        search_placeholder: {
            en: "Search...",
            nl: "Zoeken...",
            de: "Suchen...",
            es: "Buscar...",
            fr: "Rechercher..."
        },
        nav_home_btn: {
            en: "Home",
            nl: "Start",
            de: "Start",
            es: "Inicio",
            fr: "Accueil"
        },
        dialer_placeholder: {
            en: "Dial number...",
            nl: "Kies nummer...",
            de: "Nummer wählen...",
            es: "Marcar número...",
            fr: "Composer..."
        },
        calling_status: {
            en: "Calling...",
            nl: "Bellen...",
            de: "Anrufen...",
            es: "Llamando...",
            fr: "Appel..."
        },
        // Notes app placeholders & header
        notes_title_placeholder: {
            en: "Note Title...",
            nl: "Notitietitel...",
            de: "Notiztitel...",
            es: "Título de nota...",
            fr: "Titre de note..."
        },
        notes_body_placeholder: {
            en: "Write something...",
            nl: "Schrijf iets...",
            de: "Schreibe etwas...",
            es: "Escribe algo...",
            fr: "Écrire quelque chose..."
        },
        notes_save_btn: {
            en: "Save Note",
            nl: "Notitie Opslaan",
            de: "Notiz Speichern",
            es: "Guardar Nota",
            fr: "Sauvegarder"
        },
        notes_saved_header: {
            en: "Saved Notes",
            nl: "Opgeslagen Notities",
            de: "Gespeicherte Notizen",
            es: "Notas Guardadas",
            fr: "Notes Enregistrées"
        },
        wa_placeholder: {
            en: "Type a message...",
            nl: "Typ een bericht...",
            de: "Nachricht schreiben...",
            es: "Escribe un mensaje...",
            fr: "Écrire un message..."
        },
        gemini_placeholder: {
            en: "Ask Gemini...",
            nl: "Vraag Gemini...",
            de: "Gemini fragen...",
            es: "Preguntar a Gemini...",
            fr: "Demander à Gemini..."
        },
        gemini_greeting: {
            en: "Hello! I'm Gemini, your virtual assistant built into EbiUI. Ask me anything, or type command hints like 'help', 'wallpaper', 'time', or 'joke'.",
            nl: "Hallo! Ik ben Gemini, jouw virtuele assistent in EbiUI. Vraag me alles, of typ help-commando's zoals 'help', 'wallpaper', 'time' of 'joke'.",
            de: "Hallo! Ich bin Gemini, dein virtueller Assistent in EbiUI. Frage mich alles oder tippe Befehlshinweise wie 'help', 'wallpaper', 'time' oder 'joke'.",
            es: "¡Hola! Soy Gemini, tu asistente virtual integrado en EbiUI. Pregúntame lo que quieras o escribe comandos como 'help', 'wallpaper', 'time' o 'joke'.",
            fr: "Bonjour ! Je suis Gemini, votre assistant virtuel intégré à EbiUI. Demandez-moi n'importe quoi ou tapez des commandes comme 'help', 'wallpaper', 'time' ou 'joke'."
        },
        // Settings translations
        settings_sec_lang: { en: "Language", nl: "Taal", de: "Sprache", es: "Idioma", fr: "Langue" },
        settings_sys_lang: { en: "System Language", nl: "Systeemtaal", de: "Systemsprache", es: "Idioma del Sistema", fr: "Langue du Système" },
        settings_sec_theme: { en: "Display & Theme", nl: "Scherm & Thema", de: "Anzeige & Design", es: "Pantalla y Tema", fr: "Affichage & Thème" },
        settings_dark_mode: { en: "Dark Mode", nl: "Donkere Modus", de: "Dunkelmodus", es: "Modo Oscuro", fr: "Mode Sombre" },
        settings_theme_color: { en: "Theme Primary Color", nl: "Primaire Themakleur", de: "Primäre Designfarbe", es: "Color Primario del Tema", fr: "Couleur Primaire" },
        settings_sec_wallpaper: { en: "Change Wallpaper", nl: "Achtergrond Wijzigen", de: "Hintergrundbild Ändern", es: "Cambiar Fondo", fr: "Changer le Fond" },
        settings_sec_about: { en: "About EbiUI", nl: "Over EbiUI", de: "Über EbiUI", es: "Acerca de EbiUI", fr: "À Propos de EbiUI" },
        about_model: { en: "Model:", nl: "Model:", de: "Modell:", es: "Modelo:", fr: "Modèle :" },
        about_version: { en: "OS Version:", nl: "Besturingssysteem:", de: "Betriebssystem:", es: "Versión de SO:", fr: "Version de l'OS :" },
        about_developer: { en: "Developer:", nl: "Ontwikkelaar:", de: "Entwickler:", es: "Desarrollador:", fr: "Développeur :" },
        about_build: { en: "Build:", nl: "Build:", de: "Build:", es: "Compilación:", fr: "Build :" },
        about_build_val: { en: "Stable Core OS", nl: "Stabiel Kernbesturingssysteem", de: "Stabiles Kernsystem", es: "SO Núcleo Estable", fr: "OS Principal Stable" },
        
        // Fallback generic card
        generic_playstore_btn: { en: "Open Play Store Link", nl: "Open Play Store Link", de: "Play Store Link Öffnen", es: "Abrir enlace de Play Store", fr: "Ouvrir le lien Play Store" },
        generic_home_btn: { en: "Return to Launcher", nl: "Terug naar Startscherm", de: "Zum Startbildschirm", es: "Volver al Lanzador", fr: "Retour au Lanceur" },
        
        // Desktop tip widgets
        tips_header: { en: "Android 14 EbiUI Launcher", nl: "Android 14 EbiUI Startscherm", de: "Android 14 EbiUI Launcher", es: "Lanzador Android 14 EbiUI", fr: "Lanceur Android 14 EbiUI" },
        tips_subtitle: { en: "Interactive emulator designed by Bolokaiemi Ebi.", nl: "Interactieve emulator ontworpen door Bolokaiemi Ebi.", de: "Interaktiver Emulator, entworfen von Bolokaiemi Ebi.", es: "Emulador interactivo diseñado por Bolokaiemi Ebi.", fr: "Émulateur interactif conçu par Bolokaiemi Ebi." },
        tips_item_1: { en: "Click app icons to open live mini-applications!", nl: "Klik op app-pictogrammen om live mini-applicaties te openen!", de: "Klicke auf App-Symbole, um live Mini-Apps zu öffnen!", es: "¡Haz clic en los iconos para abrir miniaplicaciones en vivo!", fr: "Cliquez sur les icônes d'applications pour ouvrir des mini-applications en direct !" },
        tips_item_2: { en: "Open Settings to toggle Dark Mode, change theme accents, and change wallpapers.", nl: "Open Instellingen om de Donkere Modus in te schakelen, themakleuren te wijzigen en achtergronden aan te passen.", de: "Öffne die Einstellungen, um den Dunkelmodus zu aktivieren, Akzentfarben zu ändern und Hintergrundbilder anzupassen.", es: "Abre Ajustes para alternar el Modo Oscuro, cambiar los colores del tema y los fondos.", fr: "Ouvrez les Paramètres pour basculer en mode sombre, changer les accents de thème et les fonds d'écran." },
        tips_item_3: { en: "Status bar shows live clock. Click the clock widget or weather card!", nl: "De statusbalk toont een live klok. Klik op de klokwidget of weerkaart!", de: "Die Statusleiste zeigt eine Live-Uhr. Klicke auf das Uhr-Widget oder die Wetterkarte!", es: "La barra de estado muestra la hora. ¡Haz clic en el widget de reloj o en la tarjeta del tiempo!", fr: "La barre d'état affiche l'horloge. Cliquez sur le widget horloge ou la carte météo !" },
        tips_item_4: { en: "Click the battery icon in the top right to simulate charging!", nl: "Klik op het batterij-icoon rechtsboven om opladen te simuleren!", de: "Klicke oben rechts auf das Batteriesymbol, um das Laden zu simulieren!", es: "¡Haz clic en el icono de la batería en la esquina superior derecha para simular la carga!", fr: "Cliquez sur l'icône de batterie en haut à droite pour simuler la charge !" },
        tips_item_5: { en: "Fully responsive! Try resizing your browser window or view on a phone.", nl: "Volledig responsive! Probeer uw browservenster te verkleinen of bekijk het op een telefoon.", de: "Vollständig responsiv! Ändere die Größe des Browserfensters oder öffne es auf dem Handy.", es: "¡Totalmente responsivo! Intenta cambiar el tamaño del navegador o míralo en un teléfono.", fr: "Entièrement réactif ! Essayez de redimensionner votre navigateur ou visualisez sur un téléphone." },
        tips_view_original: { en: "View Raw Original Page", nl: "Bekijk de Originele Pagina", de: "Originale Seite Anzeigen", es: "Ver Página Original", fr: "Voir la page originale" }
    };

    // -------------------------------------------------------------
    // DOM ELEMENTS
    // -------------------------------------------------------------
    const statusTime = document.getElementById('status-time');
    const widgetTime = document.getElementById('widget-time');
    const widgetDate = document.getElementById('widget-date');
    const statusBatteryBtn = document.getElementById('status-battery-btn');
    const batteryLevelText = document.getElementById('battery-level');
    const batteryIcon = document.getElementById('battery-icon');
    const batteryChargingIcon = document.getElementById('battery-charging-icon');
    const statusWifi = document.getElementById('status-wifi');

    // Language Dropdown Triggers
    const statusLangTrigger = document.getElementById('status-lang-trigger');
    const langDropdown = document.getElementById('lang-dropdown');
    const langOptions = document.querySelectorAll('.lang-option');
    const settingsLangSelect = document.getElementById('settings-lang-select');

    // Navigation Buttons
    const navBack = document.getElementById('nav-back');
    const navHome = document.getElementById('nav-home');
    const navRecents = document.getElementById('nav-recents');
    const appHeaderHomeBtn = document.getElementById('app-header-home-btn');
    const phoneScreen = document.getElementById('phone-screen');

    // App Overlay System
    const appOverlay = document.getElementById('app-overlay');
    const appOverlayTitle = document.getElementById('app-overlay-title');
    const appCloseBtn = document.getElementById('app-close-btn');
    const simApps = document.querySelectorAll('.sim-app');

    // Wallpaper and Accent
    const phoneWallpaper = document.getElementById('phone-wallpaper');

    // -------------------------------------------------------------
    // LANGUAGE STATE & MANAGEMENT (i18n)
    // -------------------------------------------------------------
    let currentLanguage = localStorage.getItem('ebiui_language') || 'en';

    function setLanguage(lang) {
        currentLanguage = lang;
        localStorage.setItem('ebiui_language', lang);

        // Update all data-translate elements
        document.querySelectorAll('[data-translate]').forEach(el => {
            const key = el.getAttribute('data-translate');
            if (translations[key] && translations[key][lang]) {
                el.innerHTML = translations[key][lang];
            }
        });

        // Update placeholders
        document.querySelectorAll('[data-translate-placeholder]').forEach(el => {
            const key = el.getAttribute('data-translate-placeholder');
            if (translations[key] && translations[key][lang]) {
                el.placeholder = translations[key][lang];
            }
        });

        // Sync Select menus
        if (settingsLangSelect) {
            settingsLangSelect.value = lang;
        }

        // Close lang dropdown overlay
        if (langDropdown) {
            langDropdown.classList.remove('active');
        }

        // Refresh time calculations & widgets
        updateClock();

        // If Notes is open, reload the list to reflect note templates
        if (activeAppId === 'notes') loadNotesList();
        
        // Translate simulated initial bubble for Gemini if it hasn't been closed
        const geminiInitial = document.getElementById('gemini-initial-bubble');
        if (geminiInitial) {
            geminiInitial.innerHTML = translations.gemini_greeting[lang];
        }

        // Send confirmation toast
        const confirmationMessages = {
            en: "System Language: English",
            nl: "Systeemtaal: Nederlands",
            de: "Systemsprache: Deutsch",
            es: "Idioma del Sistema: Español",
            fr: "Langue du Système: Français"
        };
        showNotification(confirmationMessages[lang]);
    }

    // Toggle dropdown status bar language menu
    if (statusLangTrigger) {
        statusLangTrigger.addEventListener('click', (e) => {
            e.stopPropagation();
            langDropdown.classList.toggle('active');
        });
    }

    // Bind dropdown options
    langOptions.forEach(opt => {
        opt.addEventListener('click', () => {
            const lang = opt.getAttribute('data-lang');
            setLanguage(lang);
        });
    });

    // Close language selector when clicking outside
    document.addEventListener('click', () => {
        if (langDropdown) langDropdown.classList.remove('active');
    });

    // Bind settings dropdown language selection
    if (settingsLangSelect) {
        settingsLangSelect.addEventListener('change', () => {
            setLanguage(settingsLangSelect.value);
        });
    }

    // -------------------------------------------------------------
    // DYNAMIC TIME & DATE
    // -------------------------------------------------------------
    function updateClock() {
        const now = new Date();
        
        // Lock time display to Germany (Europe/Berlin)
        const timeOptions = {
            timeZone: 'Europe/Berlin',
            hour: '2-digit',
            minute: '2-digit',
            hour12: false
        };
        const formatter = new Intl.DateTimeFormat('en-US', timeOptions);
        const parts = formatter.formatToParts(now);
        const hours = parts.find(p => p.type === 'hour').value;
        const minutes = parts.find(p => p.type === 'minute').value;
        
        const timeString = `${hours}:${minutes}`;
        if (statusTime) statusTime.textContent = timeString;
        if (widgetTime) widgetTime.textContent = timeString;

        // Choose Date Locale
        let locale = 'en-US';
        if (currentLanguage === 'nl') locale = 'nl-NL';
        if (currentLanguage === 'de') locale = 'de-DE';
        if (currentLanguage === 'es') locale = 'es-ES';
        if (currentLanguage === 'fr') locale = 'fr-FR';

        const dateOptions = { 
            timeZone: 'Europe/Berlin',
            weekday: 'long', 
            month: 'long', 
            day: 'numeric' 
        };
        const dateString = now.toLocaleDateString(locale, dateOptions);
        if (widgetDate) widgetDate.textContent = dateString;
    }
    
    // Run clock updates
    updateClock();
    setInterval(updateClock, 1000);

    // Initialize Language
    setLanguage(currentLanguage);

    // -------------------------------------------------------------
    // STATUS BAR TOGGLES
    // -------------------------------------------------------------
    let wifiActive = true;
    if (statusWifi) {
        statusWifi.addEventListener('click', () => {
            wifiActive = !wifiActive;
            if (wifiActive) {
                statusWifi.className = 'fa-solid fa-wifi';
                statusWifi.style.color = '';
                statusWifi.title = 'WiFi: Connected';
                showNotification(currentLanguage === 'nl' ? 'WiFi Verbonden' : 
                                 currentLanguage === 'de' ? 'WLAN Verbunden' : 
                                 currentLanguage === 'es' ? 'WiFi Conectado' : 
                                 currentLanguage === 'fr' ? 'WiFi Connecté' : 'WiFi Connected');
            } else {
                statusWifi.className = 'fa-solid fa-wifi';
                statusWifi.style.color = 'rgba(255,255,255,0.3)';
                statusWifi.title = 'WiFi: Disconnected';
                showNotification(currentLanguage === 'nl' ? 'WiFi Verbinding verbroken' : 
                                 currentLanguage === 'de' ? 'WLAN Getrennt' : 
                                 currentLanguage === 'es' ? 'WiFi Desconectado' : 
                                 currentLanguage === 'fr' ? 'WiFi Déconnecté' : 'WiFi Disconnected');
            }
        });
    }

    // Battery charging toggle
    let batteryCharging = false;
    let batteryPercent = 85;
    if (statusBatteryBtn) {
        statusBatteryBtn.addEventListener('click', () => {
            batteryCharging = !batteryCharging;
            if (batteryCharging) {
                batteryIcon.style.display = 'none';
                batteryChargingIcon.style.display = 'inline-block';
                batteryChargingIcon.style.color = '#f1c40f';
                
                const chargeMsg = {
                    en: 'Power connected. Charging...',
                    nl: 'Stroom verbonden. Opladen...',
                    de: 'Strom verbunden. Lädt...',
                    es: 'Energía conectada. Cargando...',
                    fr: 'Alimentation connectée. Charge en cours...'
                };
                batteryLevelText.textContent = currentLanguage === 'nl' ? 'Opladen' : 
                                               currentLanguage === 'de' ? 'Lädt' : 
                                               currentLanguage === 'es' ? 'Cargando' : 
                                               currentLanguage === 'fr' ? 'Charge' : 'Charging';
                showNotification(chargeMsg[currentLanguage]);
                
                this.batteryInterval = setInterval(() => {
                    if (batteryPercent < 100) {
                        batteryPercent++;
                        batteryLevelText.textContent = `${batteryPercent}%`;
                    }
                }, 5000);
            } else {
                clearInterval(this.batteryInterval);
                batteryChargingIcon.style.display = 'none';
                batteryIcon.style.display = 'inline-block';
                batteryLevelText.textContent = `${batteryPercent}%`;
                
                const disconnectMsg = {
                    en: 'Power disconnected.',
                    nl: 'Stroom losgekoppeld.',
                    de: 'Strom getrennt.',
                    es: 'Energía desconectada.',
                    fr: 'Alimentation déconnectée.'
                };
                showNotification(disconnectMsg[currentLanguage]);
            }
        });
    }

    // Toast Alert Creator
    function showNotification(message) {
        const toast = document.createElement('div');
        toast.className = 'toast-alert';
        toast.textContent = message;
        document.body.appendChild(toast);
        
        toast.style.position = 'fixed';
        toast.style.bottom = '80px';
        toast.style.left = '50%';
        toast.style.transform = 'translateX(-50%)';
        toast.style.backgroundColor = 'rgba(0, 0, 0, 0.85)';
        toast.style.color = '#fff';
        toast.style.padding = '8px 16px';
        toast.style.borderRadius = '20px';
        toast.style.fontSize = '0.78rem';
        toast.style.fontWeight = '500';
        toast.style.zIndex = '1000';
        toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.3)';
        toast.style.transition = 'opacity 0.3s ease';

        setTimeout(() => {
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 300);
        }, 2000);
    }

    // -------------------------------------------------------------
    // NAVIGATION ROUTER (LAUNCHER / OVERLAYS)
    // -------------------------------------------------------------
    const appIcons = document.querySelectorAll('.app-icon-wrapper');
    let activeAppId = null;

    appIcons.forEach(wrapper => {
        wrapper.addEventListener('click', (e) => {
            const appId = wrapper.getAttribute('data-app-id');
            if (appId) {
                // If it has data-app-id, it is a simulated app. Prevent default link redirect and open overlay.
                e.preventDefault();
                const label = wrapper.querySelector('.app-label').textContent;
                openApp(appId, label);
            }
            // Otherwise, it is a direct external anchor tag. Let the browser open the link natively.
        });
    });

    // Widget click listeners
    const weatherTrigger = document.getElementById('widget-weather-trigger');
    if (weatherTrigger) {
        weatherTrigger.addEventListener('click', () => {
            const labels = { en: "Weather", nl: "Weer", de: "Wetter", es: "Tiempo", fr: "Météo" };
            openApp('weather', labels[currentLanguage], '#');
        });
    }
    const clockTrigger = document.getElementById('widget-clock-trigger');
    if (clockTrigger) {
        clockTrigger.addEventListener('click', () => {
            const labels = { en: "Clock", nl: "Klok", de: "Uhr", es: "Reloj", fr: "Horloge" };
            openApp('clock', labels[currentLanguage], '#');
        });
    }

    function openApp(appId, label) {
        const targetSimApp = document.getElementById(`app-${appId}`);
        simApps.forEach(app => app.classList.remove('active-app'));
        
        if (targetSimApp) {
            targetSimApp.classList.add('active-app');
            appOverlayTitle.textContent = label;
            activeAppId = appId;
            
            // Initialization steps
            if (appId === 'notes') loadNotesList();
            if (appId === 'whatsapp') resetWhatsAppChat();
            if (appId === 'camera') initCameraViewfinder();
            
            // Open Overlay
            appOverlay.classList.add('active');
        }
    }

    function closeActiveApp() {
        appOverlay.classList.remove('active');
        setTimeout(() => {
            simApps.forEach(app => app.classList.remove('active-app'));
            activeAppId = null;
        }, 300);
    }

    // App header controls
    if (appCloseBtn) appCloseBtn.addEventListener('click', closeActiveApp);
    if (appHeaderHomeBtn) appHeaderHomeBtn.addEventListener('click', closeActiveApp);
    
    // Bottom physical navigation buttons
    if (navHome) navHome.addEventListener('click', closeActiveApp);
    
    if (navBack) {
        navBack.addEventListener('click', () => {
            if (activeAppId === 'whatsapp' && waChatWindow && waChatWindow.classList.contains('active')) {
                waChatWindow.classList.remove('active');
            } else if (activeAppId) {
                closeActiveApp();
            }
        });
    }

    if (navRecents) {
        navRecents.addEventListener('click', () => {
            phoneScreen.style.transform = 'scale(0.97)';
            setTimeout(() => {
                phoneScreen.style.transform = 'none';
            }, 150);
            
            const cleanupMsg = {
                en: 'Cleaned cached background apps.',
                nl: 'Gecachte achtergrond-apps opgeschoond.',
                de: 'Zwischengespeicherte Apps bereinigt.',
                es: 'Aplicaciones en segundo plano limpiadas.',
                fr: 'Applications en arrière-plan nettoyées.'
            };
            showNotification(cleanupMsg[currentLanguage]);
        });
    }

    // -------------------------------------------------------------
    // SIMULATED APP: DIALER (PHONE)
    // -------------------------------------------------------------
    const dialerDisplay = document.getElementById('dialer-display');
    const dialKeys = document.querySelectorAll('.dial-key');
    const dialBackspace = document.getElementById('dialer-backspace');
    const dialCallBtn = document.getElementById('dial-call-trigger');
    const callingOverlay = document.getElementById('calling-overlay');
    const callingNumber = document.getElementById('calling-number');
    const callingStatus = document.getElementById('calling-status');
    const dialHangupBtn = document.getElementById('dial-hangup-trigger');

    dialKeys.forEach(key => {
        key.addEventListener('click', () => {
            const val = key.getAttribute('data-val');
            if (dialerDisplay) dialerDisplay.value += val;
            playBeepTone(400 + (val === '*' || val === '#' ? 50 : parseInt(val || 0) * 40));
        });
    });

    if (dialBackspace) {
        dialBackspace.addEventListener('click', () => {
            if (dialerDisplay) dialerDisplay.value = dialerDisplay.value.slice(0, -1);
        });
    }

    if (dialCallBtn) {
        dialCallBtn.addEventListener('click', () => {
            const num = dialerDisplay.value.trim() || 'Bolokaiemi Ebi';
            callingNumber.textContent = num;
            
            // Localized calling status
            callingStatus.textContent = translations.calling_status[currentLanguage];
            callingOverlay.classList.add('active');
            
            setTimeout(() => {
                if (callingOverlay.classList.contains('active')) {
                    callingStatus.textContent = translations.calling_connected[currentLanguage] || 'Connected';
                }
            }, 1800);
        });
    }

    if (dialHangupBtn) {
        dialHangupBtn.addEventListener('click', () => {
            callingOverlay.classList.remove('active');
        });
    }

    // Audio tone synthesizer for phonepad
    let audioCtx = null;
    function playBeepTone(freq) {
        try {
            if (!audioCtx) {
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }
            const osc = audioCtx.createOscillator();
            const gain = audioCtx.createGain();
            
            osc.connect(gain);
            gain.connect(audioCtx.destination);
            
            osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
            gain.gain.setValueAtTime(0.08, audioCtx.currentTime);
            
            osc.start();
            gain.gain.exponentialRampToValueAtTime(0.00001, audioCtx.currentTime + 0.15);
            osc.stop(audioCtx.currentTime + 0.16);
        } catch (e) {
            // Audio blocked
        }
    }

    // -------------------------------------------------------------
    // SIMULATED APP: WHATSAPP
    // -------------------------------------------------------------
    const waContacts = document.querySelectorAll('.wa-contact');
    const waChatWindow = document.getElementById('wa-chat-window');
    const waChatName = document.getElementById('wa-chat-name');
    const waChatBack = document.getElementById('wa-chat-back');
    const waChatMessages = document.getElementById('wa-chat-messages');
    const waMessageInput = document.getElementById('wa-message-input');
    const waSendBtn = document.getElementById('wa-send-btn');
    
    let currentContactId = '';

    const waReplies = {
        mom: {
            en: [
                "Are you focusing on your coding work, Ebi?",
                "Make sure to rest your eyes. You have been staring at that laptop screen too long!",
                "I cooked rice and plantains, come eat later.",
                "Love you dear, let me know when you are done!"
            ],
            nl: [
                "Ben je geconcentreerd aan het programmeren, Ebi?",
                "Zorg ervoor dat je je ogen rust geeft. Je staart al te lang naar dat laptopscherm!",
                "Ik heb rijst en bakbananen gekookt, kom straks eten.",
                "Hou van je schat, laat me weten als je klaar bent!"
            ],
            de: [
                "Konzentrierst du dich auf deine Programmierarbeit, Ebi?",
                "Gönn deinen Augen etwas Ruhe. Du starrst schon viel zu lange auf den Laptop-Bildschirm!",
                "Ich habe Reis und Kochbananen gekocht, komm später essen.",
                "Ich liebe dich, mein Lieber. Sag Bescheid, wenn du fertig bist!"
            ],
            es: [
                "¿Te estás concentrando en tu trabajo de programación, Ebi?",
                "¡Asegúrate de descansar los ojos. Llevas demasiado tiempo mirando la pantalla del portátil!",
                "Cociné arroz y plátanos, ven a comer más tarde.",
                "¡Te quiero mucho, avísame cuando termines!"
            ],
            fr: [
                "Tu te concentres sur ton travail de code, Ebi ?",
                "Pense à reposer tes yeux. Tu as les yeux fixés sur cet écran d'ordinateur depuis trop longtemps !",
                "J'ai préparé du riz et des bananes plantains, viens manger plus tard.",
                "Je t'aime mon chéri, tiens-moi au courant quand tu auras fini !"
            ]
        },
        boss: {
            en: [
                "Ebi, that mobile interface looks incredibly clean.",
                "Are we ready to host it on GitHub Pages today?",
                "We have a meeting with the tech team soon. Keep up the good work.",
                "Please send the repository URL once you push the commit."
            ],
            nl: [
                "Ebi, die mobiele interface ziet er ongelooflijk strak uit.",
                "Zijn we klaar om het vandaag op GitHub Pages te hosten?",
                "We hebben binnenkort een vergadering met het techteam. Ga zo door.",
                "Stuur de repository-URL zodra je de commit hebt gepusht."
            ],
            de: [
                "Ebi, diese mobile Benutzeroberfläche sieht unglaublich sauber aus.",
                "Sind wir bereit, sie heute auf GitHub Pages zu hosten?",
                "Wir haben bald eine Besprechung mit dem Tech-Team. Mach weiter so.",
                "Bitte sende die Repository-URL, sobald du den Commit gepusht hast."
            ],
            es: [
                "Ebi, esa interfaz móvil se ve increíblemente limpia.",
                "¿Estamos listos para alojarla en GitHub Pages hoy?",
                "Tenemos una reunión con el equipo técnico pronto. Sigue así.",
                "Por favor, envía la URL del repositorio una vez que realices el push."
            ],
            fr: [
                "Ebi, cette interface mobile a l'air incroyablement propre.",
                "Sommes-nous prêts à l'héberger sur GitHub Pages aujourd'hui ?",
                "Nous avons une réunion avec l'équipe technique bientôt. Continuez votre bon travail.",
                "Veuillez envoyer l'URL du dépôt dès que vous aurez poussé le commit."
            ]
        },
        gemini: {
            en: [
                "Hello, I am the Gemini assistant inside WhatsApp. How can I help you?",
                "Your EbiUI custom ROM has beautiful visual design. The glassmorphism card structure is excellent.",
                "If you need help creating other mock interfaces, just ask me!",
                "Have you added the notes application persistence yet? (It works using localStorage!)"
            ],
            nl: [
                "Hallo, ik ben de Gemini-assistent binnen WhatsApp. Hoe kan ik je helpen?",
                "Je EbiUI custom ROM heeft een prachtig visueel ontwerp. De glassmorphism-kaartstructuur is uitstekend.",
                "Als je hulp nodig hebt bij het maken van andere mock-interfaces, vraag het me dan!",
                "Heb je de persistentie van de notities-app al toegevoegd? (Het werkt via localStorage!)"
            ],
            de: [
                "Hallo, ich bin der Gemini-Assistent in WhatsApp. Wie kann ich dir helfen?",
                "Deine EbiUI Custom-ROM hat ein wunderschönes visuelles Design. Die Glassmorphismus-Kartenstruktur ist hervorragend.",
                "Wenn du Hilfe bei der Erstellung anderer Mock-Interfaces brauchst, frag mich einfach!",
                "Hast du die Persistenz der Notizen-App schon hinzugefügt? (Sie funktioniert über localStorage!)"
            ],
            es: [
                "Hola, soy el asistente Gemini dentro de WhatsApp. ¿Cómo puedo ayudarte?",
                "Tu ROM personalizada EbiUI tiene un diseño visual hermoso. La estructura de tarjetas de glassmorphism es excelente.",
                "Si necesitas ayuda para crear otras interfaces simuladas, ¡pregúntame!",
                "¿Ya añadiste la persistencia de la aplicación de notas? (¡Funciona con localStorage!)"
            ],
            fr: [
                "Bonjour, je suis l'assistant Gemini sur WhatsApp. Comment puis-je vous aider ?",
                "Votre ROM personnalisée EbiUI a un magnifique design visuel. La structure de carte glassmorphism est excellente.",
                "Si vous avez besoin d'aide pour créer d'autres interfaces fictives, demandez-moi !",
                "Avez-vous déjà ajouté la persistance de l'application de notes ? (Elle fonctionne avec localStorage !)"
            ]
        }
    };

    let waReplyIndex = {};

    function resetWhatsAppChat() {
        if (waChatWindow) waChatWindow.classList.remove('active');
        currentContactId = '';
    }

    waContacts.forEach(contact => {
        contact.addEventListener('click', () => {
            const contactId = contact.getAttribute('data-contact');
            const contactName = contact.querySelector('h3').textContent;
            currentContactId = contactId;
            
            waChatName.textContent = contactName;
            waChatWindow.classList.add('active');
            
            waChatMessages.innerHTML = '';
            waReplyIndex[contactId] = 0;
            
            const lastMsgText = contact.querySelector('p').textContent;
            appendWAMessage(lastMsgText, 'in');
        });
    });

    if (waChatBack) {
        waChatBack.addEventListener('click', () => {
            waChatWindow.classList.remove('active');
            currentContactId = '';
        });
    }

    function appendWAMessage(text, direction) {
        const bubble = document.createElement('div');
        bubble.className = `wa-bubble ${direction}`;
        bubble.textContent = text;
        waChatMessages.appendChild(bubble);
        waChatMessages.scrollTop = waChatMessages.scrollHeight;
    }

    function sendWAMessage() {
        const text = waMessageInput.value.trim();
        if (!text || !currentContactId) return;
        
        appendWAMessage(text, 'out');
        waMessageInput.value = '';
        
        // Dynamic reply in selected language
        setTimeout(() => {
            const replies = waReplies[currentContactId][currentLanguage] || waReplies[currentContactId]['en'];
            const idx = waReplyIndex[currentContactId] || 0;
            const replyText = replies[idx % replies.length];
            
            appendWAMessage(replyText, 'in');
            waReplyIndex[currentContactId] = idx + 1;
        }, 1200);
    }

    if (waSendBtn) waSendBtn.addEventListener('click', sendWAMessage);
    if (waMessageInput) {
        waMessageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendWAMessage();
        });
    }

    // -------------------------------------------------------------
    // SIMULATED APP: NOTES
    // -------------------------------------------------------------
    const noteTitleInput = document.getElementById('note-title-input');
    const noteBodyInput = document.getElementById('note-body-input');
    const noteSaveBtn = document.getElementById('note-save-btn');
    const notesList = document.getElementById('notes-list');

    function loadNotesList() {
        notesList.innerHTML = '';
        const savedNotes = JSON.parse(localStorage.getItem('ebiui_notes') || '[]');
        
        if (savedNotes.length === 0) {
            const emptyMsgs = {
                en: 'No saved notes yet. Write one above!',
                nl: 'Nog geen opgeslagen notities. Schrijf er hierboven een!',
                de: 'Noch keine Notizen gespeichert. Schreibe oben eine!',
                es: 'No hay notas guardadas aún. ¡Escribe una arriba!',
                fr: 'Aucune note enregistrée. Écrivez-en une ci-dessus !'
            };
            notesList.innerHTML = `<p style="text-align:center; font-size:0.8rem; color:#888; margin-top:20px;">${emptyMsgs[currentLanguage]}</p>`;
            return;
        }

        savedNotes.forEach((note, index) => {
            const item = document.createElement('div');
            item.className = 'note-item';
            
            const info = document.createElement('div');
            info.className = 'note-info';
            info.innerHTML = `<h4>${note.title}</h4><p>${note.body}</p>`;
            
            const delBtn = document.createElement('button');
            delBtn.className = 'note-delete-btn';
            delBtn.innerHTML = '<i class="fa-solid fa-trash-can"></i>';
            delBtn.setAttribute('title', 'Delete');
            delBtn.addEventListener('click', () => deleteNote(index));
            
            item.appendChild(info);
            item.appendChild(delBtn);
            notesList.appendChild(item);
        });
    }

    function saveNote() {
        const defaultTitles = {
            en: 'Untitled Note',
            nl: 'Naamloze notitie',
            de: 'Unbenannte Notiz',
            es: 'Nota sin título',
            fr: 'Note sans titre'
        };
        const title = noteTitleInput.value.trim() || defaultTitles[currentLanguage];
        const body = noteBodyInput.value.trim();
        
        if (!body) {
            const emptyWarn = {
                en: 'Cannot save an empty note.',
                nl: 'Kan geen lege notitie opslaan.',
                de: 'Leere Notizen können nicht gespeichert werden.',
                es: 'No se puede guardar una nota vacía.',
                fr: 'Impossible de sauvegarder une note vide.'
            };
            showNotification(emptyWarn[currentLanguage]);
            return;
        }

        const savedNotes = JSON.parse(localStorage.getItem('ebiui_notes') || '[]');
        savedNotes.unshift({ title, body });
        localStorage.setItem('ebiui_notes', JSON.stringify(savedNotes));
        
        noteTitleInput.value = '';
        noteBodyInput.value = '';
        
        loadNotesList();
        
        const saveConf = {
            en: 'Note saved successfully!',
            nl: 'Notitie succesvol opgeslagen!',
            de: 'Notiz erfolgreich gespeichert!',
            es: '¡Nota guardada con éxito!',
            fr: 'Note sauvegardée avec succès !'
        };
        showNotification(saveConf[currentLanguage]);
    }

    function deleteNote(index) {
        const savedNotes = JSON.parse(localStorage.getItem('ebiui_notes') || '[]');
        savedNotes.splice(index, 1);
        localStorage.setItem('ebiui_notes', JSON.stringify(savedNotes));
        loadNotesList();
        
        const delConf = {
            en: 'Note deleted.',
            nl: 'Notitie verwijderd.',
            de: 'Notiz gelöscht.',
            es: 'Nota eliminada.',
            fr: 'Note supprimée.'
        };
        showNotification(delConf[currentLanguage]);
    }

    if (noteSaveBtn) noteSaveBtn.addEventListener('click', saveNote);

    // -------------------------------------------------------------
    // SIMULATED APP: CALCULATOR
    // -------------------------------------------------------------
    const calcResult = document.getElementById('calc-result');
    const calcHistory = document.getElementById('calc-history');
    const calcKeys = document.querySelectorAll('.calc-key');

    let calcInput = '';
    let calcEvalDone = false;

    calcKeys.forEach(key => {
        key.addEventListener('click', () => {
            const action = key.getAttribute('data-action');
            const val = key.getAttribute('data-val');
            
            if (action === 'clear') {
                calcInput = '';
                calcResult.textContent = '0';
                calcHistory.textContent = '';
                calcEvalDone = false;
            } else if (action === 'backspace') {
                if (!calcEvalDone && calcInput.length > 0) {
                    calcInput = calcInput.slice(0, -1);
                    calcResult.textContent = calcInput || '0';
                }
            } else if (action === '=') {
                if (calcInput) {
                    try {
                        const sanitized = calcInput.replace(/×/g, '*').replace(/÷/g, '/');
                        const output = safeMathEval(sanitized);
                        calcHistory.textContent = calcInput + ' =';
                        calcResult.textContent = output;
                        calcInput = String(output);
                        calcEvalDone = true;
                    } catch (e) {
                        calcResult.textContent = 'Error';
                        calcInput = '';
                    }
                }
            } else {
                if (calcEvalDone && val) {
                    calcInput = '';
                    calcEvalDone = false;
                } else {
                    calcEvalDone = false;
                }
                const keyChar = val || action;
                calcInput += keyChar;
                calcResult.textContent = calcInput;
            }
        });
    });

    function safeMathEval(str) {
        try {
            if (/[^0-9.+\-*/\s]/.test(str)) {
                return 'Error';
            }
            const result = new Function(`return (${str})`)();
            return Number(result.toFixed(6));
        } catch (e) {
            return 'Error';
        }
    }

    // -------------------------------------------------------------
    // SIMULATED APP: CAMERA
    // -------------------------------------------------------------
    const cameraFallback = document.getElementById('camera-stream-fallback');
    const shutterBtn = document.getElementById('camera-shutter-trigger');
    const filterBtns = document.querySelectorAll('.filter-btn');
    const cameraFilterNext = document.getElementById('camera-filter-next');
    const cameraGalleryBtn = document.getElementById('camera-gallery-trigger');

    const cameraStockPhotos = [
        'https://images.unsplash.com/photo-1472214222541-d510753a49f8?w=500&auto=format&fit=crop&q=60',
        'https://images.unsplash.com/photo-1501854140801-50d01698950b?w=500&auto=format&fit=crop&q=60',
        'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=500&auto=format&fit=crop&q=60',
        'https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=500&auto=format&fit=crop&q=60'
    ];
    let cameraPhotoIdx = 0;

    function initCameraViewfinder() {
        if (cameraFallback) {
            cameraFallback.style.backgroundImage = `url('${cameraStockPhotos[cameraPhotoIdx % cameraStockPhotos.length]}')`;
            cameraFallback.style.filter = 'none';
        }
        filterBtns.forEach(btn => {
            if (btn.getAttribute('data-filter') === 'none') {
                btn.classList.add('active');
            } else {
                btn.classList.remove('active');
            }
        });
    }

    if (shutterBtn) {
        shutterBtn.addEventListener('click', () => {
            const viewfinder = document.getElementById('camera-viewfinder');
            viewfinder.style.backgroundColor = '#ffffff';
            cameraFallback.style.opacity = '0.2';
            
            playBeepTone(800);
            
            setTimeout(() => {
                viewfinder.style.backgroundColor = '#111';
                cameraFallback.style.opacity = '1';
                
                const snapMsg = {
                    en: 'Photo captured to Google Photos!',
                    nl: 'Foto opgeslagen in Google Foto\'s!',
                    de: 'Foto in Google Fotos gespeichert!',
                    es: '¡Foto guardada en Google Fotos!',
                    fr: 'Photo enregistrée dans Google Photos !'
                };
                showNotification(snapMsg[currentLanguage]);
            }, 150);
        });
    }

    if (cameraGalleryBtn) {
        cameraGalleryBtn.addEventListener('click', () => {
            cameraPhotoIdx++;
            cameraFallback.style.backgroundImage = `url('${cameraStockPhotos[cameraPhotoIdx % cameraStockPhotos.length]}')`;
            
            const galleryMsg = {
                en: 'Loading gallery photo...',
                nl: 'Galerijfoto laden...',
                de: 'Galeriefoto laden...',
                es: 'Cargando foto de la galería...',
                fr: 'Chargement de la photo...'
            };
            showNotification(galleryMsg[currentLanguage]);
        });
    }

    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filterVal = btn.getAttribute('data-filter');
            if (filterVal === 'rose') {
                cameraFallback.style.filter = 'sepia(0.3) hue-rotate(330deg) saturate(1.4)';
            } else {
                cameraFallback.style.filter = filterVal;
            }
        });
    });

    if (cameraFilterNext) {
        cameraFilterNext.addEventListener('click', () => {
            let activeIdx = 0;
            filterBtns.forEach((btn, idx) => {
                if (btn.classList.contains('active')) activeIdx = idx;
            });
            const nextIdx = (activeIdx + 1) % filterBtns.length;
            filterBtns[nextIdx].click();
        });
    }

    // -------------------------------------------------------------
    // SIMULATED APP: GEMINI AI
    // -------------------------------------------------------------
    const geminiChatArea = document.getElementById('gemini-chat-area');
    const geminiMessageInput = document.getElementById('gemini-message-input');
    const geminiSendBtn = document.getElementById('gemini-send-btn');

    function sendGeminiMessage() {
        const text = geminiMessageInput.value.trim();
        if (!text) return;

        appendGeminiMessage(text, 'user');
        geminiMessageInput.value = '';

        setTimeout(() => {
            const responseText = processGeminiCommand(text.toLowerCase());
            appendGeminiMessage(responseText, 'ai');
        }, 800);
    }

    function appendGeminiMessage(text, direction) {
        const bubble = document.createElement('div');
        bubble.className = `gemini-bubble ${direction}`;
        bubble.innerHTML = text;
        geminiChatArea.appendChild(bubble);
        geminiChatArea.scrollTop = geminiChatArea.scrollHeight;
    }

    function processGeminiCommand(query) {
        // Localized Gemini Bot Commands
        if (query.includes('help')) {
            const helpMsg = {
                en: "Here are commands I support inside EbiUI:<br>- <strong>wallpaper [1-4]</strong>: Change wallpaper theme (e.g. 'wallpaper 3')<br>- <strong>time</strong>: Show the current system time<br>- <strong>joke</strong>: Tell you a joke<br>- <strong>dark</strong> or <strong>light</strong>: Toggle screen theme",
                nl: "Hier zijn commando's die ik ondersteun in EbiUI:<br>- <strong>wallpaper [1-4]</strong>: Verander achtergrondthema (bijv. 'wallpaper 3')<br>- <strong>time</strong>: Toon de huidige systeemtijd<br>- <strong>joke</strong>: Vertel een grap<br>- <strong>dark</strong> of <strong>light</strong>: Schakel schermthema om",
                de: "Hier sind Befehle, die ich in EbiUI unterstütze:<br>- <strong>wallpaper [1-4]</strong>: Ändere das Hintergrundthema (z. B. 'wallpaper 3')<br>- <strong>time</strong>: Zeige die aktuelle Uhrzeit<br>- <strong>joke</strong>: Erzähle einen Witz<br>- <strong>dark</strong> oder <strong>light</strong>: Bildschirmdesign umschalten",
                es: "Aquí están los comandos que admito en EbiUI:<br>- <strong>wallpaper [1-4]</strong>: Cambia el tema de fondo (p. ej., 'wallpaper 3')<br>- <strong>time</strong>: Muestra la hora actual<br>- <strong>joke</strong>: Te cuento un chiste<br>- <strong>dark</strong> o <strong>light</strong>: Cambia el tema visual",
                fr: "Voici les commandes prises en charge dans EbiUI :<br>- <strong>wallpaper [1-4]</strong> : Changer de fond d'écran (ex: 'wallpaper 3')<br>- <strong>time</strong> : Afficher l'heure système<br>- <strong>joke</strong> : Raconter une blague<br>- <strong>dark</strong> ou <strong>light</strong> : Changer le thème visuel"
            };
            return helpMsg[currentLanguage];
        }
        if (query.includes('wallpaper')) {
            const num = query.match(/[1-4]/);
            if (num) {
                const wpKey = 'grad' + num[0];
                changeWallpaper(wpKey);
                
                const wpConfirm = {
                    en: `Wallpaper changed to Theme Accent ${num[0]}! Open launcher to see.`,
                    nl: `Achtergrond gewijzigd naar Thema Accent ${num[0]}! Open het startscherm om te bekijken.`,
                    de: `Hintergrundbild in Designakzent ${num[0]} geändert! Öffne den Launcher, um es zu sehen.`,
                    es: `¡Fondo cambiado al acento de tema ${num[0]}! Abre el lanzador para ver.`,
                    fr: `Fond d'écran changé pour l'accent ${num[0]} ! Ouvrez le lanceur pour voir.`
                };
                return wpConfirm[currentLanguage];
            }
            return currentLanguage === 'nl' ? "Specificeer een achtergrondnummer, bijv. 'wallpaper 2'." :
                   currentLanguage === 'de' ? "Bitte gib eine Hintergrundnummer an, z. B. 'wallpaper 2'." :
                   currentLanguage === 'es' ? "Especifica un número de fondo, p. ej., 'wallpaper 2'." :
                   currentLanguage === 'fr' ? "Veuillez spécifier un numéro d'image, ex: 'wallpaper 2'." :
                   "Please specify a wallpaper number, e.g. 'wallpaper 2'.";
        }
        if (query.includes('time')) {
            const now = new Date();
            const timeMsg = {
                en: `The current emulator system time is ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`,
                nl: `De huidige systeemtijd van de emulator is ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`,
                de: `Die aktuelle Uhrzeit des Emulators ist ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`,
                es: `La hora actual del emulador es ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`,
                fr: `L'heure système de l'émulateur est ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`
            };
            return timeMsg[currentLanguage];
        }
        if (query.includes('joke')) {
            const jokes = {
                en: [
                    "Why do programmers wear glasses? Because they can't C#!",
                    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
                    "There are 10 kinds of people: those who understand binary, and those who don't."
                ],
                nl: [
                    "Waarom dragen programmeurs een bril? Omdat ze niet kunnen C#!",
                    "Hoeveel programmeurs zijn er nodig om een gloeilamp te vervangen? Geen, dat is een hardwareprobleem.",
                    "Er zijn 10 soorten mensen: zij die binair begrijpen, en zij die dat niet doen."
                ],
                de: [
                    "Warum tragen Programmierer Brillen? Weil sie nicht C# sehen!",
                    "Wie viele Programmierer braucht man, um eine Glühbirne zu wechseln? Keinen, das ist ein Hardware-Problem.",
                    "Es gibt 10 Arten von Menschen: Diejenigen, die Binärcode verstehen, und diejenigen, die es nicht tun."
                ],
                es: [
                    "¿Por qué los programadores usan gafas? ¡Porque no pueden C#!",
                    "¿Cuántos programadores se necesitan para cambiar una bombilla? Ninguno, ¡es un problema de hardware!",
                    "Hay 10 tipos de personas: los que entienden binario y los que no."
                ],
                fr: [
                    "Pourquoi les développeurs portent-ils des lunettes ? Parce qu'ils ne peuvent pas C# !",
                    "Combien de développeurs faut-il pour changer une ampoule ? Aucun, c'est un problème matériel.",
                    "Il y a 10 types de personnes : celles qui comprennent le binaire, et les autres."
                ]
            };
            const activeJokes = jokes[currentLanguage] || jokes['en'];
            return activeJokes[Math.floor(Math.random() * activeJokes.length)];
        }
        if (query.includes('dark')) {
            document.body.classList.remove('light-theme');
            const toggle = document.getElementById('settings-darkmode-toggle');
            if (toggle) toggle.checked = true;
            return currentLanguage === 'nl' ? "Thema gewijzigd naar Donkere Modus." :
                   currentLanguage === 'de' ? "Design auf Dunkelmodus umgestellt." :
                   currentLanguage === 'es' ? "Tema cambiado a Modo Oscuro." :
                   currentLanguage === 'fr' ? "Thème basculé en Mode Sombre." :
                   "Theme switched to Dark Mode.";
        }
        if (query.includes('light')) {
            document.body.classList.add('light-theme');
            const toggle = document.getElementById('settings-darkmode-toggle');
            if (toggle) toggle.checked = false;
            return currentLanguage === 'nl' ? "Thema gewijzigd naar Lichte Modus." :
                   currentLanguage === 'de' ? "Design auf Hellmodus umgestellt." :
                   currentLanguage === 'es' ? "Tema cambiado a Modo Claro." :
                   currentLanguage === 'fr' ? "Thème basculé en Mode Clair." :
                   "Theme switched to Light Mode.";
        }

        const fallbackReply = {
            en: "I received your message! Since I'm running locally on your EbiUI, you can type <strong>help</strong> to see interactive control commands.",
            nl: "Ik heb je bericht ontvangen! Omdat ik lokaal op je EbiUI draai, kun je <strong>help</strong> typen om interactieve commando's te zien.",
            de: "Ich habe deine Nachricht erhalten! Da ich lokal auf deiner EbiUI laufe, kannst du <strong>help</strong> eingeben, um interaktive Steuerungsbefehle anzuzeigen.",
            es: "¡Recibí tu mensaje! Como me ejecuto localmente en tu EbiUI, puedes escribir <strong>help</strong> para ver los comandos interactivos.",
            fr: "J'ai bien reçu votre message ! Comme je tourne localement sur EbiUI, vous pouvez taper <strong>help</strong> pour voir les commandes disponibles."
        };
        return fallbackReply[currentLanguage];
    }

    if (geminiSendBtn) geminiSendBtn.addEventListener('click', sendGeminiMessage);
    if (geminiMessageInput) {
        geminiMessageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') sendGeminiMessage();
        });
    }

    // -------------------------------------------------------------
    // SIMULATED APP: SETTINGS & GENERAL CUSTOMIZATION
    // -------------------------------------------------------------
    const wallpaperThumbs = document.querySelectorAll('.wallpaper-thumb');
    const darkModeToggle = document.getElementById('settings-darkmode-toggle');
    const colorDots = document.querySelectorAll('.color-dot');

    colorDots.forEach(dot => {
        dot.addEventListener('click', () => {
            colorDots.forEach(d => d.classList.remove('active'));
            dot.classList.add('active');
            
            const hue = dot.getAttribute('data-hue');
            document.documentElement.style.setProperty('--theme-hue', hue);
            
            const accentConf = {
                en: 'Accent Theme primary shifted successfully!',
                nl: 'Primaire accentkleur succesvol aangepast!',
                de: 'Designakzentfarbe erfolgreich geändert!',
                es: '¡Color de acento del tema cambiado con éxito!',
                fr: 'Couleur d\'accent modifiée avec succès !'
            };
            showNotification(accentConf[currentLanguage]);
        });
    });

    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            if (darkModeToggle.checked) {
                document.body.classList.remove('light-theme');
                showNotification(currentLanguage === 'nl' ? 'Donkere modus ingeschakeld.' : 
                                 currentLanguage === 'de' ? 'Dunkelmodus aktiviert.' : 
                                 currentLanguage === 'es' ? 'Modo oscuro activado.' : 
                                 currentLanguage === 'fr' ? 'Mode sombre activé.' : 'Dark theme enabled.');
            } else {
                document.body.classList.add('light-theme');
                showNotification(currentLanguage === 'nl' ? 'Lichte modus ingeschakeld.' : 
                                 currentLanguage === 'de' ? 'Hellmodus aktiviert.' : 
                                 currentLanguage === 'es' ? 'Modo claro activado.' : 
                                 currentLanguage === 'fr' ? 'Mode clair activé.' : 'Light theme enabled.');
            }
        });
    }

    function changeWallpaper(wpKey) {
        if (wpKey === 'grad1') phoneWallpaper.style.background = 'var(--wp-grad1)';
        if (wpKey === 'grad2') phoneWallpaper.style.background = 'var(--wp-grad2)';
        if (wpKey === 'grad3') phoneWallpaper.style.background = 'var(--wp-grad3)';
        if (wpKey === 'grad4') phoneWallpaper.style.background = 'var(--wp-grad4)';

        wallpaperThumbs.forEach(thumb => {
            if (thumb.getAttribute('data-wp') === wpKey) {
                thumb.classList.add('active');
            } else {
                thumb.classList.remove('active');
            }
        });
    }

    wallpaperThumbs.forEach(thumb => {
        thumb.addEventListener('click', () => {
            const wpKey = thumb.getAttribute('data-wp');
            changeWallpaper(wpKey);
            
            const wallConf = {
                en: 'Wallpaper applied.',
                nl: 'Achtergrond toegepast.',
                de: 'Hintergrundbild angewendet.',
                es: 'Fondo de pantalla aplicado.',
                fr: 'Fond d\'écran appliqué.'
            };
            showNotification(wallConf[currentLanguage]);
        });
    });

    // Default setups
    const defaultDot = document.querySelector('.color-dot.default');
    if (defaultDot) defaultDot.classList.add('active');

    const defaultWpThumb = document.querySelector('.wallpaper-thumb[data-wp="grad2"]');
    if (defaultWpThumb) defaultWpThumb.classList.add('active');

    // -------------------------------------------------------------
    // INTERACTIVE GOOGLE SEARCH WIDGET
    // -------------------------------------------------------------
    const launcherSearchInput = document.getElementById('launcher-search-input');
    if (launcherSearchInput) {
        launcherSearchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                const query = launcherSearchInput.value.trim();
                if (query) {
                    openApp('chrome', 'Chrome', `https://www.google.com/search?q=${encodeURIComponent(query)}`);
                    launcherSearchInput.value = '';
                }
            }
        });
    }

    // -------------------------------------------------------------
    // HUB NAVIGATION & AUTH/COMMENT DASHBOARD LOGIC
    // -------------------------------------------------------------
    const navHomeTab = document.getElementById('nav-home-tab');
    const navDashboardTab = document.getElementById('nav-dashboard-tab');
    const tabViewHome = document.getElementById('tab-view-home');
    const tabViewDashboard = document.getElementById('tab-view-dashboard');

    const loginForm = document.getElementById('login-form');
    const registerForm = document.getElementById('register-form');
    const profileUsernameText = document.getElementById('profile-username-text');
    const authLogoutBtn = document.getElementById('auth-logout-btn');
    const authSectionTitle = document.getElementById('auth-section-title');

    const commentsListContainer = document.getElementById('comments-list-container');
    const commentInputWrapper = document.getElementById('comment-input-wrapper');
    const commentLockedPrompt = document.getElementById('comment-locked-prompt');
    const commentTextInput = document.getElementById('comment-text-input');
    const commentSubmitBtn = document.getElementById('comment-submit-btn');

    let currentUser = null;

    // View toggling tabs (especially on mobile layouts)
    function switchTab(targetTab) {
        if (targetTab === 'home') {
            if (navHomeTab) navHomeTab.classList.add('active');
            if (navDashboardTab) navDashboardTab.classList.remove('active');
            if (tabViewHome) tabViewHome.classList.add('active-tab-view');
            if (tabViewDashboard) tabViewDashboard.classList.remove('active-tab-view');
        } else if (targetTab === 'dashboard') {
            if (navDashboardTab) navDashboardTab.classList.add('active');
            if (navHomeTab) navHomeTab.classList.remove('active');
            if (tabViewDashboard) tabViewDashboard.classList.add('active-tab-view');
            if (tabViewHome) tabViewHome.classList.remove('active-tab-view');
            loadComments();
        }
    }

    if (navHomeTab) navHomeTab.addEventListener('click', () => switchTab('home'));
    if (navDashboardTab) navDashboardTab.addEventListener('click', () => switchTab('dashboard'));

    // Authenticate Form Views Toggle
    const linkToRegister = document.getElementById('link-to-register');
    const linkToLogin = document.getElementById('link-to-login');

    if (linkToRegister) {
        linkToRegister.addEventListener('click', (e) => {
            e.preventDefault();
            if (loginForm) loginForm.style.display = 'none';
            if (registerForm) registerForm.style.display = 'flex';
            if (authSectionTitle) authSectionTitle.textContent = 'Create an Account to Post Feedback';
        });
    }

    if (linkToLogin) {
        linkToLogin.addEventListener('click', (e) => {
            e.preventDefault();
            if (registerForm) registerForm.style.display = 'none';
            if (loginForm) loginForm.style.display = 'flex';
            if (authSectionTitle) authSectionTitle.textContent = 'Sign In to Post Feedback';
        });
    }

    // Helper: Escape user input to prevent HTML injection XSS
    function escapeHtml(text) {
        const map = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#039;'
        };
        return text.replace(/[&<>"']/g, function(m) { return map[m]; });
    }

    // Check Active Auth Session
    async function checkAuthStatus() {
        try {
            const response = await fetch('/api/user');
            const data = await response.json();
            if (data.user) {
                currentUser = data.user.username;
                showUserProfile(currentUser);
            } else {
                currentUser = null;
                showAuthForms();
            }
        } catch (error) {
            console.error('Error checking authentication status:', error);
            currentUser = null;
            showAuthForms();
        }
    }

    function showUserProfile(username) {
        if (profileUsernameText) profileUsernameText.textContent = username;

        // Unlock comment fields
        if (commentInputWrapper) commentInputWrapper.style.display = 'block';
        if (commentLockedPrompt) commentLockedPrompt.style.display = 'none';
    }

    function showAuthForms() {
        // Reset forms to Login view by default
        if (loginForm) loginForm.style.display = 'flex';
        if (registerForm) registerForm.style.display = 'none';
        if (authSectionTitle) authSectionTitle.textContent = 'Sign In to Post Feedback';

        // Lock comment fields
        if (commentInputWrapper) commentInputWrapper.style.display = 'none';
        if (commentLockedPrompt) commentLockedPrompt.style.display = 'block';
    }

    // Fetch and Render Comment Feed
    async function loadComments() {
        if (!commentsListContainer) return;
        
        try {
            const response = await fetch('/api/comments');
            const data = await response.json();
            const comments = data.comments || [];
            
            if (comments.length === 0) {
                commentsListContainer.innerHTML = `
                    <div class="comment-empty-state">
                        <i class="fa-regular fa-comment-dots" style="font-size: 1.5rem; display: block; margin-bottom: 8px; opacity: 0.5;"></i>
                        No feedback posted yet. Be the first!
                    </div>
                `;
                return;
            }
            
            commentsListContainer.innerHTML = '';
            comments.forEach(comment => {
                const commentEl = document.createElement('div');
                commentEl.className = 'comment-item';
                
                // Show delete button only if logged in user is the author
                const isOwner = currentUser && currentUser === comment.username;
                const deleteButton = isOwner 
                    ? `<button class="btn-delete" data-id="${comment.id}"><i class="fa-solid fa-trash-can"></i> Delete</button>`
                    : '';
                
                commentEl.innerHTML = `
                    <div class="comment-header">
                        <span class="comment-user"><i class="fa-regular fa-user"></i> ${escapeHtml(comment.username)}</span>
                        <span class="comment-time">${comment.created_at}</span>
                    </div>
                    <div class="comment-text">${escapeHtml(comment.text)}</div>
                    ${deleteButton ? `<div class="comment-actions">${deleteButton}</div>` : ''}
                `;
                
                commentsListContainer.appendChild(commentEl);
            });
            
            // Bind comments delete actions
            const deleteButtons = commentsListContainer.querySelectorAll('.btn-delete');
            deleteButtons.forEach(btn => {
                btn.addEventListener('click', async () => {
                    const commentId = btn.getAttribute('data-id');
                    if (confirm('Are you sure you want to delete this comment?')) {
                        await deleteComment(commentId);
                    }
                });
            });
            
        } catch (error) {
            console.error('Error fetching comments:', error);
            commentsListContainer.innerHTML = `
                <div class="comments-loading" style="color: #ff5555;">
                    <i class="fa-solid fa-triangle-exclamation"></i> Error loading comments.
                </div>
            `;
        }
    }

    // Register Form Handler
    if (registerForm) {
        registerForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const usernameInput = document.getElementById('register-username');
            const passwordInput = document.getElementById('register-password');
            const username = usernameInput ? usernameInput.value.trim() : '';
            const password = passwordInput ? passwordInput.value.trim() : '';

            if (!username || !password) return;

            try {
                const response = await fetch('/api/register', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    currentUser = data.user.username;
                    showUserProfile(currentUser);
                    showNotification('Account registered and logged in!');
                    if (usernameInput) usernameInput.value = '';
                    if (passwordInput) passwordInput.value = '';
                    loadComments();
                } else {
                    showNotification(data.error || 'Registration failed.');
                }
            } catch (error) {
                console.error('Registration error:', error);
                showNotification('Connection error. Please try again.');
            }
        });
    }

    // Login Form Handler
    if (loginForm) {
        loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const usernameInput = document.getElementById('login-username');
            const passwordInput = document.getElementById('login-password');
            const username = usernameInput ? usernameInput.value.trim() : '';
            const password = passwordInput ? passwordInput.value.trim() : '';

            if (!username || !password) return;

            try {
                const response = await fetch('/api/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });

                const data = await response.json();

                if (response.ok) {
                    currentUser = data.user.username;
                    showUserProfile(currentUser);
                    showNotification('Signed in successfully!');
                    if (usernameInput) usernameInput.value = '';
                    if (passwordInput) passwordInput.value = '';
                    loadComments();
                } else {
                    showNotification(data.error || 'Invalid username or password.');
                }
            } catch (error) {
                console.error('Login error:', error);
                showNotification('Connection error. Please try again.');
            }
        });
    }

    // Logout Action
    if (authLogoutBtn) {
        authLogoutBtn.addEventListener('click', async () => {
            try {
                const response = await fetch('/api/logout', { method: 'POST' });
                if (response.ok) {
                    currentUser = null;
                    showAuthForms();
                    showNotification('Logged out successfully.');
                    loadComments();
                } else {
                    showNotification('Logout failed.');
                }
            } catch (error) {
                console.error('Logout error:', error);
                showNotification('Connection error.');
            }
        });
    }

    // Submit Comment Handler
    if (commentSubmitBtn && commentTextInput) {
        commentSubmitBtn.addEventListener('click', async () => {
            const text = commentTextInput.value.trim();
            if (!text) {
                showNotification('Feedback comment cannot be empty.');
                return;
            }

            try {
                const response = await fetch('/api/comments', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ text })
                });

                const data = await response.json();

                if (response.ok) {
                    commentTextInput.value = '';
                    showNotification('Feedback posted!');
                    loadComments();
                } else {
                    showNotification(data.error || 'Failed to post feedback.');
                }
            } catch (error) {
                console.error('Post comment error:', error);
                showNotification('Connection error.');
            }
        });
    }

    // Delete Comment Action
    async function deleteComment(id) {
        try {
            const response = await fetch(`/api/comments/${id}`, {
                method: 'DELETE'
            });

            const data = await response.json();

            if (response.ok) {
                showNotification('Feedback deleted.');
                loadComments();
            } else {
                showNotification(data.error || 'Failed to delete comment.');
            }
        } catch (error) {
            console.error('Delete comment error:', error);
            showNotification('Connection error.');
        }
    }

    // Trigger Initial Checks
    checkAuthStatus();
    loadComments();
});
