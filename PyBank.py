# Import the necessary dependencies for os.path.join()
import os
import csv
import datetime
import calendar

now = datetime.datetime.now()
AvgPerct = 0
# Read in a .csv filels
data_output = os.path.join("HomeWork", "Budget_data.csv")

totalmonth = 0
avgCharge = []
change = 0
ProfitOne = 0
# Write data to a .csv file
with open(data_output, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    
    #for month_idx in range(1, 13): monthInYear = calendar.month_abbr[month_idx].lower()
    
    i = 0 
    totalval = 0
    myloop = 0 
    row_count = 0 
    Greatest_value = 0 
    Greatest_Decrease = 0 
    for row in csvreader :
     
        #for myvalue in ProfitOne:
            #print(f"myvalue",row[1],"ProfiOne",ProfitOne)
            
            if myloop != 0:
                if ProfitOne != 0:
                    avgCharge1 =  float(row[1]) - float(ProfitOne)
                    avgCharge.append(avgCharge1)
                    row_count = row_count + 1

                    if avgCharge1 > Greatest_value :
                        Greatest_value = avgCharge1
                        NameofMonth = row[0]
                    if avgCharge1 < Greatest_Decrease :
                        Greatest_Decrease = avgCharge1
                        NameofMonth1 = row[0]
            
            if row[1] != "Profit/Losses" :
                totalval = totalval + int(row[1])
                  
            month = row[0].split("-")
            for month_idx in range(1, 13): 
                monthInYear = calendar.month_abbr[month_idx].lower()
                #print(f"\t yearM",monthInYear, "Month", month[0])
            
                if month[0].lower() == monthInYear :
                    totalmonth  = totalmonth + 1
            #print("mylopp", myloop)
            if myloop != 0: 
                 ProfitOne = float(row[1])
                 myloop = myloop + 1
        
            myloop = 1
AvgPerct = (float(sum(avgCharge)/row_count))
print("  Financial Analysis")
print("-------------------------------")
print("Total Months: ", totalmonth)
print("Total: ", totalval)
print("Average Change", "%.2f" %AvgPerct)
print("Greatest Increase in Profits:",round(Greatest_value))
print("Greatest Decrease in Profits:",round(Greatest_Decrease))

f = open("C:\PyBank.txt", "w")
f.write("Financial Analysis")
f.write("\n----------------------------")
f.write("\nTotal Months: "+ str(totalmonth))
f.write("\n"+"Total: "+ str(totalval))
f.write("\n"+"Average Change"+ "%.2f" %AvgPerct)
f.write("\n"+"Greatest Increase in Profits:"+str(round(Greatest_value)))
f.write("\n"+"Greatest Decrease in Profits:"+str(round(Greatest_Decrease)))



