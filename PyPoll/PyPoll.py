import os
import csv

#Create CSV path
create_csv_path = os.path.join("Resources","election_data.csv")

#Extract and print headers
with open(create_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    #Define lists and variables to use in calculations
    voter_id = []
    candidates = []
    khan_count = 0
    correy_count = 0
    li_count = 0
    otooley_count = 0

    #Calculate the total number of votes in the dataset using a for loop to count total number of voter id values in column 1.
    #Also calculate the number of votes for each candidate by looping through each row and adding to total count of votes for each candidate.
    #After this, print the first part of the Election Results summary which displays this calculation.
    for row in csv_reader:

        voter_id.append(row[0])

        if str(row[2]) == "Khan":
            khan_count = khan_count + 1
        elif str(row[2]) == "Correy":
            correy_count = correy_count + 1
        elif str(row[2]) == "Li":
            li_count = li_count + 1
        elif str(row[2]) == "O'Tooley":
            otooley_count = otooley_count + 1
    
    total_votes = len(voter_id)

    #Create dictionary that keeps the number of votes for each candidate
    candidate_votes = {"Khan": khan_count,
                        "Correy": correy_count,
                        "Li": li_count,
                        "O'Tooley": otooley_count}

    #Determine the candidate with the highest number of votes, then assign candidate's name to variable "winner".
    #**winner = candidates[votes.index(max(votes))]**
    winner = max(candidate_votes, key=candidate_votes.get)

    #Calculate the percentage of votes for each candidate. 
    khan_percent = round(((khan_count/total_votes)*100),3)
    correy_percent = round(((correy_count/total_votes)*100),3)
    li_percent = round(((li_count/total_votes)*100),3)
    otooley_percent = round(((otooley_count/total_votes)*100),3)

    #Print Election Results summary.
    print("Election Results")
    print("----------------------------")
    print("Total Votes:", total_votes)
    print("----------------------------")
    print("Khan: ", khan_percent, "% (", khan_count, ")")
    print("Correy: ",correy_percent,"% (", correy_count, ")")
    print("Li: ", li_percent, "% (", li_count, ")")
    print("O'Tooley: ", otooley_percent, "% (", otooley_count, ")")
    print("----------------------------")
    print("Winner: ", winner)
    print("----------------------------")

    #Create text file with Election Results summary
    with open(os.path.join("Analysis", "Election Results.txt"), 'w') as textfile:
        textfile.write("Election Results\n")
        textfile.write("----------------------------\n")
        textfile.write("Total Votes: " + str(total_votes) + "\n")
        textfile.write("----------------------------\n")
        textfile.write("Khan: " + str(khan_percent) + "% (" + str(khan_count) + ")\n")
        textfile.write("Correy: " + str(correy_percent) + "% (" + str(correy_count) + ")\n")
        textfile.write("Li: " + str(li_percent) + "% (" + str(li_count) + ")\n")
        textfile.write("O'Tooley: " + str(otooley_percent) + "% (" + str(otooley_count) + ")\n")
        textfile.write("----------------------------\n")
        textfile.write("Winner: " + winner + "\n")
        textfile.write("----------------------------\n")
        textfile.close()
