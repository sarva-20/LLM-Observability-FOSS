"""
Setup Validation Script
Run this to verify your environment is configured correctly
"""

import sys
import os

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"❌ Python version: {version.major}.{version.minor}.{version.micro}")
        print("   Required: Python 3.11 or 3.12")
        return False

def check_packages():
    """Check if required packages are installed"""
    packages = [
        "google.genai",
        "dotenv",
        "langtrace_python_sdk",
        "opentelemetry",
        "traceloop",
        "opik"
    ]
    
    all_installed = True
    for package in packages:
        try:
            __import__(package.replace(".", "_") if "." in package else package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} not installed")
            all_installed = False
    
    return all_installed

def check_env_file():
    """Check if .env file exists and has required keys"""
    if not os.path.exists(".env"):
        print("❌ .env file not found")
        print("   Create a .env file with your API keys")
        return False
    
    print("✅ .env file found")
    
    required_keys = ["GEMINI_API_KEY", "LANGTRACE_API_KEY"]
    optional_keys = ["OPIK_API_KEY", "OPIK_WORKSPACE"]
    
    with open(".env", "r") as f:
        content = f.read()
    
    missing_required = []
    for key in required_keys:
        if key not in content:
            missing_required.append(key)
    
    if missing_required:
        print(f"❌ Missing required keys: {', '.join(missing_required)}")
        return False
    else:
        print("✅ All required API keys present")
    
    missing_optional = []
    for key in optional_keys:
        if key not in content:
            missing_optional.append(key)
    
    if missing_optional:
        print(f"⚠️  Optional keys missing: {', '.join(missing_optional)}")
        print("   (Only needed for unified demo)")
    
    return True

def check_docker():
    """Check if Docker is running"""
    import subprocess
    try:
        result = subprocess.run(
            ["docker", "ps"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ Docker is running")
            
            # Check if Jaeger container exists
            if "jaeger" in result.stdout:
                print("✅ Jaeger container is running")
            else:
                print("⚠️  Jaeger container not found")
                print("   Run: docker start jaeger")
            return True
        else:
            print("❌ Docker is not running")
            print("   Start Docker Desktop")
            return False
    except FileNotFoundError:
        print("❌ Docker not installed")
        print("   Install Docker Desktop from docker.com")
        return False

def main():
    print("=" * 60)
    print("🔍 LLM Observability Demo - Setup Validation")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version()),
        ("Required Packages", check_packages()),
        ("Environment Variables", check_env_file()),
        ("Docker & Jaeger", check_docker())
    ]
    
    print()
    print("=" * 60)
    print("📊 Summary")
    print("=" * 60)
    
    passed = sum(1 for _, result in checks if result)
    total = len(checks)
    
    for name, result in checks:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    print()
    if passed == total:
        print("🎉 All checks passed! You're ready to run the demos!")
        print()
        print("Next steps:")
        print("1. Run: python chatbot_v1_no_observability.py")
        print("2. Follow the README for more demos")
    else:
        print(f"⚠️  {total - passed} check(s) failed")
        print()
        print("Fix the issues above and run this script again:")
        print("python validate_setup.py")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
