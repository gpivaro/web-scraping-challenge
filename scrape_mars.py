### Import Dependencies
import os
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
import time


def scrape():
    # Setup configuration variables to enable Splinter to interact with browser
    driverPath = ["/usr/local/bin/chromedriver"]  # For MacBook
    executable_path = {"executable_path": driverPath[0]}
    browser = Browser("chrome", **executable_path, headless=True)

    # Create a empty dictionary to store the data
    scraped_data = {}

    ######################     NASA  ########################
    # URL of page to be scraped
    url_nasa = "https://mars.nasa.gov/news/"

    # Use the browser to visit the url
    browser.visit(url_nasa)

    # Wait for 5 seconds for error purpouses to load the page
    time.sleep(5)

    # Return the rendered page by the browser
    html_nasa = browser.html

    # Use beatifulsoup to scrap the page rendered by the browser
    soup = BeautifulSoup(html_nasa, "html.parser")

    # Search for the div where the title is located
    results = soup.find_all("div", class_="content_title")
    news_title = results[1].text
    # print(f"Title: {news_title}")

    # Search for the div where the paragraph news is located
    results = soup.find_all("div", class_="article_teaser_body")
    new_p = results[0].text
    # print(f"Paragraph: {new_p}")

    # Save the scraped data to an entry of the dictionary
    scraped_data["Title"] = news_title
    scraped_data["Paragraph"] = new_p

    ################## JPL Mars Space Images - Featured Image  ##################
    # URL for JPL Nasa websit
    url_jpl = "https://www.jpl.nasa.gov"

    # The url for JPL Featured Space Image
    space_images = "/spaceimages/?search=&category=Mars"

    # Full url
    url_jpl_space_images = f"{url_jpl}{space_images}"

    # Use the browser to visit the url
    browser.visit(url_jpl_space_images)

    # Use beatifulsoup to scrap the page rendered by the browser
    html_jpl = browser.html
    soup = BeautifulSoup(html_jpl, "html.parser")

    # Featured image is in the div class="carousel_container"
    results = soup.find("div", class_="carousel_container")

    # Find the article
    article = results.find("article")

    # Grab the style string and split
    style = article["style"].split("(")

    # Retrieve the url strig location
    image_location = style[1].split(")")[0][1:-1]

    # Compose the full url of the image
    featured_image_url = f"{url_jpl}{image_location}"

    # Save the scraped data to an entry of the dictionary
    scraped_data["ImageURL"] = featured_image_url

    ################## Mars Facts ##################
    # URL
    url_mars_facts = "https://space-facts.com/mars/"

    # Use Pandas to automatically scrape any tabular data from a page.
    tables = pd.read_html(url_mars_facts)

    # Select the intended table
    table_facts = tables[0]

    # Rename the table colums
    table_facts.rename(columns={0: "Ind", 1: "Data"}, inplace=True)

    # Rename the table colums
    table_facts = table_facts.set_index("Ind")

    # Save the scraped data to an entry of the dictionary
    scraped_data["TableHTML"] = table_facts.to_html()

    ################# Mars Hemispheres #################
    # URL
    url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Use the browser to visit the url
    browser.visit(url_mars_hemispheres)

    # Splinter can capture a page's underlying html and use pass it to BeautifulSoup to allow us to scrape the content
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # By analyzing the page we can find that the images are in a div class='description'
    results = soup.find_all("div", class_="description")

    # Create a list with the name of the hemispheres
    list_hemispheres = []
    for i in range(len(results)):
        list_hemispheres.append(results[i].a.h3.text)

    hemisphere_image_urls = []

    # Create a list of dictionaries for each hemisphere
    for i in range(len(list_hemispheres)):

        # Use the browser to visit the url
        browser.click_link_by_partial_text(list_hemispheres[i])

        # Splinter can capture a page's underlying html and use pass it to BeautifulSoup to allow us to scrape the content
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")

        # By analyzing the page we can find that the images link are in a li
        results_new = soup.find_all("li")

        # Append the dictionary with the image url string and the hemisphere title to a list.
        for n in range(len(results_new)):
            if results_new[n].a.text == "Sample":
                hemisphere_image_urls.append(
                    {
                        "title": list_hemispheres[i].replace(
                            "Hemisphere Enhanced", "Hemisphere"
                        ),
                        "img_url": results_new[0].a["href"],
                    }
                )

        # Use the browser to visit the url
        browser.visit(url_mars_hemispheres)

    # Save the scraped data to an entry of the dictionary
    scraped_data["ListImages"] = hemisphere_image_urls

    # When you’ve finished testing, close your browser using browser.quit:
    browser.quit()

    return scraped_data
