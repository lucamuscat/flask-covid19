from flask import Flask, render_template, url_for
from stats import stats

app = Flask(__name__)
stats = stats()


@app.route("/")
def index():
    if stats.expired(minutes=1):
        stats.refresh()

    percentage_infected = (float(stats.corona.get('total_cases')) /
                           stats.population.get('population')*100)

    return render_template(
        "index.html",
        corona_data=stats.corona,
        population_data=stats.population,
        percentage_infected=percentage_infected,
        last_updated=stats.last_updated_time
    )


if __name__ == "__main__":
    app.run()
