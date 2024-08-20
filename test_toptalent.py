import ssl
import socket
from datetime import datetime
import requests
import pytest

# List of URLs to check
urls = [
    "mobilunity-talent.com",
    "mobilunity-proposal.com",
    "mobilunity-tech.com",
    "mobilunity.biz",
    "mobilunity.net",
    "mobilunity.org",
    "mobilunity.info",
    "mobilunity.co"
]

# Expected redirect URL
expected_redirect = "https://mobilunity.com"

def get_ssl_expiry_date(hostname):
    context = ssl.create_default_context()
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            expiry_date_str = cert['notAfter']
            expiry_date = datetime.strptime(expiry_date_str, "%b %d %H:%M:%S %Y %Z")
            return expiry_date

def check_redirect(url):
    try:
        response = requests.get(f"http://{url}", allow_redirects=True)
        return response.url == expected_redirect
    except requests.RequestException as e:
        print(f"Request failed for {url} with exception {e}")
        return False

@pytest.mark.parametrize("url", urls)
def test_ssl_expiry(url):
    try:
        ssl_expiry_date = get_ssl_expiry_date(url)
        assert ssl_expiry_date is not None, f"SSL check failed for {url}"
        print(f"{url} - SSL is valid till {ssl_expiry_date.strftime('%m/%d/%Y')}")
    except Exception as e:
        pytest.fail(f"SSL check failed for {url} with exception {e}")

@pytest.mark.parametrize("url", urls)
def test_redirect(url):
    try:
        redirect_check = check_redirect(url)
        assert redirect_check, f"{url} does not redirect to {expected_redirect}"
        print(f"{url} - Redirects correctly to {expected_redirect}")
    except Exception as e:
        pytest.fail(f"Redirect check failed for {expected_redirect} with exception {e}")

if __name__ == "__main__":
    pytest.main()
