#Import dependencies
import os
import csv

#Create CSV path
create_csv_path = os.path.join("Resources","budget_data.csv")

#Extract and print headers
with open(create_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    #Define lists to use in calculations
    dates = []
    profit_loss = []
    profit_change = []

    #Calculate the total number of months included in the dataset, and
    #the net total amount of "Profit/Losses" over the entire period.
    #To do this I utilised a for loop to count total months in column 1, and sum profit/loss in the second column.
    #After this, I printed the first part of the Financial Analysis summary which displays these calculations.
    for row in csv_reader:

        profit_loss.append(float(row[1]))
        dates.append(row[0])
    
    total_months = len(dates)
    total_profit_loss = round(sum(profit_loss))

    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", total_months)
    print("Total: $", total_profit_loss)

    #Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes.
    #To do this I used a for loop to find the differences between all rows of "Profit/Loss" column and calculate average change.
    #Calculate the greatest increase in profits (date and amount) over the entire period.
    #Calculate the greatest decrease in profits (date and amount) over the entire period.
    #To do this, I utilised the same for loop to identify maximum profit change (greatest increase in profits) and
    #minimum profit change (greatest decrease in profits). 
    #After this, I printed the second part of the Financial Analysis summary which displays these calculations.
    for i in range(1,len(profit_loss)):  
        profit_change.append(profit_loss[i] - profit_loss[i-1])
        average_change = round(sum(profit_change)/len(profit_change),2)

        greatest_increase_amount = round(max(profit_change))

        greatest_decrease_amount = round(min(profit_change))

        greatest_increase_date = str(dates[profit_change.index(max(profit_change))+1])
        greatest_decrease_date = str(dates[profit_change.index(min(profit_change))+1])

    print("Avereage Change: $", average_change)
    print("Greatest Increase in Profits:", greatest_increase_date,"($", greatest_increase_amount,")")
    print("Greatest Decrease in Profits:", greatest_decrease_date,"($", greatest_decrease_amount,")")

    #Create text file with Financial Analysis summary 
    with open(os.path.join("Analysis", "Financial_Analysis.txt"), 'w') as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("----------------------------\n")
        textfile.write("Total Months: " + str(total_months) + "\n")
        textfile.write("Total: $" + str(total_profit_loss) + "\n")
        textfile.write("Average  Change: $" + str(average_change) + "\n")
        textfile.write("Greatest Increase in Profits: " + str(greatest_increase_date) + " ($" + str(greatest_increase_amount) + ")\n")
        textfile.write("Greatest Decrease in Profits: " + str(greatest_decrease_date) + " ($" + str(greatest_decrease_amount) + ")")
        textfile.close()