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

col=df.as_matrix() # create matrix out of dataframes
col2=df2.as_matrix()
#print col # look at what the matrices look like
#print col2