# Railway Env: Frontend User Dev

Servicio Railway:
https://sentinel-frontend-dev.up.railway.app

Backend objetivo:
https://sentinel-backend-dev.up.railway.app

Notas:
- En apps Next.js sobre Railway no definas NODE_ENV manualmente.
- Usa siempre URLs Railway, no localhost.

Variables recomendadas:

```dotenv
NEXT_PUBLIC_APP_URL=https://sentinel-frontend-dev.up.railway.app

BACKEND_URL=https://sentinel-backend-dev.up.railway.app
NEXT_PUBLIC_API_URL=https://sentinel-backend-dev.up.railway.app
NEXT_PUBLIC_API_TIMEOUT=30000

NEXT_PUBLIC_SKIP_AUTH=false
NEXT_PUBLIC_ENABLE_VERCEL_ANALYTICS=false

NEXT_PUBLIC_OG_IMAGE=https://res.cloudinary.com/deco31416/image/upload/v1765056067/What-Is-KYC-in-Crypto_i2b3pw.png

NEXT_TELEMETRY_DISABLED=1
```

No definir en Railway para este servicio:

```dotenv
NODE_ENV=
PORT=
```