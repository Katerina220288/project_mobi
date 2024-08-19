import requests

# List of URLs to check
urls = [
    "http://mobilunity-talent.com",
    "http://mobilunity-proposal.com",
    "http://mobilunity-tech.com",
    "http://mobilunity.biz",
    "http://mobilunity.net",
    "http://mobilunity.org",
    "http://mobilunity.info",
    "http://mobilunity.co"
]

# Expected redirect URL
expected_redirect = "https://mobilunity.com"

def check_redirect(url):
    try:
        response = requests.get(url, allow_redirects=True)
        if response.url == expected_redirect:
            print(f"{url} redirects correctly to {expected_redirect}")
        else:
            print(f"{url} does not redirect correctly. It redirects to {response.url}")
    except requests.RequestException as e:
        print(f"Failed to check {url}: {e}")

# Check each URL
for url in urls:
    check_redirect(url)
