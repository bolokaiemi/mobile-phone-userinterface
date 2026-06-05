/**
 * Android 14 EbiUI - Interactive Emulator Application Logic
 * Created by: Bolokaiemi Ebi
 */

document.addEventListener('DOMContentLoaded', () => {
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

    // Navigation Buttons
    const navBack = document.getElementById('nav-back');
    const navHome = document.getElementById('nav-home');
    const navRecents = document.getElementById('nav-recents');
    const phoneScreen = document.getElementById('phone-screen');

    // App Overlay System
    const appOverlay = document.getElementById('app-overlay');
    const appOverlayTitle = document.getElementById('app-overlay-title');
    const appCloseBtn = document.getElementById('app-close-btn');
    const simApps = document.querySelectorAll('.sim-app');

    // Wallpaper and Accent
    const phoneWallpaper = document.getElementById('phone-wallpaper');

    // -------------------------------------------------------------
    // DYNAMIC TIME & DATE
    // -------------------------------------------------------------
    function updateClock() {
        const now = new Date();
        let hours = now.getHours();
        let minutes = now.getMinutes();
        
        // Pad single digits
        hours = hours < 10 ? '0' + hours : hours;
        minutes = minutes < 10 ? '0' + minutes : minutes;
        
        const timeString = `${hours}:${minutes}`;
        if (statusTime) statusTime.textContent = timeString;
        if (widgetTime) widgetTime.textContent = timeString;

        // Update date on widget
        const options = { weekday: 'long', month: 'long', day: 'numeric' };
        const dateString = now.toLocaleDateString('en-US', options);
        if (widgetDate) widgetDate.textContent = dateString;
    }
    
    // Run clock updates
    updateClock();
    setInterval(updateClock, 1000);

    // -------------------------------------------------------------
    // STATUS BAR TOGGLES
    // -------------------------------------------------------------
    // Wifi Toggle
    let wifiActive = true;
    if (statusWifi) {
        statusWifi.addEventListener('click', () => {
            wifiActive = !wifiActive;
            if (wifiActive) {
                statusWifi.className = 'fa-solid fa-wifi';
                statusWifi.style.color = '';
                statusWifi.title = 'WiFi: Connected';
                showNotification('WiFi Connected');
            } else {
                statusWifi.className = 'fa-solid fa-wifi';
                statusWifi.style.color = 'rgba(255,255,255,0.3)';
                statusWifi.title = 'WiFi: Disconnected';
                showNotification('WiFi Disconnected');
            }
        });
    }

    // Battery / Charging Toggle
    let batteryCharging = false;
    let batteryPercent = 85;
    if (statusBatteryBtn) {
        statusBatteryBtn.addEventListener('click', () => {
            batteryCharging = !batteryCharging;
            if (batteryCharging) {
                batteryIcon.style.display = 'none';
                batteryChargingIcon.style.display = 'inline-block';
                batteryChargingIcon.style.color = '#f1c40f';
                batteryLevelText.textContent = 'Charging';
                showNotification('Power source connected. Charging...');
                
                // Simulate battery rising
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
                showNotification('Power disconnected.');
            }
        });
    }

    // Toast Notification Maker
    function showNotification(message) {
        const toast = document.createElement('div');
        toast.className = 'toast-alert';
        toast.textContent = message;
        document.body.appendChild(toast);
        
        // Simple Toast Styles injection if not already in stylesheet
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
        wrapper.addEventListener('click', () => {
            const appId = wrapper.getAttribute('data-app-id');
            const appLink = wrapper.getAttribute('data-link');
            const label = wrapper.querySelector('.app-label').textContent;
            const imgSrc = wrapper.querySelector('.app-icon').getAttribute('src');
            
            openApp(appId, label, appLink, imgSrc);
        });
    });

    // Widget Triggers
    const weatherTrigger = document.getElementById('widget-weather-trigger');
    if (weatherTrigger) {
        weatherTrigger.addEventListener('click', () => {
            openApp('weather', 'Weather', '#');
        });
    }
    const clockTrigger = document.getElementById('widget-clock-trigger');
    if (clockTrigger) {
        clockTrigger.addEventListener('click', () => {
            openApp('clock', 'Clock', '#');
        });
    }

    function openApp(appId, label, externalLink = '#', imgSrc = '') {
        // Find if we have a simulated app template
        const targetSimApp = document.getElementById(`app-${appId}`);
        
        // Hide all active apps first
        simApps.forEach(app => app.classList.remove('active-app'));
        
        if (targetSimApp) {
            // Activate target simulated app template
            targetSimApp.classList.add('active-app');
            appOverlayTitle.textContent = label;
            activeAppId = appId;
            
            // Special initialization per app
            if (appId === 'notes') loadNotesList();
            if (appId === 'whatsapp') resetWhatsAppChat();
            if (appId === 'camera') initCameraViewfinder();
        } else {
            // Use Fallback generic app screen with direct play store link
            const genericApp = document.getElementById('app-generic');
            genericApp.classList.add('active-app');
            activeAppId = 'generic';
            
            document.getElementById('generic-app-title').textContent = label;
            document.getElementById('generic-app-name-bold').textContent = label;
            document.getElementById('generic-app-img').setAttribute('src', imgSrc || 'https://cdn-icons-png.flaticon.com/512/93/93158.png');
            
            const storeBtn = document.getElementById('generic-app-playstore-link');
            storeBtn.setAttribute('href', externalLink);
            storeBtn.setAttribute('title', `Open Store for ${label}`);
        }

        // Slide up the overlay screen
        appOverlay.classList.add('active');
    }

    function closeActiveApp() {
        appOverlay.classList.remove('active');
        setTimeout(() => {
            simApps.forEach(app => app.classList.remove('active-app'));
            activeAppId = null;
        }, 300);
    }

    // Event binding for closing app
    if (appCloseBtn) appCloseBtn.addEventListener('click', closeActiveApp);
    
    // Bottom physical phone buttons
    if (navHome) navHome.addEventListener('click', closeActiveApp);
    
    if (navBack) {
        navBack.addEventListener('click', () => {
            if (activeAppId === 'whatsapp' && waChatWindow && waChatWindow.classList.contains('active')) {
                // If in chat conversation, go back to chat list
                waChatWindow.classList.remove('active');
            } else if (activeAppId) {
                closeActiveApp();
            }
        });
    }

    if (navRecents) {
        navRecents.addEventListener('click', () => {
            // Trigger little feedback animation on screen
            phoneScreen.style.transform = 'scale(0.97)';
            setTimeout(() => {
                phoneScreen.style.transform = 'none';
            }, 150);
            showNotification('Cleaned cached background apps.');
        });
    }

    // Generic fallback button return
    const genericBackBtn = document.getElementById('generic-back-btn');
    if (genericBackBtn) {
        genericBackBtn.addEventListener('click', closeActiveApp);
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
            
            // Audio beep synthesis
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
            const num = dialerDisplay.value.trim() || 'Bolokaiemi Ebi (Dev)';
            callingNumber.textContent = num;
            callingStatus.textContent = 'Calling...';
            callingOverlay.classList.add('active');
            
            // Simulate call connection after 1.5 seconds
            setTimeout(() => {
                if (callingOverlay.classList.contains('active')) {
                    callingStatus.textContent = 'Connected (Simulated Call)';
                }
            }, 1800);
        });
    }

    if (dialHangupBtn) {
        dialHangupBtn.addEventListener('click', () => {
            callingOverlay.classList.remove('active');
        });
    }

    // Web Audio synthesizer for phone pad tones
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
            // Audio Context blocked or unsupported
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
        mom: [
            "Are you focusing on your coding work, Ebi?",
            "Make sure to rest your eyes. You have been staring at that laptop screen too long!",
            "I cooked rice and plantains, come eat later.",
            "Love you dear, let me know when you are done!"
        ],
        boss: [
            "Ebi, that mobile interface looks incredibly clean.",
            "Are we ready to host it on GitHub Pages today?",
            "We have a meeting with the tech team soon. Keep up the good work.",
            "Please send the repository URL once you push the commit."
        ],
        gemini: [
            "Hello, I am the Gemini assistant inside WhatsApp. How can I help you?",
            "Your EbiUI custom ROM has beautiful visual design. The glassmorphism card structure is excellent.",
            "If you need help creating other mock interfaces, just ask me!",
            "Have you added the notes application persistence yet? (It works using localStorage!)"
        ]
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
            
            // Clear past chat screen and load initial history
            waChatMessages.innerHTML = '';
            waReplyIndex[contactId] = 0;
            
            // Add a couple of initial messages
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
        
        // Trigger automated bot reply
        setTimeout(() => {
            const replies = waReplies[currentContactId];
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
            notesList.innerHTML = '<p style="text-align:center; font-size:0.8rem; color:#888; margin-top:20px;">No saved notes yet. Write one above!</p>';
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
            delBtn.setAttribute('title', 'Delete Note');
            delBtn.addEventListener('click', () => deleteNote(index));
            
            item.appendChild(info);
            item.appendChild(delBtn);
            notesList.appendChild(item);
        });
    }

    function saveNote() {
        const title = noteTitleInput.value.trim() || 'Untitled Note';
        const body = noteBodyInput.value.trim();
        
        if (!body) {
            showNotification('Cannot save an empty note.');
            return;
        }

        const savedNotes = JSON.parse(localStorage.getItem('ebiui_notes') || '[]');
        savedNotes.unshift({ title, body });
        localStorage.setItem('ebiui_notes', JSON.stringify(savedNotes));
        
        noteTitleInput.value = '';
        noteBodyInput.value = '';
        
        loadNotesList();
        showNotification('Note saved successfully!');
    }

    function deleteNote(index) {
        const savedNotes = JSON.parse(localStorage.getItem('ebiui_notes') || '[]');
        savedNotes.splice(index, 1);
        localStorage.setItem('ebiui_notes', JSON.stringify(savedNotes));
        loadNotesList();
        showNotification('Note deleted.');
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
                        // Safe evaluation
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
                // Number or basic operator
                if (calcEvalDone && val) {
                    // Start fresh if user presses number after evaluation
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

    // Extremely simple safe parser instead of using evil eval()
    function safeMathEval(str) {
        try {
            // Validate token format strictly (only digits, dots, operators)
            if (/[^0-9.+\-*/\s]/.test(str)) {
                return 'Error';
            }
            // Use Function constructor in isolated scope (still safer than raw eval, client-side only)
            const result = new Function(`return (${str})`)();
            return Number(result.toFixed(6)); // avoids floats like 0.1 + 0.2 = 0.30000000000000004
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

    // Capture Photo flash simulation
    if (shutterBtn) {
        shutterBtn.addEventListener('click', () => {
            const viewfinder = document.getElementById('camera-viewfinder');
            viewfinder.style.backgroundColor = '#ffffff';
            cameraFallback.style.opacity = '0.2';
            
            // Audio click sound
            playBeepTone(800);
            
            setTimeout(() => {
                viewfinder.style.backgroundColor = '#111';
                cameraFallback.style.opacity = '1';
                showNotification('Photo captured to Google Fotos!');
            }, 150);
        });
    }

    // Swap viewfinder mock background photo
    if (cameraGalleryBtn) {
        cameraGalleryBtn.addEventListener('click', () => {
            cameraPhotoIdx++;
            cameraFallback.style.backgroundImage = `url('${cameraStockPhotos[cameraPhotoIdx % cameraStockPhotos.length]}')`;
            showNotification('Loading gallery photo...');
        });
    }

    // Apply filters
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            
            const filterVal = btn.getAttribute('data-filter');
            cameraFallback.style.filter = filterVal;
        });
    });

    if (cameraFilterNext) {
        cameraFilterNext.addEventListener('click', () => {
            // Find active filter
            let activeIdx = 0;
            filterBtns.forEach((btn, idx) => {
                if (btn.classList.contains('active')) activeIdx = idx;
            });
            
            // Cycle
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

        // Typing response animation placeholder
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
        if (query.includes('help')) {
            return "Here are commands I support inside EbiUI:<br>- <strong>wallpaper [1-4]</strong>: Change wallpaper theme (e.g. 'wallpaper 3')<br>- <strong>time</strong>: Show the current system time<br>- <strong>joke</strong>: Tell you a joke<br>- <strong>dark</strong> or <strong>light</strong>: Toggle screen theme";
        }
        if (query.includes('wallpaper')) {
            const num = query.match(/[1-4]/);
            if (num) {
                const wpKey = 'grad' + num[0];
                changeWallpaper(wpKey);
                return `Wallpaper changed to Theme Accent ${num[0]}! Open launcher to see.`;
            }
            return "Please specify a wallpaper number, e.g. 'wallpaper 2'.";
        }
        if (query.includes('time')) {
            const now = new Date();
            return `The current emulator system time is ${now.getHours()}:${now.getMinutes() < 10 ? '0' + now.getMinutes() : now.getMinutes()}.`;
        }
        if (query.includes('joke')) {
            const jokes = [
                "Why do programmers wear glasses? Because they can't C#!",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
                "There are 10 kinds of people: those who understand binary, and those who don't.",
                "Why was the JavaScript developer sad? Because he didn't know how to 'context' himself!"
            ];
            return jokes[Math.floor(Math.random() * jokes.length)];
        }
        if (query.includes('dark')) {
            document.body.classList.remove('light-theme');
            document.getElementById('settings-darkmode-toggle').checked = true;
            return "Theme switched to Dark Mode.";
        }
        if (query.includes('light')) {
            document.body.classList.add('light-theme');
            document.getElementById('settings-darkmode-toggle').checked = false;
            return "Theme switched to Light Mode.";
        }
        return "I received your message! Since I'm running locally on your EbiUI, you can type <strong>help</strong> to see interactive control commands.";
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

    // Accent Hue Changer
    colorDots.forEach(dot => {
        dot.addEventListener('click', () => {
            colorDots.forEach(d => d.classList.remove('active'));
            dot.classList.add('active');
            
            const hue = dot.getAttribute('data-hue');
            document.documentElement.style.setProperty('--theme-hue', hue);
            showNotification(`Accent Theme primary shifted successfully!`);
        });
    });

    // Dark Mode Toggle Switcher
    if (darkModeToggle) {
        darkModeToggle.addEventListener('change', () => {
            if (darkModeToggle.checked) {
                // Checked means dark mode is active (remove light-theme class)
                document.body.classList.remove('light-theme');
                showNotification('Dark theme enabled.');
            } else {
                document.body.classList.add('light-theme');
                showNotification('Light theme enabled.');
            }
        });
    }

    // Wallpaper changer helper
    function changeWallpaper(wpKey) {
        // Toggle wallpaper styles
        if (wpKey === 'grad1') phoneWallpaper.style.background = 'var(--wp-grad1)';
        if (wpKey === 'grad2') phoneWallpaper.style.background = 'var(--wp-grad2)';
        if (wpKey === 'grad3') phoneWallpaper.style.background = 'var(--wp-grad3)';
        if (wpKey === 'grad4') phoneWallpaper.style.background = 'var(--wp-grad4)';

        // Update settings thumbnail active border
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
            showNotification('Wallpaper applied.');
        });
    });

    // Set default color dot active on start
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
                    // Open Google search inside simulated Chrome
                    openApp('chrome', 'Chrome', `https://www.google.com/search?q=${encodeURIComponent(query)}`);
                    launcherSearchInput.value = '';
                }
            }
        });
    }
});
