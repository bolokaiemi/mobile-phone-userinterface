import urllib.request
import json

def test_endpoint(url):
    try:
        with urllib.request.urlopen(url) as response:
            status = response.status
            body = response.read().decode('utf-8')
            return status, json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')
    except Exception as e:
        return 500, str(e)

def main():
    print("=== VERIFYING LIVE SERVER ENDPOINTS ===")
    
    # 1. /api/courses
    status, res = test_endpoint("http://localhost:8080/api/courses")
    print(f"GET /api/courses -> Status: {status}")
    if status == 200:
        print(f"  Success! Found {len(res.get('courses', []))} courses.")
        
    # 2. /api/admin/stats
    status, res = test_endpoint("http://localhost:8080/api/admin/stats")
    print(f"GET /api/admin/stats -> Status: {status}")
    if status == 200:
        print(f"  Success! Stats: {res}")
        
    # 3. /api/comments
    status, res = test_endpoint("http://localhost:8080/api/comments")
    print(f"GET /api/comments -> Status: {status}")
    if status == 200:
        print(f"  Success! Found {len(res.get('comments', []))} comments.")

if __name__ == "__main__":
    main()
