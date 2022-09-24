#add some dependencies
import csv
import os
#assign variables for a file
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open and read the election results
with open(file_to_load) as election_data:
    #read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)  
    #for row in file_reader:
        #print(row)
    #read and print the header row
  