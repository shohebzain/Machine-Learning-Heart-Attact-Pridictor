"""
Build script — Assembles production-ready dist/ folder
Run: python build_dist.py
"""
import shutil
import os
import sys

SRC = os.path.dirname(os.path.abspath(__file__))
DIST = os.path.join(SRC, 'dist')

# Files/dirs to include in production build
INCLUDE_FILES = [
    'app.py',
    'SVM_heart.pkt',
    'columns.pkl',
    'scaler.pkl',
    'df_encode.pkl',
    'requirements.txt',
    'train_model.py',
]

INCLUDE_DIRS = [
    'templates',
    'static',
]

PRODUCTION_FILES = {
    'wsgi.py': '''"""WSGI entry point for production deployment."""
from app import app

if __name__ == "__main__":
    app.run()
''',

    'Procfile': 'web: waitress-serve --port=$PORT wsgi:app\n',

    '.env.example': '''FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=change-this-to-a-random-secret-key
PORT=5000
''',

    'run_production.bat': '''@echo off
echo ======================================
echo   CardioAI - Production Server
echo ======================================
echo.
echo Installing dependencies...
pip install -r requirements.txt >nul 2>&1
echo Starting production server on port 5000...
waitress-serve --port=5000 --threads=4 wsgi:app
pause
''',

    'run_production.sh': '''#!/bin/bash
echo "======================================"
echo "  CardioAI - Production Server"
echo "======================================"
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt > /dev/null 2>&1
echo "Starting production server on port 5000..."
waitress-serve --port=5000 --threads=4 wsgi:app
''',

    'Dockerfile': '''FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["waitress-serve", "--port=5000", "--threads=4", "wsgi:app"]
''',

    '.dockerignore': '''__pycache__
*.pyc
venv
.env
.git
''',
}


def build():
    print("[BUILD] CardioAI Production Build")
    print("=" * 40)

    # Clean previous dist
    if os.path.exists(DIST):
        print("[CLEAN] Removing old dist/...")
        shutil.rmtree(DIST)

    os.makedirs(DIST)
    print(f"[CREATE] dist/")

    # Copy source files
    for f in INCLUDE_FILES:
        src_path = os.path.join(SRC, f)
        dst_path = os.path.join(DIST, f)
        if os.path.exists(src_path):
            shutil.copy2(src_path, dst_path)
            print(f"  [COPY] {f}")
        else:
            print(f"  [WARN] {f} not found, skipping")

    # Copy directories
    for d in INCLUDE_DIRS:
        src_path = os.path.join(SRC, d)
        dst_path = os.path.join(DIST, d)
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
            count = sum(len(files) for _, _, files in os.walk(dst_path))
            print(f"  [COPY] {d}/ ({count} files)")

    # Update requirements.txt with production deps
    req_path = os.path.join(DIST, 'requirements.txt')
    with open(req_path, 'r') as f:
        existing = f.read().strip()
    with open(req_path, 'w') as f:
        f.write(existing + '\n')
        if 'waitress' not in existing:
            f.write('waitress\n')
        if 'gunicorn' not in existing:
            f.write('gunicorn\n')
    print("  [UPDATE] requirements.txt (added waitress, gunicorn)")

    # Generate production files
    for filename, content in PRODUCTION_FILES.items():
        fpath = os.path.join(DIST, filename)
        with open(fpath, 'w', newline='\n') as f:
            f.write(content)
        print(f"  [GEN] {filename}")

    # Make shell script executable
    sh_path = os.path.join(DIST, 'run_production.sh')
    if os.path.exists(sh_path):
        os.chmod(sh_path, 0o755)

    # Create production app.py (disable debug mode)
    app_path = os.path.join(DIST, 'app.py')
    with open(app_path, 'r') as f:
        content = f.read()
    content = content.replace("debug=True", "debug=False")
    content = content.replace("app.run(debug=True)", "app.run(debug=False)")
    with open(app_path, 'w') as f:
        f.write(content)
    print("  [PATCH] app.py (debug=False)")

    # Summary
    total_files = sum(len(files) for _, _, files in os.walk(DIST))
    total_size = sum(
        os.path.getsize(os.path.join(dp, f))
        for dp, _, fnames in os.walk(DIST)
        for f in fnames
    )
    print()
    print("=" * 40)
    print(f"[DONE] Production build complete!")
    print(f"  Location: {DIST}")
    print(f"  Files:    {total_files}")
    print(f"  Size:     {total_size / 1024:.1f} KB")
    print()
    print("To run production server:")
    print("  cd dist")
    print("  pip install -r requirements.txt")
    print("  python wsgi.py")
    print("  -- OR --")
    print("  waitress-serve --port=5000 wsgi:app")


if __name__ == '__main__':
    build()
