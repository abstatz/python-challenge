


import os
import csv

candidate_votes = {}
candidates = []

votes = 0
winning_votes = 0


csvpath = os.path.join('election_data.csv')


with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	# read header
	csv_header = next (csvreader)
	

	#same as banking related to header; no work on row 1

	#start for loop; create var = totat votes >> +1
	#dictionary for the candidate; create empty dic before opeing the file; dictionary will be based on key value
	#just getting votes throuh loop and calc based on dictionary
	

	for row in csv.reader(csvfile):
		votes += 1

		candidate = row[2]
		if candidate not in candidates:
			candidates.append(candidate)
			candidate_votes[candidate] = 0

		candidate_votes[candidate] +=1
	#print(candidate_votes[candidate])
	for candidate in candidate_votes:
		if (candidate_votes[candidate]) > winning_votes:
			winning_votes = (candidate_votes[candidate])
			winner = candidate

print("Election Results")
print("--------------------------------------------")
print(f"Total Votes: {votes}")
print("--------------------------------------------")
for candidate in candidate_votes:
	print(f"{candidate} {candidate_votes[candidate]/votes:.0%} ({candidate_votes[candidate]})")

print("--------------------------------------------")
	#election results = (F streams)

print(winner)





file = open("pypolloutput.txt", "w")
Summaryoutput = ( 
f"Election Results\n"    
f"--------------------------------------------\n"    
f"Total Votes: {votes}\n" 
f"--------------------------------------------\n"
)

file.writelines(Summaryoutput)

for candidate in candidate_votes:
    voter_output = f"{candidate}: {candidate_votes[candidate]/votes:.0%} ({candidate_votes[candidate]})\n"
    file.writelines(voter_output)

summaryoutput2 = (f"{candidate} {candidate_votes[candidate]/votes:.0%} ({candidate_votes[candidate]})\n"  f"--------------------------------------------\n" f"The Winner is: {winner}")
file.writelines(summaryoutput2)
file.close()