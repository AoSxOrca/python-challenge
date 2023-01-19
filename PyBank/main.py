import csv #import module
  
with open('./Resources/budget_data.csv') as csv_file: #open csv file
      
    csv_reader = csv.reader(csv_file) #create a csv reader obj
    header_row = next(csv_reader) #read header row
    
    budget_data = [[],[]] #create empty nested list to store data of csv file

    for row in csv_reader: # iterate over all the rows 
        budget_data[0].append(row[0]) #Date
        budget_data[1].append(int(row[1])) #profit/loss


total_months = len(budget_data[0]) #total months
net_total = sum(budget_data[1]) #total profit/loss

greatest_increase = 0 
greatest_increase_index = 0
greatest_decrease = 0
greatest_decrease_index = 0
changes = list()

for i in range(len(budget_data[1])): #iterate over index of all the rows and find greatest increase, decrease
    if i == 0:
        continue
    change = budget_data[1][i] - budget_data[1][i-1]
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_index = i
    if change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_index = i
    changes.append(change)

# create string to print results on console and store to text file
financial_analysis = f"Financial Analysis \n\
----------------------------\n\
Total Months: {total_months}\n\
Total: ${net_total}\n\
Average Change: ${round(sum(changes)/len(changes),2)}\n\
Greatest Increase in Profits: {budget_data[0][greatest_increase_index]} (${greatest_increase})\n\
Greatest Decrease in Profits: {budget_data[0][greatest_decrease_index]} (${greatest_decrease})"

print(financial_analysis) #print results

file = open("./analysis/final-analysis.txt","w") #open file to write
file.write(financial_analysis) #write results to file
file.close() #close file