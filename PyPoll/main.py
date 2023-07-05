import os
import csv

# Paths to collect and distribute data
election_csv = os.path.join("Resources", "election_data.csv")
election_txt = os.path.join("analysis", "election_analysis.txt")

# Define variables
total_votes_casted = 0
candidate_votes = {}
candidate_name = []
winning_candidate = ""
charles_percentage = 0
diana_percentage = 0
raymon_percentage = 0
charles_count = 0
diana_count = 0
raymon_count = 0

# Read the CSV
with open(election_csv, encoding="UTF-8") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row first
    csv_header = next(csvreader)

    # Loop through CSV and perform calculations
    for row in csvreader:

        # Add to total vote count
        total_votes_casted += 1

        # Get candidate from each row
        candidate = row[2]

        # Add candidate to candidate list
        if candidate not in candidate_name:
            candidate_name.append(candidate)

        # Begin tracking candidate's votes
            candidate_votes[candidate] = 0
        
        # Add votes to candidate's count
        candidate_votes[candidate] = candidate_votes[candidate] + 1


# Obtain Winner
    for candidate in candidate_votes:
        if (candidate_votes.get("Charles Casper Stockham") > candidate_votes.get("Diana DeGette") and candidate_votes.get("Charles Casper Stockham") > candidate_votes.get("Raymon Anthony Doane")):
            winning_candidate = "Charles Casper Stockham"
        elif (candidate_votes.get("Diana DeGette") > candidate_votes.get("Charles Casper Stockham") and candidate_votes.get("Diana DeGette") > candidate_votes.get("Raymon Anthony Doane")):
            winning_candidate = "Diana DeGette"
        elif (candidate_votes.get("Raymon Anthony Doane") > candidate_votes.get("Charles Casper Stockham") and candidate_votes.get("Raymon Anthony Doane") > candidate_votes.get("Diana DeGette")):
            winning_candidate = "Raymon Anthony Doane"

        
    # Get percentages for each candidate
    charles_percentage = (candidate_votes.get("Charles Casper Stockham")) / total_votes_casted * 100
    diana_percentage = (candidate_votes.get("Diana DeGette")) / total_votes_casted * 100
    raymon_percentage = (candidate_votes.get("Raymon Anthony Doane")) / total_votes_casted * 100

    # Get counts for each candidate
    charles_count = (candidate_votes.get("Charles Casper Stockham"))
    diana_count = (candidate_votes.get("Diana DeGette"))
    raymon_count = (candidate_votes.get("Raymon Anthony Doane"))
                         

# # Write Text File with Printed Outputs
with open(election_txt, "w") as txtfile:

    output = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes_casted}\n"
        f"-------------------------\n"
        f"Charles Casper Stockham: {charles_percentage: .3f}% ({charles_count}) \n"
        f"Diana DeGette: {diana_percentage: .3f}% ({diana_count}) \n"
        f"Raymon Anthony Doane: {raymon_percentage: .3f}% ({raymon_count}) \n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------"
    )
    print(output)
    txtfile.write(output)



# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------