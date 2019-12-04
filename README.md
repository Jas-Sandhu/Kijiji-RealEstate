# Kijiji-RealEstate
Data Science project centered around the Toronto rental market.

This repository is a work in progress.

The first goal is to extract rental market data from Kijiji in a clean and modular way.

The second goal is to analyze and visualize the data to draw insights using either R or Python.

MOST RECENT CHANGES:

Mapping.py - Contains a mapping of different cities and their corresponding URL on Kijiji.

Retrieve.py - Contains various functions that pull specific pieces of information from each posting in a city (postal code, rent, number of rooms, etc.

RealEstate.py - Iterates through every posting on a page and call on Mapping.py to retrieve the correct URL and Retrieve.py to extract data.

Kijiji.py is the main module that needs to be executed in order to obtain the desired results.
You'll need to update some of the variables in that module in order specify the correct file path, city and number of pages to parse.
The final output is a csv file containing real estate data for a particular market.
