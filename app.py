from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo

# From the separate python file in this directory, we'll import the code that is used to scrape craigslist
from scrape_mars import scrape


# Next, create a route called /scrape that will import your scrape_mars.py script and call your scrape function.

# Store the return value in Mongo as a Python dictionary.
# Create a root route / that will query your Mongo database and pass the mars data into an HTML template to display the data.

