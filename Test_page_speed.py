import requests
import json


def get_page_speed_insights(api_key, url, strategy='desktop'):
    endpoint = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed'
    params = {
        'url': url,
        'key': api_key,
        'strategy': strategy,
        'category': ['performance', 'accessibility', 'best-practices', 'seo']
    }

    response = requests.get(endpoint, params=params)

    if response.status_code != 200:
        print("Error fetching PageSpeed Insights data:", response.text)
        return None

    return response.json()


def main():
    api_key = 'AIzaSyACMG-1IITbJP8j3o38AlGzQSFN9AN2wRY'
    url = 'https://www.hiredynamicsdevelopers.com/'

    report = get_page_speed_insights(api_key, url)

    if report:
        try:
            lighthouse_result = report['lighthouseResult']
            performance_score = lighthouse_result['categories']['performance']['score'] * 100
            accessibility_score = lighthouse_result['categories']['accessibility']['score'] * 100
            best_practices_score = lighthouse_result['categories']['best-practices']['score'] * 100
            seo_score = lighthouse_result['categories']['seo']['score'] * 100

            print(f"Report is done for {url}")
            print(f"Performance score: {performance_score}")
            print(f"Accessibility score: {accessibility_score}")
            print(f"Best Practices score: {best_practices_score}")
            print(f"SEO score: {seo_score}")
        except KeyError as e:
            print(f"Key error: {e}. The response structure might have changed.")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("PageSpeed Insights report could not be generated.")


if __name__ == "__main__":
    main()
