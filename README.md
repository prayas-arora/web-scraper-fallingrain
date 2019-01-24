# Web-Scraper-fallingrain
Web Scraper to prepare a CSV file containing State, City, Latitude, Longitude, Elevation, Estimated Population.
 Website_url='http://www.fallingrain.com/world/IN/'

This is a web scraper that implements Depth First Search using a stack to collect the required information.

Libraries used:
os.path, pandas, requests, bs4 from BeautifulSoup4

First, urls for all the states are collected in a list.
These urls are scraped iteratively using a Depth First Search. DFS is implemented using a stack which stores sub-links inside each state url.
After reaching the base of each url, beautifulsoup4 is used to extract the required table.
Collected data is manipulated as required and appended to a csv file.
