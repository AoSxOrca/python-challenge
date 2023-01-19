import csv #import module
  
with open('./Resources/election_data.csv') as csv_file: #open csv file
      
    csv_reader = csv.reader(csv_file) #create a csv reader obj
    header_row = next(csv_reader) #read header row
    
    election_data = [[],[],[]] #create empty nested list to store data of csv file

    for row in csv_reader: # iterate over all the rows 
        election_data[0].append(int(row[0])) #Id
        election_data[1].append(row[1]) #County
        election_data[2].append(row[2]) #Candidate
    
total_votes = len(election_data[0]) #total votes
candidates = list(set(election_data[2])) #all candidates list
candidates.sort() #sort list
candidates_votes = [] #list to store all candidates votes
candidates_votes_perc = [] #list to store all candidates votes percentage
winner_name = "" #winner name
winner_votes = 0 #winner total votes

for candidate in candidates: #iterate over all candidates names and find votes, percentage and winner
    cand_votes = election_data[2].count(candidate)
    cand_votes_per = (cand_votes/total_votes)*100
    candidates_votes.append(cand_votes)
    candidates_votes_perc.append(cand_votes_per)
    if cand_votes>winner_votes:
        winner_votes = cand_votes
        winner_name = candidate

# create string to print results on console and store to text file
election_results = f"\
Election Results\n\
-------------------------\n\
Total Votes: {total_votes}\n\
-------------------------\n"
for i in range(len(candidates)):

    election_results += f"{candidates[i]}: {round(candidates_votes_perc[i],2)}% ({candidates_votes[i]})\n"

election_results += f"\
-------------------------\n\
Winner: {winner_name}\n\
-------------------------"

print(election_results) #print results

file = open("./analysis/election-results.txt","w") #open file to write
file.write(election_results) #write results to file
file.close() #close file