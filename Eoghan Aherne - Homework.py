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