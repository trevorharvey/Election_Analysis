import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Election_Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis","election_analysis.txt")

# Initialize a total vote counter (candidates).
total_votes = 0
# Initialize a total vote counter (counties)
county_count = 0

# Candidate options
candidate_options = []
# Declare the empty dictionary.
candidate_votes = {}

# County options
county_options = []
# Declare the empty dictionary
county_votes = {}

# Winning Candidate and Winning Count Ticker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Highest Voting County
highest_vote_county = ""
hvc_count = 0
hvc_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Loop each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count (per candidate)
        total_votes += 1
        # Add to the total vote count (per county)
        county_count += 1

        # Print the candidate name for each row.
        candidate_name = row[2]
        # Print the county name for each row.
        county_name = row[1]

        # If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        
        # If county does not match any existing county...
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # Begin tracking that county's vote count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Add a vote to that county's count.
        county_votes[county_name] += 1
    

# Save the resukts to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    # Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate and percentage
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        
    
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate

    # Print out the winning candidate, vote count and percentage of votes to terminal.
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary) 

    # Determine the percentage of votes for each county by looping through the counts
    # Iterate through the county list
    for county in county_votes:
        # Retrieve vote count for county and percentage.
        c_votes = county_votes[county]
        c_votes_percentage = float(c_votes) / float(county_count) * 100
        county_results = (f"{county}: {c_votes_percentage:.1f}% ({c_votes:,})\n ")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        txt_file.write(county_results)

        # Determine the highest vote count, the highest voting count percentage, and highest voting county.
        if (c_votes > hvc_count) and (c_votes_percentage > hvc_percentage):
            hvc_count = c_votes
            hvc_percentage = c_votes_percentage
            highest_vote_county = county
    
    # Print out the "Largest County Turnout", vote count and percentage of votes to terminal.
    hvc_county_summary = (
        f"---------------------------\n"
        f"Largest County Turnout: {highest_vote_county}\n"
        f"---------------------------\n")
    print(hvc_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary) 

