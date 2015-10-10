# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 22:45:06 2015

@author: Eoghan
"""

import numpy as np #import numpy
import pandas as pd # import pandas
import sqlite3 # import sqlite

conn = sqlite3.connect('renewable.db')  # connect to the Database

location=("SELECT * FROM location;") # select all the columns from the 'location' table
ports=("SELECT * FROM ports;") # select all the columns from the 'ports'table

costs=[] #create an empty array 'costs'
locations=[] #create an empty array 'locations'
portslocation =[] #create an empty array 'portlocations'

df=pd.io.sql.read_sql(location,conn) # crate a dataframe named 'df' with the Pandas library 'read_sql' with location and conn as the parameters
df2=pd.io.sql.read_sql(ports,conn) # crate a dataframe named 'df2' with the Pandas library 'read_sql' with ports and conn as the parameters

LocationLatitude=np.array( df.iloc[0:9,0]) # create an array 'LocationLatitude' with the Numpy libray, consisting of the first 0 to 9 rows of the 0th row of the dataframe 'df'
LocationLongitude=np.array( df.iloc[0:9,1]) # create an array 'LocationLongitude' with the Numpy libray, consisting of the first 0 to 9 rows of the 1st row of the dataframe 'df'
LocationProduction=np.array( df.iloc[0:9,2]) # create an array 'LocationProduction' with the Numpy libray, consisting of the first 0 to 9 rows of the 2nd row of the dataframe 'df'

PortsLatitude=np.array (df2.iloc[0:9,0]) #  create an array 'PortsLatitude' with the Numpy libray, consisting of the first 0 to 9 rows of the 0th row of the dataframe 'df2'
PortsLongitude=np.array( df2.iloc[0:9,1])# create an array 'PortsLongitude' with the Numpy libray, consisting of the first 0 to 9 rows of the 1st row of the dataframe 'df2'
for i in range(len(LocationLatitude)): #For every row 'i' in the range 0 to the length of the array 'LocationLatitude'
    for x in range(len(PortsLatitude)): #For every row 'x' in the range 0 to the length of the array 'PortsLatitude'
        costs.append((((LocationLatitude[i] - PortsLatitude[x])**2+ \
        (LocationLongitude[i]-PortsLongitude[x])**2)**(0.5))* \
        LocationProduction[i]) # Add to the array 'costs' by subtracting square of the x'th element of Ports Latitude from the i'th element of LocationLatitude and adding this to the square of the subtraction 
        #of the x'th element of PortsLongitude from the i'th element of LocationLongitude and the finding the square root of this sum - Effectively, using Pythagerous Theorem to find the distance between the points
        locations.append(i+1) # appending the array 'Locations' with the number 'i' and adding 1 to it to transform it to a real world number - this is done at the same point as the cost for the i'th element calculation to simulate a dictionary creation
        portslocation.append(x+1) # appending the array 'PortsLocations' with the number 'x' and adding 1 to it to transform it to a real world number - this is done at the same point as the cost for the x'th element calculation to simulate a dictionary creation


print "The location that gives the lowest transport costs is Location " + str(locations[np.argmin(costs)]) + " and Port " + str( portslocation[np.argmin(costs)]) + " giving a total cost of €"+ str( costs[np.argmin(costs)])
# print the above string with the text and using the Numpy library function 'argmin' to find which element of the costs array is the lowest - this turns out to be 14, so the index 14 is looked up Loctaions and PortsLocations array