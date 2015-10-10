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