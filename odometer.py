from requests_html import HTMLSession


def odometer_stats(url, table_id, country="Malta"):
    """
    Currently deprecated.
    """
    try:
        session = HTMLSession()
        r = session.get(url)
        table = r.html.find(f"{table_id} > tbody > tr")
        country_stats = [tr.find("td")
                         for tr in table if country in tr.text][0]
        return country_stats
    except Exception:
        print("No internet")


def odometer_stats_global(url, table_id):
    """
    Returns an array of tr elements. Each column can be extracted using
    tr.find(td) (tr being an individual element of the returned iterable)

    Keyword arguments:

    url -- Url to the specific odometer website

    table_id -- Id of the table in which the data is contained.
    """
    try:
        session = HTMLSession()
        r = session.get(url)
        table = r.html.find(f"{table_id} > tbody > tr")
        return table
    except Exception as ex:
        print(ex)
