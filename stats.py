from scraper import corona
from scraper import population
from time import time
from datetime import timedelta
from datetime import datetime


class stats():
    def __init__(self):
        self.corona = corona()
        self.population = population()
        self.countries = self.corona.keys()
        self.last_updated_epoch = time()
        self.last_updated_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S")

    def expired(self, minutes):
        """
        Returns a boolean which checks if the data in the class is older than
        the parameter minutes.

        Keyword arguments:
        minutes -- The number of minutes needed for the data to be considered
        "expired"
        """
        current_time = time()
        initial_time = self.last_updated_epoch
        delta_time = current_time - initial_time
        # The threshold is recorded in minutes
        threshold = timedelta(minutes=minutes).total_seconds()
        return delta_time >= threshold

    def refresh(self):
        self.corona = corona()
        self.population = population()
        self.last_updated_epoch = time()
        self.last_updated_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S")
