# Web-Scraper-fallingrain
Web Scraper to prepare a CSV file containing State, City, Latitude, Longitude, Elevation, Estimated Population.
Website_url='http://www.fallingrain.com/world/IN/'

This is a web scraper that implements Depth First traversal using a stack to collect the required information.

Libraries used:
os.path, pandas, requests, bs4 from BeautifulSoup4, time.

First, urls for all the states are collected in a list.
These urls are scraped iteratively using a Depth First Traversal implemented using a stack which stores sub-links present inside each state url.
After reaching the base of each url, beautifulsoup4 is used to extract the final table.
Note: 
(a) Final table in each hierarchy is recognised to either have attribute border=2 or is the second table on the page having a map.
Collected data is manipulated as required and appended to a csv file.
(b) Please open the csv file using link: https://raw.githubusercontent.com/Prayas1997/web-scraper-fallingrain/master/India.csv in your browser(preferrably Google Chrome) or download it and open with Libre office. This is because India.csv contains names written in regional languages and Microsoft Excel messes those names with different encodings.


********* IMPORTANT!!! **********
1). I've added 0.1 sec delay into the code before any new page is fetched from server. This is done so that the server does not block the script by closing connection suspecting an attack. The script does not get stuck in an infinite loop at any point of time. It takes time to process states with large no. of places. For example, Andhra Pradesh has around 30,200 places. Total running time for the script is 2+hrs on an intel i5 4th gen laptop processor and 4GB RAM. 

2). Inorder to provide for easy analysis of data, rows having any field as NAN are removed.
