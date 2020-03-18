from odometer import odometer_stats
from datetime import datetime
from time import time


def corona(country="Malta"):
    url = "https://www.worldometers.info/coronavirus/"
    table_id = "#main_table_countries_today"
    data = odometer_stats(url, table_id, country)
    results = dict()

    labels = ["total_cases", "new_cases", "total_deaths", "new_deaths"]

    # Each label is represented by the index created by the enumeration.
    for index, value in enumerate(labels, start=1):
        text = data[index].text if data[index].text != "" else "None"
        results[value] = text

    return results


def population(country="Malta"):
    url = "https://www.worldometers.info/world-population/population-by-country/"
    population_table_id = "#example2"
    population_results = dict()
    data = odometer_stats(
        url, population_table_id, country)
    population_results["population"] = int(data[2].text.replace(",", ""))
    return population_results


def update_current_time(dictionary):
    dictionary["time_str"] = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S")
    dictionary["time_epoch"] = time()
