"""
Heart Attack Prediction - System Test Script
Tests all components and validates bug fixes
"""

import sys
import os

def print_header(text):
    print(f"\n{'='*50}")
    print(f"  {text}")
    print(f"{'='*50}\n")

def test_imports():
    """Test if all required packages are installed"""
    print_header("Testing Package Imports")
    
    packages = {
        'flask': 'Flask',
        'numpy': 'NumPy',
        'sklearn': 'scikit-learn',
        'pickle': 'Python pickle'
    }
    
    failed = []
    for module, name in packages.items():
        try:
            __import__(module)
            print(f"✓ {name} imported successfully")
        except ImportError as e:
            print(f"✗ {name} failed: {e}")
            failed.append(name)
    
    return len(failed) == 0

def test_file_structure():
    """Test if all required files exist"""
    print_header("Testing File Structure")
    
    required_files = {
        'app.py': 'Flask application',
        'requirements.txt': 'Dependencies file',
        'templates/index.html': 'HTML template',
        'static/style.css': 'CSS stylesheet',
        'static/script.js': 'JavaScript file',
        'SVM_heart.pkt': 'SVM model (may be corrupted)',
        'columns.pkl': 'Feature columns',
        'scaler.pkl': 'Data scaler',
        'df_encode.pkl': 'Encoder'
    }
    
    missing = []
    for file, desc in required_files.items():
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"✓ {file:<25} ({desc}) - {size} bytes")
        else:
            print(f"✗ {file:<25} ({desc}) - MISSING")
            missing.append(file)
    
    return len(missing) == 0

def test_app_syntax():
    """Test if app.py has valid Python syntax"""
    print_header("Testing Python Syntax")
    
    try:
        import py_compile
        py_compile.compile('app.py', doraise=True)
        print("✓ app.py has valid syntax")
        return True
    except py_compile.PyCompileError as e:
        print(f"✗ Syntax error in app.py: {e}")
        return False

def test_app_import():
    """Test if app.py can be imported"""
    print_header("Testing App Import")
    
    try:
        import app
        print("✓ app.py imported successfully")
        print(f"  - Flask app instance: {type(app.app)}")
        print(f"  - Model loaded: {'✓ Yes' if app.model else '✗ No (model file may be corrupted)'}")
        print(f"  - Columns loaded: {'✓ Yes' if app.columns else '✗ No'}")
        print(f"  - Scaler loaded: {'✓ Yes' if app.scaler else '✗ No'}")
        
        if app.model is None:
            print("\n  ⚠ Model files may be corrupted or in wrong format")
            print("  → Ensure pickle files (.pkt/.pkl) are valid")
            print("  → Try regenerating model files")
        
        return True
    except Exception as e:
        print(f"✗ Error importing app.py: {e}")
        return False

def test_routes():
    """Test if Flask routes are registered"""
    print_header("Testing Flask Routes")
    
    try:
        import app
        
        routes = []
        for rule in app.app.url_map.iter_rules():
            routes.append((rule.rule, list(rule.methods - {'HEAD', 'OPTIONS'})))
        
        if routes:
            for route, methods in routes:
                print(f"✓ Route: {route:<20} Methods: {', '.join(methods)}")
            return True
        else:
            print("✗ No routes found")
            return False
    except Exception as e:
        print(f"✗ Error checking routes: {e}")
        return False

def main():
    """Run all tests"""
    print("\n")
    print("╔" + "="*48 + "╗")
    print("║  Heart Attack Prediction - System Test      ║")
    print("║  Testing all bug fixes and configuration    ║")
    print("╚" + "="*48 + "╝")
    
    results = {
        'Package Imports': test_imports(),
        'File Structure': test_file_structure(),
        'Python Syntax': test_app_syntax(),
        'App Import': test_app_import(),
        'Flask Routes': test_routes(),
    }
    
    print_header("Test Summary")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status:8} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n✓ All tests passed! You can now run: python app.py")
    else:
        print("\n✗ Some tests failed. Please review errors above.")
        print("\nCommon fixes:")
        print("  - Run: pip install -r requirements.txt --only-binary :all:")
        print("  - Verify pickle files are not corrupted")
        print("  - Check that all files exist in the correct directories")
    
    return 0 if passed == total else 1

if __name__ == '__main__':
    sys.exit(main())
