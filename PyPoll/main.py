# import modules
import os
import csv

# Path to collect data
csvpath = os.path.join("./Resources/election_data.csv")

# Columns = "Voter ID, County, Candidate"

election_poll = {}
voter_ids = []
voter_county = []
total_votes_number = []
votes_percentage = []
total_votes_counter = 0
candidates_list = []
total_votes = 0
winner = []

# Read csv
with open(csvpath, newline= '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    for row in csvreader:

        #count the lines of data for total votes
        total_votes_counter = total_votes_counter + 1
        
        # fills dictionary using candidate names as keys, 
        # one key per name.
        if row[2] in election_poll.keys():
            election_poll[row[2]] = election_poll[row[2]] + 1
        else:
            election_poll[row[2]] = 1

# Fill in the dictionary with keys and values
for key, value in election_poll.items():
    candidates_list.append(key)
    total_votes_number.append(value)

# Now find the precentage
for v in total_votes_number:
    votes_percentage.append(round(v/total_votes_counter*100, 1))

# Group the lists into related tuples using zip function
poll_data = list(zip(candidates_list, total_votes_number, votes_percentage))

for candidate in poll_data:
    if max(total_votes_number) == candidate[1]:
        winner.append(candidate[0])

# Print in terminal and to a txt file
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("ELECTION RESULTS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Total Votes: "+ str(sum(total_votes_number)))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print((str(candidates_list[0]))+ ": "+ str(total_votes_number[0]) +" total votes, %"+ str(votes_percentage[0]))
print((str(candidates_list[1]))+ ": "+ str(total_votes_number[1]) +" total votes, %"+ str(votes_percentage[1]))
print((str(candidates_list[2]))+ ": "+ str(total_votes_number[2]) +" total votes, %"+ str(votes_percentage[2]))
print((str(candidates_list[3]))+ ": "+ str(total_votes_number[3]) +" total votes, %"+ str(votes_percentage[3]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Winner: "+ str(winner[0]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

with open('Pypoll.txt', 'w') as text_file:
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f"ELECTION RESULTS", file=text_file)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f"Total Votes: "+ str(sum(total_votes_number)), file=text_file)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print((str(candidates_list[0]))+ ": "+ str(total_votes_number[0]) +" total votes, %"+ str(votes_percentage[0]), file=text_file)
    print((str(candidates_list[1]))+ ": "+ str(total_votes_number[1]) +" total votes, %"+ str(votes_percentage[1]), file=text_file)
    print((str(candidates_list[2]))+ ": "+ str(total_votes_number[2]) +" total votes, %"+ str(votes_percentage[2]), file=text_file)
    print((str(candidates_list[3]))+ ": "+ str(total_votes_number[3]) +" total votes, %"+ str(votes_percentage[3]), file=text_file)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f"WINNER: "+ str(winner[0]), file=text_file)
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
