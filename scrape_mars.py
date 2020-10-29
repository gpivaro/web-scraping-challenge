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

    ######################     NASA  ########################
    # URL of page to be scraped
    # url_nasa = "https://mars.nasa.gov/news/"
    url_nasa = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    # Use the browser to visit the url
    browser.visit(url_nasa)

    # Return the rendered page by the browser
    html_nasa = browser.html

    # Use beatifulsoup to scrap the page rendered by the browser
    soup = BeautifulSoup(html_nasa, "html.parser")

    # Wait for 300 milliseconds for error purpouses
    # .3 can also be used
    time.sleep(5)

    # Search for the div where the title is located
    results = soup.find_all("div", class_="content_title")
    news_title = results[1].text
    # print(f"Title: {news_title}")

    # Search for the div where the paragraph news is located
    results = soup.find_all("div", class_="article_teaser_body")
    new_p = results[0].text
    # print(f"Paragraph: {new_p}")

    # Create a dictionary with the scraped data
    Nasa_News = {"Title": news_title, "Paragraph": new_p}
    # Nasa_News

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
    # print(results)

    # Find the article
    article = results.find("article")

    # Grab the style string and split
    style = article["style"].split("(")

    # Retrieve the url strig location
    image_location = style[1].split(")")[0][1:-1]

    # Compose the full url of the image
    featured_image_url = f"{url_jpl}{image_location}"
    # print(featured_image_url)

    # Create a dictionary with the scraped data
    JPL = {"ImageURL": featured_image_url}
    # JPL

    ################## Mars Facts ##################
    # URL
    url_mars_facts = "https://space-facts.com/mars/"

    # Use Pandas to automatically scrape any tabular data from a page.
    tables = pd.read_html(url_mars_facts)

    # Select the intended table
    table_facts = tables[0]
    html_table = table_facts.to_html()
    # print(html_table)
    # table_facts.to_html('table.html')

    # Create a dictionary with the scraped data
    MarsFacts = {"TableHTML": html_table}
    # MarsFacts

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
            if results_new[n].a.text == "Original":
                hemisphere_image_urls.append(
                    {
                        "title": list_hemispheres[i].replace(
                            "Hemisphere Enhanced", "Hemisphere"
                        ),
                        "img_url": results_new[1].a["href"],
                    }
                )

        # Use the browser to visit the url
        browser.visit(url_mars_hemispheres)

    # Create a dictionary with the scraped data
    USGS = {"ListImages": hemisphere_image_urls}
    USGS

    # When you’ve finished testing, close your browser using browser.quit:
    browser.quit()

    # Create a list of all dictionaries with the scraped data
    scraped_data = [Nasa_News, JPL, MarsFacts, USGS]

    return scraped_data


# data = scrape()
# print()
# print()
# print(data)
# print()
