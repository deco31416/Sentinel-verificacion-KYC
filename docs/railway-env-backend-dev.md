# Railway Env: Backend Dev

Servicio Railway:
https://sentinel-backend-dev.up.railway.app

Frontends conectados a este backend:
- https://sentinel-panel-admin-dev.up.railway.app
- https://sentinel-frontend-dev.up.railway.app

Objetivo:
- Mantener la misma estructura de variables que [sentinel-backend/.env.local](sentinel-backend/.env.local)
- Cambiar solo URLs y hosts para Railway donde aplica
- No guardar secretos reales en este documento

Notas:
- Si Railway ya inyecta `PORT`, puedes dejar esa variable sin crear manualmente.
- Si quieres replicar exactamente la forma del local, aquí la dejo incluida de todos modos.
- Este archivo es para entorno development en Railway, no producción.

Bloque completo equivalente al local:

```dotenv
# ========================================
# 🖥️ SENTINEL BACKEND — RAILWAY DEV CONFIG
# ========================================
# Railway backend: https://sentinel-backend-dev.up.railway.app
# Railway frontend-user: https://sentinel-frontend-dev.up.railway.app
# Railway panel-admin: https://sentinel-panel-admin-dev.up.railway.app

# Application
NODE_ENV=development
PORT=7020
API_PREFIX=api/v1

# MongoDB
MONGODB_URI=<YOUR_MONGODB_URI>

# JWT Authentication
JWT_SECRET=<YOUR_JWT_SECRET>
JWT_EXPIRES_IN=24h

# AES-256-GCM Encryption (for PII data)
ENCRYPTION_SECRET=<YOUR_ENCRYPTION_SECRET_BASE64>

# ========================================
# 📧 EMAIL
# ========================================
EMAIL_PROVIDER=resend
EMAIL_FROM=contacto@deco31416.com
EMAIL_FROM_NAME=Sentinel KYC
RESEND_API_KEY=<YOUR_RESEND_API_KEY>

# (No usar salvo que realmente cambies de proveedor)
# GMAIL_USER=your-email@gmail.com
# GMAIL_APP_PASSWORD=xxxx xxxx xxxx xxxx

# ========================================
# 🔔 SENTRY
# ========================================
SENTRY_DSN=<YOUR_SENTRY_DSN>
SENTRY_ENVIRONMENT=development
SENTRY_TRACES_SAMPLE_RATE=1.0
SENTRY_PROFILES_SAMPLE_RATE=1.0

# ========================================
# 💬 TWILIO — SMS OTP
# ========================================
TWILIO_ACCOUNT_SID=<YOUR_TWILIO_ACCOUNT_SID>
TWILIO_AUTH_TOKEN=<YOUR_TWILIO_AUTH_TOKEN>
TWILIO_PHONE_NUMBER=<YOUR_TWILIO_PHONE_NUMBER>

# ========================================
# 🔴 REDIS
# ========================================
REDIS_URL=<YOUR_REDIS_URL>

# ========================================
# 🛡️ DATA SENTINEL — SCREENING ENGINE
# ========================================
# ⚠️ En Railway no hay localhost — apunta al host real del servicio si existe
DATA_SENTINEL_ENDPOINT=<url-del-servicio-data-sentinel>
DATA_SENTINEL_API_KEY=CHANGE_THIS_SHARED_SECRET_BETWEEN_SENTINEL_AND_ENGINE_MIN_32_CHARS
DATA_SENTINEL_HMAC_SECRET=CHANGE_THIS_SHARED_SECRET_BETWEEN_SENTINEL_AND_ENGINE_MIN_32_CHARS
DATA_SENTINEL_TIMEOUT=30000

# ========================================
# ☁️ CLOUDINARY
# ========================================
CLOUDINARY_CLOUD_NAME=deco31416
CLOUDINARY_API_KEY=<YOUR_CLOUDINARY_API_KEY>
CLOUDINARY_API_SECRET=<YOUR_CLOUDINARY_API_SECRET>

# ========================================
# 🌐 CORS — RAILWAY URLS
# ========================================
CORS_ORIGIN=https://sentinel-frontend-dev.up.railway.app,https://sentinel-panel-admin-dev.up.railway.app
FRONTEND_URL=https://sentinel-panel-admin-dev.up.railway.app

# ========================================
# 🤖 GROQ API
# ========================================
GROQ_API_KEY=<YOUR_GROQ_API_KEY>

# Modelos
GROQ_CV_MODEL=llama-3.3-70b-versatile
GROQ_VISION_MODEL=meta-llama/llama-4-scout-17b-16e-instruct
GROQ_VOICE_MODEL=whisper-large-v3

# Estrategias (GROQ_ONLY = Python microservicios eliminados)
GROQ_CV_STRATEGY=GROQ_ONLY
GROQ_OCR_STRATEGY=GROQ_ONLY
GROQ_VOICE_STRATEGY=GROQ_ONLY

GROQ_CV_FALLBACK_ENABLED=true
GROQ_OCR_FALLBACK_ENABLED=true
GROQ_VOICE_FALLBACK_ENABLED=true

GROQ_CV_TIMEOUT=3000
GROQ_OCR_TIMEOUT=10000
GROQ_VOICE_TIMEOUT=5000
```

Diferencias intencionales frente al local:
- `CORS_ORIGIN` usa las dos URLs Railway de frontend.
- `FRONTEND_URL` apunta al panel admin en Railway.
- `DATA_SENTINEL_ENDPOINT` en local era `localhost:5000` — en Railway debe apuntar al host real del servicio de screening (si no existe aún, déjalo deshabilitado o usa la URL del servicio cuando esté deployado).