import pandas as pd 
import numpy as np 
import matplotlib.pyplot as graph 

moviedata = pd.read_csv("movie_metadata.txt", index_col="movie_title")

#print (moviedata.shape)
print (moviedata.head(5))

"""
temp_double = moviedata.append(moviedata)
print(temp_double.shape)

temp_double = temp_double.drop_duplicates()
print "new shape after duplicates dropped = \n"
print (temp_double.shape)

print "Looks like the original dataset had duplicates too. Dropping duplicates from original .....  = \n"
moviedata.drop_duplicates(inplace=True)
print (moviedata.shape)
"""

#print (moviedata.columns)

##for col in moviedata:
##	print col + " .. "

print moviedata.isnull().sum()

critic_reviews = moviedata['num_critic_for_reviews']
critic_review_mean = critic_reviews.mean()
print critic_review_mean
critic_reviews.fillna(critic_review_mean, inplace=True)
#print critic_reviews

print moviedata.isnull().sum()
