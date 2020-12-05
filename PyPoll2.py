import os
import csv

total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0


file_path = os.path.join(
    "/Users/a56k/Desktop/Analytics.project/Election_Analysis/Resources", "election_results.csv")
file_to_save = os.path.join(
    "/Users/a56k/Desktop/Analytics.project/Election_Analysis/Resources", "election_analysis.txt")

with open(file_path) as election_data:
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2] 
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
    candidate_votes[candidate_name] += 1
    
            
with open(file_to_save, "w") as text_file:
    election_result = (
    f"\nElection Results\n"
    f"\n------------------------\n"
    f"\nTotal Votes: {total_votes:,}\n"
    f"---------------------\n")
    print(election_result, end="")
    text_file.write(election_result)
    text_file.write("Arapahoe\nDenver\nJefferson")
    for candidate_name in candidate_votes:
        
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes)*100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        text_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
            
    
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winnning vote count: {winning_count:,}\n"
        f"Winning percentage: {vote_percentage:.1f}%\n"
        f"-----------------------\n")
    print(winning_candidate_summary)
    text_file.write(winning_candidate_summary)