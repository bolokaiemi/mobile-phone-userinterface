import urllib.request
import json
import sys

def verify_courses():
    print("Testing connection to Flask Server on http://localhost:8080/api/courses...")
    try:
        req = urllib.request.Request("http://localhost:8080/api/courses")
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            print("SUCCESS: /api/courses returned status code 200.")
            courses = data.get('courses', [])
            print(f"Total Courses retrieved: {len(courses)}")
            
            # Print courses details
            for course in courses:
                print(f"- [{course.get('badge')}] {course.get('title')}: {course.get('meta')}")
                
            assert len(courses) == 5, "Should have 5 courses!"
            assert courses[0]['id'] == 'html5', "First course should be HTML5!"
            print("\nALL COURSES TESTS PASSED SUCCESSFULLY!")
    except Exception as e:
        print("FAILED: /api/courses endpoint error:", e)
        sys.exit(1)

if __name__ == "__main__":
    verify_courses()
