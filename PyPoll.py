#List of Data to retrieve:
#Total Number of votes
#Candidates who recieved votes
#percentage of votes each candidate won
#total NUMBER of votes each candidate won
#The Winner of the Election by popular vote.
#windows uses \ to seperate files
#exampled of importing and using a module
#import datetime
#in order to reduce confusion with module and class names you could also:
#import datetime as dt
#use now() attribute on class to get present time
#now = dt.datetime.now()
#Print Present time
#print("the time right now is", now)

import csv
import random
import os
#dir(csv) #would list all available functions in the csv module
#or a variable if printed

#assign a variable to load the file via it's path
#file_to_load = 'Resources/election_results.csv'
#open it in READ mode
#election_data = open(file_to_load,'r')
#Perform analysis here later

#now close the file, to prevent data loss
#election_data.close()

#can use the with statement to open the file properly without
#having to worry about closing it ensuring data protection
#with open(filename) as file_variable:
#file_to_load = 'Resources/election_results.csv'
#with open(file_to_load) as election_data:
    #to do:perform analysis
  #  print(election_data)
#since with ends with a colon, we must indent the next line
#if you don't know the direct route to a file to import, use
# the os module so "import os" the os.path module will stick out
#here id you dir(os.path) you will find a function called join
#join() will join or file path components together if provided as
#seperate strings; then it returns a direct path with the appropriate
#operating system separator
#Chaining is a programmatic style to make multiple method calls
#on the same object
file_to_load = os.path.join("Resources", "election_results.csv")
#open results and read the file
with open(file_to_load) as election_data:
    #print that data
    print(election_data)
#create a filename variable to save and write to a file
file_to_save = os.path.join("analysis", "election_analysis.txt")
#use open function with the "w" mode to write to the file
#make suire you have made the folder "analysis" inside the main folder
#outfile =open(file_to_save, "w")
#let's add some simple data to the text file "write() from os import:
#outfile.write("Yo what's up.")
#don't forget to close
#outfile.close()

#can use with statement to avoid using close and open functions
with open(file_to_save,"w") as txt_file:
    #write some data
    txt_file.write("Counties in the Election\n")
    txt_file.write("-----------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")
 
    #or can do it in one line txt_file.write("Arapahoe, Jefferson, Denver")
    #\n is indicator of making a new line