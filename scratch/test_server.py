import urllib.request
import json
import urllib.error
from http.cookiejar import CookieJar

def run_integration_test():
    base_url = "http://localhost:8080"
    
    # Set up a cookie processor to handle the session cookie across requests
    cj = CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    urllib.request.install_opener(opener)

    print("=== STARTING API INTEGRATION TEST ===")
    
    # 1. Register a test user
    print("\n1. Testing User Registration (/api/register)...")
    register_data = json.dumps({
        "username": "tester",
        "password": "password123"
    }).encode('utf-8')
    
    req = urllib.request.Request(
        f"{base_url}/api/register", 
        data=register_data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            print("Registration Status:", response.status)
            print("Response:", res_data)
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8')
        print("Registration Error:", e.code, body)
        if "already taken" in body:
            print("User already exists, proceeding to login instead...")
        else:
            return

    # 2. Login the test user (if registration was already done previously)
    print("\n2. Testing User Login (/api/login)...")
    login_data = json.dumps({
        "username": "tester",
        "password": "password123"
    }).encode('utf-8')
    req = urllib.request.Request(
        f"{base_url}/api/login",
        data=login_data,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Login Status:", response.status)
        print("Response:", res_data)

    # 3. Check current user
    print("\n3. Checking Session User (/api/user)...")
    req = urllib.request.Request(f"{base_url}/api/user")
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Session Status:", response.status)
        print("User:", res_data)

    # 4. Post a comment
    print("\n4. Posting a Comment (/api/comments)...")
    comment_data = json.dumps({
        "text": "Hello, EbiUI feedback! This is a test comment."
    }).encode('utf-8')
    req = urllib.request.Request(
        f"{base_url}/api/comments",
        data=comment_data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Post Comment Status:", response.status)
        print("Response:", res_data)
        comment_id = res_data['comment']['id']

    # 5. Fetch all comments
    print("\n5. Listing Comments (/api/comments)...")
    req = urllib.request.Request(f"{base_url}/api/comments")
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("List Status:", response.status)
        print("Comments list:")
        for c in res_data['comments']:
            print(f" - [{c['id']}] {c['username']}: {c['text']}")

    # 6. Delete the comment
    print(f"\n6. Deleting Comment ID {comment_id} (/api/comments/{comment_id})...")
    req = urllib.request.Request(
        f"{base_url}/api/comments/{comment_id}",
        method="DELETE"
    )
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Delete Status:", response.status)
        print("Response:", res_data)

    # 7. List comments again to verify deletion
    print("\n7. Listing Comments after Deletion (/api/comments)...")
    req = urllib.request.Request(f"{base_url}/api/comments")
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("List Status:", response.status)
        print("Comments remaining count:", len(res_data['comments']))

    # 8. Logout
    print("\n8. Logging Out (/api/logout)...")
    req = urllib.request.Request(f"{base_url}/api/logout", method="POST")
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Logout Status:", response.status)
        print("Response:", res_data)

    # 9. Verify session is cleared
    print("\n9. Checking Session User after Logout (/api/user)...")
    req = urllib.request.Request(f"{base_url}/api/user")
    with urllib.request.urlopen(req) as response:
        res_data = json.loads(response.read().decode('utf-8'))
        print("Session Status:", response.status)
        print("User:", res_data)

    print("\n=== INTEGRATION TEST COMPLETE ===")

if __name__ == "__main__":
    run_integration_test()
