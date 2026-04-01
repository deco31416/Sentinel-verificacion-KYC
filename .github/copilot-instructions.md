# Copilot Instructions — Sentinel KYC (Workspace Global)

> Aplica a **todo el workspace** `Sentinel-KYC`.
> Contiene arquitectura, mapa de repos, reglas transversales y convenciones globales.
> Cada repo tiene su propio `.github/copilot-instructions.md` con reglas específicas del servicio.

---

## 1. Qué es Sentinel KYC

**Sentinel KYC** es una plataforma completa de verificación de identidad (Know Your Customer) con IA:
- Verificación facial en tiempo real (liveness check + face match)
- Análisis y validación de documentos de identidad (OCR + anti-AI)
- Biometría de voz para autenticación
- Análisis de comportamiento y detección de fraude
- Panel administrativo multi-tenant para operadores de compliance
- SDK oficial para TypeScript/JS, Kotlin (Android) y Swift (iOS/macOS)
- Sistema de webhooks para integración con terceros
- Manual review y audit log completo para compliance

---

## 2. Mapa del Sistema

```
+-------------------------------------------------------------------------+
|                      WORKSPACE: Sentinel-KYC                           |
|                                                                         |
|  sentinel-frontend-user  :3007  (Next.js 16 App Router)                |
|    | HTTP /api/* -> Next.js API proxy routes                            |
|    +-----------------------------------------------------------> :7020  |
|                                                                         |
|  sentinel-panel-admin    :3003  (Next.js 16 App Router)                |
|    | HTTP /api/* -> Next.js API proxy routes                            |
|    +-----------------------------------------------------------> :7020  |
|                                                                         |
|  sentinel-backend        :7020  (NestJS REST API)                      |
|    +-- /api/v1/auth/**         JWT + MFA + sesiones                    |
|    +-- /api/v1/kyc/**          Sesiones KYC + revision                 |
|    +-- /api/v1/users/**        Gestion de usuarios                     |
|    +-- /api/v1/companies/**    Multi-tenant empresas                   |
|    +-- /api/v1/api-keys/**     API keys + webhooks                     |
|    +-- /api/v1/dashboard/**    Metricas y stats                        |
|    +-- /api/v1/screening/**    Screening de sujetos                    |
|    +-- /api/v1/flows/**        Flujos KYC configurables                |
|                |                                                        |
|                +---- HTTP ----> Python AI Services                     |
|                          +-- computer-vision-service                   |
|                          +-- machine-ocr-service                       |
|                          +-- voice-biometric-service                   |
|                          +-- behavioral-analytics-service              |
|                          +-- cognitive-learning-service                |
|                          +-- machine-learning-service                  |
|                                                                         |
|  SDK Clients:                                                           |
|    sdk-typescript  ->  HTTP -> sentinel-backend :7020                  |
|    sdk-kotlin      ->  HTTP -> sentinel-backend :7020                  |
|    sdk-swift       ->  HTTP -> sentinel-backend :7020                  |
+-------------------------------------------------------------------------+
```

---

## 3. Tabla de Repositorios

| Repo | Funcion | Puerto local | Stack | Pkg Manager | Remote |
|------|---------|-------------|-------|-------------|--------|
| `sentinel-backend` | API REST + auth + KYC + webhooks | **7020** | NestJS v10 + MongoDB | Yarn@4 | sentinel-kyc/sentinel-backend |
| `sentinel-frontend-user` | UI verificacion usuarios finales | **3007** | Next.js 16 + React 19 | pnpm | sentinel-kyc/sentinel-frontend-user |
| `sentinel-panel-admin` | Panel admin multi-tenant | **3003** | Next.js 16 + React 19 | pnpm | sentinel-kyc/sentinel-panel-admin |
| `sdk-typescript` | SDK oficial JS/TS | — | TypeScript + tsup + vitest | npm | sentinel-kyc/sdk-typescript |
| `sdk-kotlin` | SDK oficial Android | — | Kotlin + Gradle (API 24+) | gradle | sentinel-kyc/sdk-kotlin |
| `sdk-swift` | SDK oficial iOS/macOS 14+ | — | Swift + SPM | spm | sentinel-kyc/sdk-swift |
| `sentinel-services-computer-vision-service` | Vision computacional + face match | — | Python + FastAPI | pip/venv | — |
| `sentinel-services-machine-ocr-service` | OCR de documentos | — | Python + FastAPI | pip/venv | — |
| `sentinel-services-voice-biometric-service` | Biometria de voz | — | Python + FastAPI | pip/venv | — |
| `sentinel-services-behavioral-analytics-service` | Analisis de comportamiento | — | Python + FastAPI | pip/venv | — |
| `sentinel-services-cognitive-learning-service` | Aprendizaje cognitivo | — | Python + FastAPI | pip/venv | — |
| `sentinel-services-machine-learning-service` | ML general | — | Python + FastAPI | pip/venv | — |
| `sentinel--Kyc` | Documentacion y recursos compartidos | — | Monorepo docs | — | sentinel-kyc/sentinel--Kyc |

---

## 4. Estructura Git — CRITICO

> **Cada carpeta del workspace es un repositorio Git INDEPENDIENTE.**
> NO son submodules. Cada uno tiene su propio `.git/` y se push a su propio remote.
> El workspace raiz (`Sentinel-KYC`) es tambien un repo independiente en deco31416.

| Directorio | Remote origin | Rama activa |
|-----------|--------------|-------------|
| `Sentinel-KYC` (raiz) | deco31416/Sentinel-verificacion-KYC | development |
| `sentinel-backend` | sentinel-kyc/sentinel-backend | development |
| `sentinel-frontend-user` | sentinel-kyc/sentinel-frontend-user | development |
| `sentinel-panel-admin` | sentinel-kyc/sentinel-panel-admin | development |
| `sdk-typescript` | sentinel-kyc/sdk-typescript | development |
| `sdk-kotlin` | sentinel-kyc/sdk-kotlin | development |
| `sdk-swift` | sentinel-kyc/sdk-swift | development |
| `sentinel--Kyc` | sentinel-kyc/sentinel--Kyc | development |

### Workflow de commits por subrepo

Siempre entrar al directorio del repo antes de hacer git:

```bash
cd sentinel-panel-admin   # ir al repo especifico
git add -A
git commit -m "type(scope): descripcion"
git push origin development
```

### Convencion de commits (Conventional Commits)

| Prefijo | Uso |
|---------|-----|
| `feat` | Nueva funcionalidad |
| `fix` | Bug fix |
| `chore` | Mantenimiento, deps, config |
| `refactor` | Refactor sin cambio funcional |
| `docs` | Solo documentacion |
| `test` | Tests |
| `perf` | Mejora de rendimiento |

---

## 5. Comunicacion entre Servicios

### Frontends -> Backend

| Origen | Protocolo | Proxy Next.js | Destino |
|--------|-----------|---------------|---------|
| `sentinel-frontend-user` browser | HTTP REST | `/api/auth/*` | backend :7020/api/v1/auth/* |
| `sentinel-frontend-user` browser | HTTP REST | `/api/kyc/*` | backend :7020/api/v1/kyc/* |
| `sentinel-frontend-user` browser | HTTP REST | `/api/users/*` | backend :7020/api/v1/users/* |
| `sentinel-panel-admin` browser | HTTP REST | `/api/*` | backend :7020/api/v1/* |

> El browser NUNCA llama directamente a `:7020`. SIEMPRE pasa por rutas proxy Next.js (`app/api/`).

### Backend -> Servicios Python

El backend delega procesamiento IA a microservicios Python via HTTP con API key.
Cada servicio Python tiene su propia variable de entorno en el backend:
`DATA_SENTINEL_ENDPOINT`, `DATA_SENTINEL_API_KEY`, `DATA_SENTINEL_HMAC_SECRET`

---

## 6. Variables de Entorno — Referencia Cruzada

### sentinel-backend
```bash
PORT=7020
MONGODB_URI=mongodb://localhost:27017/sentinel-kyc
JWT_SECRET=...                          # HS256 en dev, RS256 en prod
JWT_REFRESH_SECRET=...
FRONTEND_URL=http://localhost:3003      # Panel admin por defecto
CORS_ORIGIN=http://localhost:3003,http://localhost:3007
DATA_SENTINEL_ENDPOINT=...
DATA_SENTINEL_API_KEY=...
DATA_SENTINEL_HMAC_SECRET=...
```

### sentinel-frontend-user
```bash
NEXT_PUBLIC_APP_URL=http://localhost:3007
BACKEND_URL=http://localhost:7020       # Server-only — nunca al browser
```

### sentinel-panel-admin
```bash
NEXT_PUBLIC_APP_URL=http://localhost:3003
BACKEND_URL=http://localhost:7020       # Server-only — nunca al browser
```

---

## 7. Seguridad — Reglas Globales

### Autenticacion
- Todos los endpoints del backend requieren JWT (`Bearer access_token`), excepto `/auth/login` y `/health`.
- El browser accede al backend SIEMPRE por rutas proxy Next.js (`app/api/`).
- Tokens JWT en `httpOnly cookies` — nunca en `localStorage` o `sessionStorage`.
- MFA obligatorio: OTP por email/SMS antes de emitir el `access_token` final.

### Secretos
- Contrasenas: **bcrypt** siempre — nunca bcrypt, MD5 o SHA1.
- JWT: HS256 en desarrollo, RS256 con clave asimetrica en produccion.
- Variables sensibles: `.env.local` — nunca commitear `.env.local`.

### CORS
- Origenes explicitos en `CORS_ORIGIN` — no `*` en produccion.
- Los frontends se comunican con el backend solo via proxy routes.

### Validacion
- NestJS: `ValidationPipe` con `whitelist: true, forbidNonWhitelisted: true, transform: true`.
- Next.js API routes: validar inputs antes de proxear al backend.
- Servicios Python: Pydantic para todos los schemas.

---

## 8. Convenciones Globales

### Variables de Entorno
- `NEXT_PUBLIC_*` → expuesto al browser (solo si es absolutamente necesario)
- `BACKEND_URL` → URL del backend (solo servidor Next.js, jamas al browser)
- `SCREAMING_SNAKE_CASE` para todas las variables

### Rutas HTTP
- REST: `kebab-case` → `/api/v1/kyc/sessions/:id`
- No verbos en rutas — usar el metodo HTTP correcto (GET/POST/PUT/DELETE)

### MongoDB
- `snake_case` para field names: `created_at`, `user_id`, `risk_score`
- Normalizar `_id -> id` en TODOS los responses al frontend

### Eventos / Webhooks
- `camelCase` con namespace: `kyc:status_updated`, `session:created`

---

## 9. Reglas Globales para Copilot

### Frontends Next.js (panel-admin y frontend-user)
- **1 archivo `.tsx` = 1 componente React exportado.** Nunca 2-3 componentes en el mismo archivo.
- **Fetch solo via `lib/api/`** hacia rutas proxy `app/api/` — nunca fetch directo al backend.
- Iconos: `lucide-react` siempre. Nunca emojis para UI.
- Componentes reutilizables en `components/ui/` y `components/shared/`.
- Formularios: `react-hook-form` + `zod` para validacion del lado cliente.
- Tailwind v4: no `@apply` con utilidades de Tailwind v4.
- Scrollbars personalizadas definidas en `app/globals.css` (unico archivo de estilos globales).

### Backend NestJS
- Paquetes con `yarn` (Yarn@4) — nunca npm ni pnpm en este repo.
- Un modulo por dominio — nunca mezclar logica de dominios distintos.
- DTOs con `class-validator` + `class-transformer` en todos los endpoints.
- Respuestas uniformes via `TransformInterceptor`.
- Normalizar `_id -> id` antes de enviar al cliente.

### SDKs
- Librerias puras — sin dependencias de UI, sin deps de Node.js server.
- `baseUrl` siempre provista por el consumidor — nunca hardcodeada.
- Errores tipados con `SentinelKycError` con `code: string`.

### Servicios Python
- Virtual environment `.venv/` por servicio.
- Schemas Pydantic para todos los modelos.
- `@asynccontextmanager lifespan` — no `@app.on_event`.
- Todo I/O asincrono con `async/await`.

### Lo que Copilot NO debe hacer en ningun repo
- Cambiar puertos sin actualizar este archivo (seccion 3).
- Usar `fetch()` directo al backend desde componentes React.
- Guardar tokens JWT en `localStorage`.
- Usar `CORS: *` en produccion.
- Crear 2+ componentes en el mismo `.tsx`.
- Usar `any` en TypeScript sin comentario de justificacion.
- Commitear `.env.local` o archivos con secretos.
- Usar el package manager incorrecto por repo (ver tabla seccion 3).
- Mezclar estilos inline con Tailwind — elegir uno.

---

## 10. Instrucciones Detalladas por Repo

| Repo | Instrucciones especificas |
|------|--------------------------|
| `sentinel-backend` | `.github/copilot-instructions.md` — NestJS, MongoDB, bcrypt, JWT |
| `sentinel-frontend-user` | `.github/copilot-instructions.md` — Next.js 16, proxy routes, KYC flow |
| `sentinel-panel-admin` | `.github/copilot-instructions.md` — Next.js 16, OTPModal, admin features |
| `sdk-typescript` | `.github/copilot-instructions.md` — tsup, vitest, isomorfico |
| `sdk-kotlin` | `.github/copilot-instructions.md` — Coroutines, Gradle, Android |
| `sdk-swift` | `.github/copilot-instructions.md` — async/await, SPM, iOS/macOS |