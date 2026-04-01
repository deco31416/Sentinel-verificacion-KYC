"""
Sentinel KYC — Lanzador local
==============================
Abre 3 ventanas CMD visibles independientes:

  [1] Backend        →  http://localhost:7020/api/v1
  [2] Frontend User  →  http://localhost:3007
  [3] Panel Admin    →  http://localhost:3003

Uso: python start-all.py
"""

import subprocess
import os
import time

ROOT = os.path.dirname(os.path.abspath(__file__))


def read_port_from_env(project_dir, fallback):
    """Lee PORT= del .env.local del proyecto. Si no existe, usa fallback."""
    env_file = os.path.join(project_dir, ".env.local")
    if not os.path.isfile(env_file):
        return fallback
    with open(env_file, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line.startswith("PORT="):
                return line.split("=", 1)[1].strip()
    return fallback


BACKEND_DIR = os.path.join(ROOT, "sentinel-backend")
FRONTEND_DIR = os.path.join(ROOT, "sentinel-frontend-user")
PANEL_DIR = os.path.join(ROOT, "sentinel-panel-admin")

frontend_port = read_port_from_env(FRONTEND_DIR, "3007")
panel_port = read_port_from_env(PANEL_DIR, "3003")

projects = [
    {
        "title": f"SENTINEL BACKEND :7020",
        "dir": BACKEND_DIR,
        "cmd": "yarn start:dev",
        "color": "0A",  # verde sobre negro
    },
    {
        "title": f"SENTINEL FRONTEND USER :{frontend_port}",
        "dir": FRONTEND_DIR,
        "cmd": f"pnpm dev -p {frontend_port}",
        "color": "0B",  # amarillo sobre negro
    },
    {
        "title": f"SENTINEL PANEL ADMIN :{panel_port}",
        "dir": PANEL_DIR,
        "cmd": f"pnpm dev -p {panel_port}",
        "color": "0D",  # magenta sobre negro
    },
]

print("=" * 55)
print("  🛡️  Sentinel KYC — Arrancando entorno local...")
print("=" * 55)

for p in projects:
    # color /T:0X cambia el color de la nueva ventana (fondo/letra)
    full_cmd = (
        f'start "{p["title"]}" /D "{p["dir"]}" '
        f'cmd /k "color {p["color"]} && echo. && echo  [{p["title"]}] && echo. && {p["cmd"]}"'
    )
    subprocess.Popen(full_cmd, shell=True)
    print(f"  ✔  {p['title']}")
    time.sleep(1)  # pequeña pausa para que no choquen las ventanas al abrirse

print()
print("  Servicios iniciados:")
print("  • Backend     →  http://localhost:7020/api/v1")
print("  • Backend     →  http://localhost:7020/api/docs  (Swagger)")
print(f"  • Frontend    →  http://localhost:{frontend_port}")
print(f"  • Panel Admin →  http://localhost:{panel_port}")
print()
print("  Cierra las ventanas individuales para detener cada servicio.")
print("=" * 55)
