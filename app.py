from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo

# From the separate python file in this directory,
# we'll import the code that is used to scrape the pages
from scrape_mars import scrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_mission_scraping"
mongo = PyMongo(app)

# identify the collection
mars_data = mongo.db.mars_data
# mars_data.drop()

# Render the index.html page with any craigslist listings in our database.
# If there are no listings, the table will be empty.
@app.route("/")
def index():
    mars_info = mars_data.find_one()

    return render_template("index.html", data_db=mars_info)


# This route will trigger the webscraping, but it will then
# send us back to the index route to render the results
@app.route("/scrape")
def scraper():

    # drop collection
    mars_data.drop()

    # scrape_craigslist.scrape() is a custom function that
    # we've defined in the scrape_mars.py file within this directory
    scraped_data = scrape()
    mars_data.insert_many([scraped_data])

    # Use Flask's redirect function to send us to a
    # different route once this task has completed.
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
