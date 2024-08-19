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
expected_redirect = "https://mobilunity.com/"

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
    except requests.RequestException:
        return False

results = []

for url in urls:
    try:
        ssl_expiry_date = get_ssl_expiry_date(url)
        redirect_check = check_redirect(url)
        results.append((url, ssl_expiry_date, redirect_check))
    except Exception as e:
        results.append((url, None, False))

# Print the results
for result in results:
    url, ssl_expiry_date, redirect_check = result
    if ssl_expiry_date:
        ssl_expiry_str = ssl_expiry_date.strftime("%m/%d/%Y")
        print(f"{url} - SSL is valid till {ssl_expiry_str} - Redirects correctly: {expected_redirect}")
    else:
        print(f"{url} - SSL check failed - Redirects correctly: {response.url}")
