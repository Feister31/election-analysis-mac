

# import dependencies
import csv
import os

# add a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")

#initalize a total vote counter
total_votes = 0

# Candidate Options and candidate votes
candidate_options = []
candidate_votes = {}

# Challenge options 
county_names =[]
county_votes = {}

# Track the winning candidate vote count and percentage 

winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Challenge track the largeset county vote turnout and its percentage

largest_county_turnout = ""
largest_county_votes = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    print(reader)
# read the header
    header = next(reader)
# print(header)

    for row in reader:
        #add to the toal votes count
        total_votes = total_votes + 1 

        #Get the candidate name from each row
        candidate_name = row[2]

        #Extract the county name from each row
        county_name = row[1]

        # if the candidate does not match any existing candidate add it into 
        # the list

        if candidate_name not in candidate_options:
            #add the 
            candidate_options.append(candidate_name)
            # add begin tracking that candidate voter count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidate count
        candidate_votes[candidate_name] += 1

        #challege county
        if county_name not in county_names:

                #challenge add it to the list in the running
                county_names.append(county_name)

                #tracking that candidate voter count
                county_votes[county_name] = 0 
        county_votes[county_name] += 1
# save the result to our text file
with open(file_to_save, "w") as txt_file:
        #print the final vote count
        election_results = (
            f"\nElection Results\n"
            f"\n-------------------\n"
            f"Total Votes: {total_votes:,}"
            f"\n-------------------\n\n"
            f"County Votes:\n"
        )
        print(election_results , end="")
        txt_file.write(election_results)
        
        #challenge save the final county
        for county in county_votes:
            #retrieve vote count and percentage 
            county_vote = county_votes[county]
            county_percent = int(county_vote) / int(total_votes) * 100
            county_results = (
                f"{county}: {county_percent:.1f}% ({county_vote:,})\n"
            )
            print(county_results, end="")
            txt_file.write(county_results)       

            # DETERMINE WINNING VOTE COUNT AND CANDIDATE
            if(county_vote > largest_county_votes):
                largest_county_votes = county_vote
                largest_county_turnout = county
        #print the county iwth the largest turnout
        largest_county_turnout = ( 
            f"\n------------------------------\n"
            f"Largest County Turnout: {largest_county_turnout}\n"
            f"--------------------------------\n"
        )
        print(largest_county_turnout)
        txt_file.write(largest_county_turnout)

        for candidate in candidate_votes:
            #retreve vote count and percentage
            votes = candidate_votes[candidate]
            vote_percentage = int(votes) / int(total_votes) * 100
            candidate_results = (
                f"{candidate}: {vote_percentage:.1f}% ({votes:,}\n"
            )
            
            print(candidate_results)
            # Save the candidate result to our text file
            txt_file.write(candidate_results)
            
            # Determine the winner of the vote count winning percentage
            if(votes > winning_percentage) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_candidate = candidate
                winning_percentage = vote_percentage

        winning_candidate_summary = (
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {vote_percentage:.1f}\n"
            f"----------------------------\n"
        )

        print(winning_candidate_summary)

        #Save the winning candidate name to the text file
        txt_file.write(winning_candidate_summary)