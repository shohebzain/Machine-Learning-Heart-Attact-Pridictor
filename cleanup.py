"""
Project Directory Cleanup Script
Removes temporary, generated, and unnecessary files/folders.
Preserves all source code, configuration, and documentation.

Usage:
    python cleanup.py              # Interactive mode (lists items, asks confirmation)
    python cleanup.py --dry-run    # Preview only, no deletions
    python cleanup.py --auto       # Skip confirmation (use with caution)
"""

import io, sys
# Fix Windows console encoding for Unicode characters
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

import os
import sys
import shutil
import argparse
from pathlib import Path

# ── Configuration ──────────────────────────────────────────────

# Directories to remove (matched by name, anywhere in tree)
REMOVE_DIRS = {
    '__pycache__',
    'node_modules',
    '.vscode',
    '.idea',
    'dist',
    'build',
    '.mypy_cache',
    '.pytest_cache',
    '.tox',
    '.eggs',
    '*.egg-info',
    '.sass-cache',
    '.parcel-cache',
    '.next',
    '.nuxt',
    '.cache',
    '.temp',
    '.tmp',
}

# File patterns to remove (matched by name or extension)
REMOVE_FILE_PATTERNS = {
    # OS artifacts
    '.DS_Store',
    'Thumbs.db',
    'desktop.ini',
    # Log and temp files
    '*.log',
    '*.tmp',
    '*.temp',
    '*.bak',
    '*.swp',
    '*.swo',
    '*~',
    # Python compiled
    '*.pyc',
    '*.pyo',
    '*.pyd',
    # Coverage / profiling
    '.coverage',
    'coverage.xml',
    'htmlcov',
}

# Always preserve these (never delete even if they match a pattern)
PRESERVE = {
    'app.py',
    'train_model.py',
    'test_system.py',
    'test_integration.py',
    'run_tests_and_report.py',
    'cleanup.py',
    'requirements.txt',
    'README.md',
    'SUMMARY.md',
    'CHECKLIST.md',
    'BUGS_FIXED.md',
    'TROUBLESHOOTING.md',
    'TEST_REPORT.md',
    'run_server.bat',
    'SVM_heart.pkt',
    'columns.pkl',
    'scaler.pkl',
    'df_encode.pkl',
    'index.html',
    'style.css',
    'script.js',
    'venv',           # Keep virtual environment
}

# Directories to never descend into
SKIP_DIRS = {'venv', '.git', 'templates', 'static'}


def matches_pattern(name, patterns):
    """Check if a filename matches any of the glob-like patterns."""
    from fnmatch import fnmatch
    for pattern in patterns:
        if fnmatch(name, pattern):
            return True
    return False


def find_items_to_remove(root_dir):
    """Scan directory and return lists of (dirs, files) to remove."""
    dirs_to_remove = []
    files_to_remove = []

    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=True):
        # Skip protected directories
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        rel_dir = os.path.relpath(dirpath, root_dir)

        for d in list(dirnames):
            if d in PRESERVE:
                continue
            full_path = os.path.join(dirpath, d)
            if d in REMOVE_DIRS or matches_pattern(d, REMOVE_DIRS):
                dirs_to_remove.append(full_path)
                dirnames.remove(d)  # Don't descend into it

        for f in filenames:
            if f in PRESERVE:
                continue
            full_path = os.path.join(dirpath, f)
            if f in REMOVE_FILE_PATTERNS or matches_pattern(f, REMOVE_FILE_PATTERNS):
                files_to_remove.append(full_path)

    return dirs_to_remove, files_to_remove


def format_size(size_bytes):
    """Format bytes to human-readable size."""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"


def get_dir_size(path):
    """Get total size of a directory."""
    total = 0
    try:
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                try:
                    total += os.path.getsize(fp)
                except OSError:
                    pass
    except OSError:
        pass
    return total


def main():
    parser = argparse.ArgumentParser(description="Clean project directory of temporary files")
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview items to remove without deleting anything')
    parser.add_argument('--auto', action='store_true',
                        help='Skip confirmation prompt (use with caution)')
    parser.add_argument('--path', type=str, default='.',
                        help='Root directory to clean (default: current directory)')
    args = parser.parse_args()

    root = os.path.abspath(args.path)

    print()
    print("=" * 60)
    print("  Project Directory Cleanup")
    print("=" * 60)
    print(f"\n  Root: {root}")
    if args.dry_run:
        print("  Mode: DRY RUN (no files will be deleted)")
    else:
        print("  Mode: LIVE (files will be deleted after confirmation)")
    print()

    # Scan
    print("  Scanning for items to remove...")
    dirs_to_remove, files_to_remove = find_items_to_remove(root)

    if not dirs_to_remove and not files_to_remove:
        print("\n  ✅ Project is already clean! Nothing to remove.")
        return 0

    # Display directories
    total_size = 0
    if dirs_to_remove:
        print(f"\n  📁 Directories to remove ({len(dirs_to_remove)}):")
        print("  " + "-" * 56)
        for d in sorted(dirs_to_remove):
            rel = os.path.relpath(d, root)
            size = get_dir_size(d)
            total_size += size
            print(f"    🗑️  {rel:<40} {format_size(size):>10}")

    # Display files
    if files_to_remove:
        print(f"\n  📄 Files to remove ({len(files_to_remove)}):")
        print("  " + "-" * 56)
        for f in sorted(files_to_remove):
            rel = os.path.relpath(f, root)
            try:
                size = os.path.getsize(f)
                total_size += size
            except OSError:
                size = 0
            print(f"    🗑️  {rel:<40} {format_size(size):>10}")

    # Summary
    print(f"\n  {'=' * 56}")
    print(f"  Total items:  {len(dirs_to_remove)} directories, {len(files_to_remove)} files")
    print(f"  Total size:   {format_size(total_size)}")
    print(f"  {'=' * 56}")

    # Preserved items notice
    print(f"\n  ✅ Protected (will NOT be deleted):")
    print(f"     Source code, config files, documentation, model files,")
    print(f"     templates/, static/, venv/, .git/")

    if args.dry_run:
        print(f"\n  ℹ️  DRY RUN complete. No files were deleted.")
        print(f"     Run without --dry-run to perform actual cleanup.\n")
        return 0

    # Confirmation
    if not args.auto:
        print()
        try:
            answer = input("  ⚠️  Proceed with deletion? (yes/no): ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n\n  ❌ Aborted by user. No files were deleted.\n")
            return 1

        if answer not in ('yes', 'y'):
            print("\n  ❌ Aborted. No files were deleted.\n")
            return 1

    # Delete
    print("\n  Deleting items...")
    errors = []

    for d in dirs_to_remove:
        try:
            shutil.rmtree(d)
            rel = os.path.relpath(d, root)
            print(f"    ✅ Removed directory: {rel}")
        except Exception as e:
            errors.append(f"Dir {d}: {e}")
            print(f"    ❌ Failed: {os.path.relpath(d, root)} - {e}")

    for f in files_to_remove:
        try:
            os.remove(f)
            rel = os.path.relpath(f, root)
            print(f"    ✅ Removed file: {rel}")
        except Exception as e:
            errors.append(f"File {f}: {e}")
            print(f"    ❌ Failed: {os.path.relpath(f, root)} - {e}")

    # Result
    print(f"\n  {'=' * 56}")
    if errors:
        print(f"  ⚠️  Cleanup completed with {len(errors)} error(s).")
        for err in errors:
            print(f"     - {err}")
    else:
        print(f"  ✅ Cleanup complete! Removed {len(dirs_to_remove)} dirs, {len(files_to_remove)} files.")
        print(f"     Freed {format_size(total_size)} of space.")
    print(f"  {'=' * 56}\n")

    return 0


if __name__ == '__main__':
    sys.exit(main())
