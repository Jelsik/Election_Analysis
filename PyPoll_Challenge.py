#add some dependencies
import csv
from itertools import count
import os
#assign variables for a file
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0 #count the votes variable
#Create County Variables
county_options = [] #count counties
county_votes={} #store votes for county
voter_turnout = 0
voter_percentage = 0
mostcountyvotes = 0
largest_county=""
largest_county_output = ""
countyheader = "County Votes:\n"
candidate_option = [] #candidate counter 
#create dictionary for storing votes to candidate
candidate_votes = {}
#Winning Candidate Counter Variables
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#open and read the election results
with open(file_to_load) as election_data:
    #read and analyze data here
    file_reader = csv.reader(election_data)
    headers = next(file_reader)  
    #read rows and count total number of votes
    for row in file_reader:
        total_votes = total_votes + 1
        #read first row to skip header
        candidate_name = row[2]
        county_name = row[1]
        #add county names
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name]= 0
        #add candidates names v
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #count votes for each candidate
        county_votes[county_name]+=1
        candidate_votes[candidate_name] +=1
    #print(candidate_votes)
    #print(county_votes) check if data collected
#open file and write results to it
with open(file_to_save, "w") as txt_file:
    
    election_results = (f"Election Results\n"
                        f"-------------------\n"
                        f"Total Votes: {total_votes:,}\n"
                        f"--------------------\n\n")
    txt_file.write(election_results)
    print(election_results.strip())  #.strip() used to remove space and help with formatting
    print("")
    print(countyheader.strip())
    txt_file.write(countyheader)
    #Determine County Votes
    for county_name in county_votes:
        #collect votes of county
        voter_turnout = county_votes[county_name]
        #Determine vote percentage
        voter_percentage = float(voter_turnout) / float(total_votes) * 100
        #round it
        voter_percentage = round(voter_percentage,2)
        county_results = (f"{county_name}: {voter_percentage:.1f}% ({county_votes[county_name]:,})\n")
        #print to terminal
        print(county_results.strip())
        #write to file
        txt_file.write(county_results)
        #determine county with most votes
        if(voter_turnout > mostcountyvotes):
            mostcountyvotes = voter_turnout
            largest_county = county_name
            largest_county_output = (f"\n--------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"--------------------\n")
    #print county
    print(largest_county_output) 
    #write county
    txt_file.write(largest_county_output)
    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #get percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        #round to make the percentage more readable
        vote_percentage = round(vote_percentage, 2) #code from https://stackoverflow.com/questions/3221654/specifying-number-of-decimal-places-in-python
        #print info
        candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({candidate_votes[candidate_name]:,})\n"
        )
        #print to terminal
        print(candidate_results)
        #add to file
        txt_file.write(candidate_results)
        #print(f"{candidate_name}: recieved {vote_percentage}% of the vote.\n")
        if(votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set winning count + votes and winning_percent =
            #vote_votepercentage
            winning_count = votes
            winning_percentage = vote_percentage
            #set winning candidate name 
            winning_candidate = candidate_name
            #to do: print out the winning candidate stuff
            winning_candidate_summary = (
            f"-----------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n"
        )
    
   
   
    
    #print summary of victory
    print(winning_candidate_summary)
    #write that stuff to file
    txt_file.write(winning_candidate_summary)
    
    
    
    


    