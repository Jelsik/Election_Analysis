#add some dependencies
import csv
import os
#assign variables for a file
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")
total_votes = 0 #count the votes variable
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
        #add candidates names v
        if candidate_name not in candidate_option:
            candidate_option.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #count votes for each candidate
        candidate_votes[candidate_name] +=1
    #print(candidate_votes)
#open file and write results to it
with open(file_to_save, "w") as txt_file:
    
    election_results = (f"Election Results\n"
                        f"-------------------\n"
                        f"Total Votes: {total_votes}\n"
                        f"--------------------\n")
    txt_file.write(election_results)

    for candidate_name in candidate_votes:
        #retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #get percentage
        vote_percentage = float(votes) / float(total_votes) * 100
        #round to make the percentage more readable
        vote_percentage = round(vote_percentage, 2) #code from https://stackoverflow.com/questions/3221654/specifying-number-of-decimal-places-in-python
        #print info
        candidate_results = (
        f"{candidate_name}: {vote_percentage:.1f}% ({candidate_votes[candidate_name]})\n"
        )
        #print to terminal
        print(candidate_results)
        #add to file
        txt_file.write(candidate_results)
        print(f"{candidate_name}: recieved {vote_percentage}% of the vote.\n")
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
            f"Winner :{winning_candidate}\n"
            f"Winning Vote Count: {winning_count}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n"
        )
    
#print to figure out still going
    print(election_results,"")
   
       
    #print summary of victory
    print(winning_candidate_summary)
    #write that stuff to file
    txt_file.write(winning_candidate_summary)
    
    
    
    


    