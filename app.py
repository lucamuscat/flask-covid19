from flask import Flask, render_template, url_for
from stats import stats

app = Flask(__name__)
initial_stats = stats("Malta")


@app.route("/")
def index():
    if initial_stats.expired(minutes=1):
        initial_stats.refresh()

    percentage_infected = (float(initial_stats.corona.get('total_cases')) /
                           initial_stats.population.get('population')*100)

    return render_template(
        "index.html",
        corona_data=initial_stats.corona,
        population_data=initial_stats.population,
        percentage_infected=percentage_infected,
        last_updated=initial_stats.last_updated_time,
        country=initial_stats.country
    )


@app.route("/<country>")
def country(country):
    temp = stats(country)

    percentage_infected = (float(temp.corona.get('total_cases')) /
                           temp.population.get('population')*100)

    return render_template(
        "index.html",
        corona_data=temp.corona,
        population_data=temp.population,
        percentage_infected=percentage_infected,
        last_updated=temp.last_updated_time,
        country=temp.country
    )


if __name__ == "__main__":
    app.run()
