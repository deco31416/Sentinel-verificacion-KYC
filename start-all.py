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

projects = [
    {
        "title": "SENTINEL BACKEND :7020",
        "dir": os.path.join(ROOT, "sentinel-backend"),
        "cmd": "yarn start:dev",
        "color": "0A",  # verde sobre negro
    },
    {
        "title": "SENTINEL FRONTEND USER :3007",
        "dir": os.path.join(ROOT, "sentinel-frontend-user"),
        "cmd": "pnpm dev",
        "color": "0B",  # amarillo sobre negro
    },
    {
        "title": "SENTINEL PANEL ADMIN :3003",
        "dir": os.path.join(ROOT, "sentinel-panel-admin"),
        "cmd": "pnpm dev",
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
print("  • Frontend    →  http://localhost:3007")
print("  • Panel Admin →  http://localhost:3003")
print()
print("  Cierra las ventanas individuales para detener cada servicio.")
print("=" * 55)
