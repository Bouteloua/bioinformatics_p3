#Python Problem 1
#mode.py
#Introduction to Bioinformatics Assignment 2
#Purpose: Find the mode
#Your Name: Brian Franzone
#Date: 02/Oct/2014

#import pandas 
import pandas as pd

#Open the table
df = pd.read_table('data.txt')

#print the mode for the column
print df.mode()