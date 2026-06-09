import urllib.request

def test_endpoint(url):
    try:
        with urllib.request.urlopen(url) as response:
            return response.status, response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode('utf-8')
    except Exception as e:
        return 500, str(e)

def main():
    status, body = test_endpoint("http://localhost:8080/api/courses")
    print(f"Status: {status}")
    print("Response Body:")
    print(body[:2000])

if __name__ == "__main__":
    main()
