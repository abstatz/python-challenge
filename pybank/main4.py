
import os
import csv


change_list = []
profit_loss = 0
total_months = 0
max_change = ["",0]
min_change = ["",99999999]


csvpath = os.path.join('budget_data.csv')


with open(csvpath) as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')

	# read header
	csv_header = next (csvreader)
	

	first_row = next(csvreader)
	monthly_value = int(first_row[1])




	for row in csv.reader(csvfile):
		profit_loss += int(row[1])


		total_months += 1


		monthly_change = int(row[1])- monthly_value
		monthly_value = int(row[1])
		change_list.append(monthly_change)

		if monthly_change > max_change[1]:
			max_change[0] = row[0]
			max_change[1] = monthly_change

		if monthly_change < min_change[1]:
			min_change[0] = row[0]
			min_change[1] = monthly_change


monthly_average = sum(change_list)/len(change_list)		









print("Financial Analysis")
print("--------------------------------------------")
print(f"Total Months: {total_months} ")
print(f"Total Profit and Loss:  ${profit_loss}")
print(f"Average Change: $ {monthly_average:.2f}")
print(f"Greatest Increase in Profits: {max_change[0]} ${max_change[1]} ")
print(f"Greatest Decrease in Profits: {min_change[0]} ${min_change[1]} ")









# Generate Output 
file = open("pybankoutput.txt", "w")
Summaryoutput = (    f"Financial Analysis\n"    f"-------------------------------\n"    f"Total Months: {total_months}\n"    f"Total: ${profit_loss}\n"    f"Average  Change: ${monthly_average:.2f}\n"    f"Greatest Increase in Profits: {max_change[0]} ${max_change[1]})\n"    f"Greatest Decrease in Profits: {min_change[0]} ${min_change[1]})\n")
file.writelines(Summaryoutput)
file.close()