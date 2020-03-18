from odometer import odometer_stats_global
from datetime import datetime
from time import time


def corona():
    """
    Scrapes COVID-19 related data and returns a dictionary containing
    the countries name as the key and another dictionary as a value which
    contains the following  keys:

    total_cases: Total number of cases in respective country.

    new_cases: Total number of new cases in respective country(string)

    total_deaths: Total number of deaths in the respective country

    new_deaths: Deaths which have occured on the current day
    """
    url = "https://www.worldometers.info/coronavirus/"
    table_id = "#main_table_countries_today"
    data = odometer_stats_global(url, table_id)
    results = dict()

    labels = ["total_cases", "new_cases", "total_deaths", "new_deaths"]

    # Each label is represented by the index created by the enumeration.
    for i in data:
        current = i.find("td")
        country = current[0].text
        temp_dict = dict()
        for index, value in enumerate(labels, start=1):
            temp_dict[value] = current[index].text if current[index].text != "" else "None"
        results[country] = temp_dict

    return results


def population():
    url = "https://www.worldometers.info/world-population/population-by-country/"
    population_table_id = "#example2"
    population_results = dict()
    data = odometer_stats_global(url, population_table_id)
    for tr in data:
        current = tr.find("td")
        country_name = current[1].text
        population_count = int(current[2].text.replace(",", ""))
        population_results[country_name] = population_count
    return population_results


def update_current_time(dictionary: dict):
    dictionary["time_str"] = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S")
    dictionary["time_epoch"] = time()
