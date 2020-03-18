from requests_html import HTMLSession


def odometer_stats(url, table_id, country="Malta"):
    session = HTMLSession()
    try:
        r = session.get(url)
        table = r.html.find(f"{table_id} > tbody > tr")
        country_stats = [tr.find("td")
                         for tr in table if country in tr.text][0]
        return country_stats
    except Exception:
        print("No internet")
