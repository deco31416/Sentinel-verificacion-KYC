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

## 🏢 Empresas (Frontend User `:3007`)

| Email | Password | Rol | Empresa | Plan | companyId en DB |
|---|---|---|---|---|---|
| `company.techcorp@yopmail.com` | `TechCorp123!` | `client_company` | TechCorp Demo S.A. | Professional | `69cadae64472eb3363653d27` |
| `company.fintech@yopmail.com` | `Fintech123!` | `client_company` | FintechDemo S.A. | Enterprise | `69cadae64472eb3363653d29` |
| `company.admin@sentinel-kyc.com` | `Company123!Admin` | `client_company` | Sentinel Demo Company | Starter | `6944fddd4f969a657afb93c5` |

---

## 👤 Usuarios Finales (Frontend User `:3007`)

| Email | Password | Rol | Empresa |
|---|---|---|---|
| `user@sentinel-kyc.com` | `User123!Demo` | `end_user` | Sentinel Demo Company |
| `agent@sentinel-kyc.com` | `Agent123!KYC` | `end_user` | Sentinel Demo Company |

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
