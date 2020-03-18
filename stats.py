from scraper import corona
from scraper import population
from time import time
from datetime import timedelta
from datetime import datetime


class stats():
    def __init__(self, country="Malta"):
        self.country = country
        self.corona = corona(self.country)
        self.population = population(self.country)
        self.last_updated_epoch = time()
        self.last_updated_time = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S")

    def expired(self, minutes):
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
