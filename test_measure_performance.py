import pytest
from measure_performance import get_page_speed_insights, extract_scores

@pytest.fixture
def api_key():
    return 'AIzaSyACMG-1IITbJP8j3o38AlGzQSFN9AN2wRY'

@pytest.fixture
def sites():
    return [
        ('Hire Dynamics Developers', 'https://www.hiredynamicsdevelopers.com/'),
        ('SF Recruiters', 'https://www.sf-recruiters.com/'),
        ('SF Staffing Agency', 'https://www.sfstaffingagency.com/')
    ]

@pytest.fixture
def desktop_reports(api_key, sites):
    reports = []
    for name, url in sites:
        report = get_page_speed_insights(api_key, url, 'desktop')
        reports.append((name, report))
    return reports

@pytest.fixture
def mobile_reports(api_key, sites):
    reports = []
    for name, url in sites:
        report = get_page_speed_insights(api_key, url, 'mobile')
        reports.append((name, report))
    return reports

def test_desktop_scores(desktop_reports):
    for site_name, desktop_report in desktop_reports:
        assert desktop_report is not None, f"Desktop report for {site_name} could not be generated."
        scores = extract_scores(desktop_report)
        assert scores is not None, f"Could not extract scores from desktop report for {site_name}."
        print(f"\nDesktop Report for {site_name}")
        print(f"Performance score: {scores['performance']}")
        print(f"Accessibility score: {scores['accessibility']}")
        print(f"Best Practices score: {scores['best_practices']}")
        print(f"SEO score: {scores['seo']}")

def test_mobile_scores(mobile_reports):
    for site_name, mobile_report in mobile_reports:
        assert mobile_report is not None, f"Mobile report for {site_name} could not be generated."
        scores = extract_scores(mobile_report)
        assert scores is not None, f"Could not extract scores from mobile report for {site_name}."
        print(f"\nMobile Report for {site_name}")
        print(f"Performance score: {scores['performance']}")
        print(f"Accessibility score: {scores['accessibility']}")
        print(f"Best Practices score: {scores['best_practices']}")
        print(f"SEO score: {scores['seo']}")
