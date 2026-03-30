# 🛡️ Sentinel KYC — Usuarios de Desarrollo Local

> ⚠️ Solo para uso local/dev. No compartir ni commitear.

**URLs:**
- Backend API → http://localhost:7020/api/v1
- Swagger → http://localhost:7020/api/docs
- Frontend User → http://localhost:3007
- Panel Admin → http://localhost:3003

---

## 👑 Super Admin

| Email | Password | Panel |
|---|---|---|
| `deco31416@gmail.com` | `1685Deco*+` | Panel Admin `:3003` |

---

## 🔧 Admins (Panel Admin)

| Email | Password | Rol |
|---|---|---|
| `admin.manager@yopmail.com` | `Manager123!` | `admin_manager` — crea otros admins |
| `admin.senior@yopmail.com` | `Senior123!` | `admin_senior` — permisos avanzados |
| `admin.junior@yopmail.com` | `Junior123!` | `admin_junior` — permisos básicos |
| `admin.viewer@yopmail.com` | `Viewer123!` | `admin_viewer` — solo lectura |

---

## 🏢 Empresas (Panel Admin / API)

| Email | Password | Rol | Empresa | Plan |
|---|---|---|---|---|
| `company.techcorp@yopmail.com` | `TechCorp123!` | `client_company` | TechCorp Demo S.A. | Professional |
| `company.fintech@yopmail.com` | `Fintech123!` | `client_company` | FintechDemo S.A. | Enterprise (Premium) |

---

## 👤 Usuarios Finales (Frontend User `:3007`)

| Email | Password | Rol | Empresa |
|---|---|---|---|
| `user.alice@yopmail.com` | `Alice123!` | `end_user` | TechCorp Demo S.A. |
| `user.bob@yopmail.com` | `Bob123456!` | `end_user` | TechCorp Demo S.A. |
| `user.carol@yopmail.com` | `Carol123!` | `end_user` | FintechDemo S.A. |

---

## 🚀 Arrancar entorno

```bash
python start-all.py
```

O manualmente:

```bash
# Terminal 1 — Backend :7020
cd sentinel-backend && yarn start:dev

# Terminal 2 — Frontend User :3007
cd sentinel-frontend-user && pnpm dev

# Terminal 3 — Panel Admin :3003
cd sentinel-panel-admin && pnpm dev
```

## 🔄 Re-sembrar BD (idempotente)

```bash
cd sentinel-backend && yarn seed
```
