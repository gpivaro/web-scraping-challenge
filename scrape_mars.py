### Import Dependencies
import os
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd


def scrape():

    scraped_data = {}

    # ### Setup Splinter
    # # identify location of chromedriver and store it as a variable
    # # driverPath = !which chromedriver
    # driverPath = ["/usr/local/bin/chromedriver"]

    # # Setup configuration variables to enable Splinter to interact with browser
    # executable_path = {"executable_path": driverPath[0]}
    # browser = Browser("chrome", **executable_path, headless=False)

    # ################################ NASA Mars News ###################################
    # ###################################################################################
    # # URL of page to be scraped
    # # url_nasa = "https://mars.nasa.gov/news/"
    # url_nasa = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    # #### Use splinter to inform the browser to visit the page
    # # Use the browser to visit the url
    # browser.visit(url_nasa)

    # # Use beatifulsoup to scrap the page rendered by the browser
    # html_nasa = browser.html
    # soup = BeautifulSoup(html_nasa, "html.parser")

    # # # Print the li that contatins the first headline
    # # results = soup.find("div", class_="content_title")
    # # # results = soup.find_all("div", class_="content_title")

    # # # Assign the text to variables that you can reference later
    # # # news_title = results.a.text
    # # news_title = results[1].text
    # # print(f"Title: {news_title}\n")

    # # results = soup.find("li", class_="slide")
    # # news_p = results.find("div", class_="article_teaser_body").text
    # # print(f"{news_p}")

    # # scraped_data["Nasa title"] = news_title
    # # scraped_data["Nasa par"] = news_p

    scraped_data["Nasa title"] = "Change This"
    scraped_data["Nasa par"] = "Test Test Test"

    # ##################### JPL Mars Space Images - Featured Image ######################
    # ###################################################################################
    # # URL for JPL Nasa websit
    # url_jpl = "https://www.jpl.nasa.gov"

    # # The url for JPL Featured Space Image
    # space_images = "/spaceimages/?search=&category=Mars"

    # # Full url
    # url_jpl_space_images = f"{url_jpl}{space_images}"

    # # Use the browser to visit the url
    # browser.visit(url_jpl_space_images)

    # # Use beatifulsoup to scrap the page rendered by the browser
    # html_jpl = browser.html
    # soup = BeautifulSoup(html_jpl, "html.parser")

    # # Featured image is in the div class="carousel_container"
    # results = soup.find("div", class_="carousel_container")

    # # Find the article
    # article = results.find("article")

    # # Grab the style string and split
    # style = article["style"].split("(")

    # # Retrieve the url strig location
    # image_location = style[1].split(")")[0][1:-1]

    # # Compose the full url of the image
    # featured_image_url = f"{url_jpl}{image_location}"
    # print(featured_image_url)

    # scraped_data["JPL image"] = featured_image_url

    # ############################ Mars Facts ###########################################
    # ###################################################################################
    # # URL
    # url_mars_facts = "https://space-facts.com/mars/"

    # # Use Pandas to automatically scrape any tabular data from a page.
    # tables = pd.read_html(url_mars_facts)

    # # Select the intended table
    # table_facts = tables[0]
    # html_table = table_facts.to_html()
    # print(html_table)
    # table_facts.to_html("table.html")

    # scraped_data["Mars table"] = html_table

    # ############################# Mars Hemispheres ####################################
    # ###################################################################################
    # # URL
    # url_mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # # Use the browser to visit the url
    # browser.visit(url_mars_hemispheres)

    # # Splinter can capture a page's underlying html and use pass it to BeautifulSoup to allow us to scrape the content
    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")

    # # By analyzing the page we can find that the images are in a div class='description'
    # results = soup.find_all("div", class_="description")

    # # Create a list with the name of the hemispheres
    # list_hemispheres = []
    # for i in range(len(results)):
    #     list_hemispheres.append(results[i].a.h3.text)

    # print(list_hemispheres)
    # hemisphere_image_urls = []

    # # Create a list of dictionaries for each hemisphere
    # for i in range(len(list_hemispheres)):

    #     # Use the browser to visit the url
    #     browser.click_link_by_partial_text(list_hemispheres[i])

    #     # Splinter can capture a page's underlying html and use pass it to BeautifulSoup to allow us to scrape the content
    #     html = browser.html
    #     soup = BeautifulSoup(html, "html.parser")

    #     # By analyzing the page we can find that the images link are in a li
    #     results_new = soup.find_all("li")

    #     # Append the dictionary with the image url string and the hemisphere title to a list.
    #     for n in range(len(results_new)):
    #         if results_new[n].a.text == "Original":
    #             hemisphere_image_urls.append(
    #                 {"title": list_hemispheres[i], "img_url": results_new[1].a["href"]}
    #             )

    #     # Use the browser to visit the url
    #     browser.visit(url_mars_hemispheres)

    # print(hemisphere_image_urls)

    # scraped_data["Mars Hemispheres"] = hemisphere_image_urls

    # When you’ve finished testing, close your browser using browser.quit:
    # browser.quit()

    return scraped_data


# data = scrape()
# print()
# print()
# print("-----------")
# print(data)
