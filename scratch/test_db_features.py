import urllib.request
import json
import sys

def run_tests():
    print("Testing connection to Flask Server on http://localhost:8080...")
    
    # 1. Test stats endpoint
    try:
        req = urllib.request.Request("http://localhost:8080/api/admin/stats")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("SUCCESS: /api/admin/stats returned status code 200.")
            print("Database File Path on Host:", data.get('db_path'))
            print("Total Reviews:", data.get('total_reviews'))
            print("Total Students:", data.get('total_students'))
    except Exception as e:
        print("FAILED: /api/admin/stats endpoint error:", e)
        sys.exit(1)
        
    # 2. Test database download endpoint
    try:
        req = urllib.request.Request("http://localhost:8080/api/admin/db-download")
        with urllib.request.urlopen(req) as response:
            content = response.read()
            print(f"SUCCESS: /api/admin/db-download returned {len(content)} bytes of ebiui.db.")
            assert len(content) > 0, "Downloaded database file is empty!"
    except Exception as e:
        print("FAILED: /api/admin/db-download endpoint error:", e)
        sys.exit(1)
        
    # 3. Test CORS preflight OPTIONS request
    try:
        req = urllib.request.Request(
            "http://localhost:8080/api/comments",
            method="OPTIONS"
        )
        req.add_header("Origin", "http://localhost:63342")
        req.add_header("Access-Control-Request-Method", "POST")
        req.add_header("Access-Control-Request-Headers", "Content-Type")
        
        with urllib.request.urlopen(req) as response:
            headers = dict(response.headers)
            print("SUCCESS: CORS Preflight OPTIONS returned 200.")
            print("Access-Control-Allow-Origin:", headers.get("Access-Control-Allow-Origin"))
            print("Access-Control-Allow-Credentials:", headers.get("Access-Control-Allow-Credentials"))
            
            assert headers.get("Access-Control-Allow-Origin") == "http://localhost:63342", "CORS Origin did not echo correctly!"
            assert headers.get("Access-Control-Allow-Credentials") == "true", "CORS Credentials not allowed!"
    except Exception as e:
        print("FAILED: CORS Preflight OPTIONS error:", e)
        sys.exit(1)
        
    print("\nALL AUTOMATED TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
