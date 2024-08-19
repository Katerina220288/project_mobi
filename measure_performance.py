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
        print(f"Error fetching PageSpeed Insights data for {strategy}:", response.text)
        return None

    return response.json()


def extract_scores(report):
    try:
        lighthouse_result = report['lighthouseResult']
        scores = {
            'performance': lighthouse_result['categories']['performance']['score'] * 100,
            'accessibility': lighthouse_result['categories']['accessibility']['score'] * 100,
            'best_practices': lighthouse_result['categories']['best-practices']['score'] * 100,
            'seo': lighthouse_result['categories']['seo']['score'] * 100,
        }
        return scores
    except KeyError as e:
        print(f"Key error: {e}. The response structure might have changed.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
