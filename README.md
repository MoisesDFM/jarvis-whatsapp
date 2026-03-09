🦾 JARVIS - Asistente WhatsApp 24/7
Jarvis funciona en la nube, sin necesidad de tener la PC encendida.
Responde automáticamente tus mensajes de WhatsApp usando IA.

📁 Archivos del proyecto
jarvis-whatsapp/
├── app.py            ← Servidor principal de Jarvis
├── requirements.txt  ← Dependencias Python
├── Procfile          ← Configuración para Railway
└── README.md         ← Esta guía

🚀 PASO A PASO: CONFIGURACIÓN COMPLETA
PASO 1 — Subir a GitHub

Ve a github.com y crea una cuenta si no tienes
Crea un repositorio nuevo llamado jarvis-whatsapp
Sube los 3 archivos: app.py, requirements.txt, Procfile


PASO 2 — Desplegar en Railway (servidor gratis)

Ve a → https://railway.app
Regístrate con tu cuenta de GitHub
Clic en "New Project"
Selecciona "Deploy from GitHub repo"
Elige tu repositorio jarvis-whatsapp
Railway despliega automáticamente ✅
Ve a Settings → Networking → Generate Domain
Copia tu URL (ej: https://jarvis-xxxx.up.railway.app)


PASO 3 — Activar WhatsApp con Twilio

Ve a → https://twilio.com y regístrate gratis
En el panel ve a: Messaging → Try it out → Send a WhatsApp message
Verás un número de Twilio y un código (ej: join bright-tiger)
Desde tu celular, envía ese código al número de Twilio por WhatsApp
Tu celular queda conectado al sandbox ✅


PASO 4 — Conectar Twilio con Railway

En Twilio ve a: Messaging → Sandbox Settings
En el campo "WHEN A MESSAGE COMES IN" pega:

   https://TU-URL-DE-RAILWAY.up.railway.app/webhook

Método: HTTP POST
Guarda los cambios ✅


PASO 5 — Probar
Envía cualquier mensaje desde tu WhatsApp al número de Twilio.
¡Jarvis responderá automáticamente! 🤖