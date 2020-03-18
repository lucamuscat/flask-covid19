from flask import Flask, render_template, url_for
from stats import stats

app = Flask(__name__)
initial_stats = stats()


@app.route("/")
def index():
    if initial_stats.expired(minutes=1):
        initial_stats.refresh()

    return render_template(
        "index.html",
        corona_data=initial_stats.corona.get("Malta"),
        population_data=initial_stats.population.get("Malta"),
        last_updated=initial_stats.last_updated_time,
        country="Malta"
    )


@app.route("/Country/<country>")
def country(country):
    if initial_stats.expired(minutes=5):
        initial_stats.refresh()

    print(country)

    return render_template(
        "index.html",
        corona_data=initial_stats.corona.get(country),
        population_data=initial_stats.population.get(country),
        last_updated=initial_stats.last_updated_time,
        country=str(country)
    )


if __name__ == "__main__":
    app.run()
