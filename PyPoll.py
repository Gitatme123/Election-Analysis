#added our dependencies
import csv
import os
# assign a variable for the file to lad and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election  results and read the file.
with open(file_to_load) as election_data:
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
   
    # read and print the header row
    headers = next(file_reader)
    print(headers)
    
