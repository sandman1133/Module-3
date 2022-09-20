# import library
import os
import csv

# join path
data_budget = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(data_budget, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
    
    # find net amount of profit and loss
    P = []
    months = []

    # read each row of data after header
    for rows in csvreader:
        P.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    change_revenue =[]

    for x in range(1, len(P)):
        change_revenue.append((int(P[x]) - int(P[x-1])))

    # calculate average revenue change
    change_avg_rev = sum(change_revenue) / len(change_revenue)
    change_revenue = round(change_avg_rev, 2)

    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(change_revenue)

    #greatest decrease in revenue
    greatest_decrease = min(change_revenue)


    # print Results
    print ("Financial Analysis")

    print("....................................................................................")

    print ("Total Months:" + str(total_months))

    print("Total:" + "$" + str(sum(P)))

    print ("Average Change:" + "$" + str(change_revenue))

    print("Greatest Increase in Profits: " + str(months[change_revenue.index(max(change_revenue))+1]) + " " + "($" + str(greatest_increase) + ")")

    print("Greatest Decrease in Profits: " + str(months[change_revenue.index(min(change_revenue))+1]) + " " + "($" + str(greatest_decrease) + ")")


    # output to a text file
    file = open("output.txt","w")

    file.write("Financial Analysis" + "\n")

    file.write("...................................................................................." + "\n")

    file.write("total months: " + str(total_months) + "\n")

    file.write("Total: " + "$" + str(sum(P)) + "\n")

    file.write("Average change: " + "$" + str(change_avg_rev) + "\n")

    file.write("Greatest Increase in Profits: " + str(months[change_revenue.index(max(change_revenue))+1]) + " " + "($" + str(greatest_increase) + ")\n")

    file.write("Greatest Decrease in Profits: " + str(months[change_revenue.index(min(change_revenue))+1]) + " " + "($" + str(greatest_decrease) + ")\n")

    file.close()
