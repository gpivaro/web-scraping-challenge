# Web Scraping Homework - Mission to Mars

### Rice University Data Analytics and Visualization Boot Camp 2020


This repository contains a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The overview of the project is the outlined below.


## Step 1 - Scraping

The initial scraping uses Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter.

* The [Jupyter Notebook](mission_to_mars.ipynb) file contains all the scraping and analysis tasks. The following outlines what will be scraped.

### NASA Mars News

* Scrape the [NASA Mars News Site](https://mars.nasa.gov/news/) and collect the latest News Title and Paragraph Text.


### JPL Mars Space Images - Featured Image

* Visit the url for JPL Featured Space Image [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.


### Mars Facts

* Visit the Mars Facts webpage [here](https://space-facts.com/mars/) and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. Use Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) to obtain high resolution images for each of Mar's hemispheres.

* We will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.

* Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data.

* Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.


- - -

## Step 2 - MongoDB and Flask Application

Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* Start by converting the Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all the scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, create a route called `/scrape` that will import the `scrape_mars.py` script and call the `scrape` function.

  * Store the return value in Mongo as a Python dictionary.

* Create a root route `/` that will query the Mongo database and pass the mars data into an HTML template to display the data.

* Create a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 
## Hints

* Use Splinter to navigate the sites when needed and BeautifulSoup to help find and parse out the necessary data.

* Use Pymongo for CRUD applications for the database. For the inital version of this applicaiton, we will simply overwrite the existing document each time the `/scrape` url is visited and new data is obtained.

* Use Bootstrap to structure the HTML template.