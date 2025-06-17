import sys
import platform
import os

print("="*40)
print("🔍 PYTHON ENVIRONMENT CHECK")
print("="*40)

# Version Info
print(f"✅ Python Version     : {platform.python_version()}")
print(f"✅ Python Executable  : {sys.executable}")

# OS Info
print(f"🖥️ Operating System   : {platform.system()} {platform.release()}")

# Check PATH
print("\n📁 Checking if Python is in PATH...")
path_dirs = os.environ['PATH'].split(';')
python_in_path = any("python" in p.lower() for p in path_dirs)

print(f"🔗 Python in PATH     : {'✅ YES' if python_in_path else '❌ NO'}")

# Check pip
try:
    import pip
    print(f"\n📦 pip Installed      : ✅ Version {pip.__version__}")
except ImportError:
    print("\n📦 pip Installed      : ❌ NOT FOUND")

# Suggest command
print("\n👉 Try running: python --version")
print("👉 Try running: pip list")

print("\n✅ Setup Verified. You're good to go!" if python_in_path else "\n⚠️ Python might not be correctly added to PATH.")
print("="*40)
