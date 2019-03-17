# Import the necessary dependencies for os.path.join()
import os
import csv
import datetime
import calendar

now = datetime.datetime.now()
#################################
###  Total Value :3521001       #
###  Khan: 63.000% (2218231)    #
###  Correy: 20.000% (704200)   #
###  Li: 14.000% (492940)       #
###  O'Tooley: 3.000% (105630)  #
###  Winner:Khan with 63% Votes #
#################################
# Read in a .csv filels
data_output = os.path.join("C:\\Users\\KS185259\\Documents\\Python\\HomeWork", "election_data.csv")
total_voter = []
total_votes = 0 
total_votes1 = 0
total_votes2 = 0
total_votes3 = 0
total_votes4 = 0
percentage1 = 0.00
percentage2 = 0.00
percentage3 = 0.00
percentage4 = 0.00
Counter1 = 0
Counter2 = 0
Counter3 = 0
Counter4 = 0
voter_num = ""
x=[]
Cand_Name = []
Cand_Name1 = []
# Write data to a .csv file
with open(data_output, newline="") as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    #print(len(Cand_Name))
    for row in csvreader :
        
        if row[0] != "Voter ID":
               
            if voter_num not in row[0]: 
                #print("row 1",row[0],"voter_num",voter_num)
                voter_num = row[0]
                total_votes = total_votes + 1
            else :
                voter_num = row[0]
                total_votes = total_votes + 1
        
        if (row[2] != "Candidate") and (len(Cand_Name)==0):
            #print("Firscleat Value1",Cand_Name) #clear "Row[2]",row[2])
            Cand_Name.append(row[2])
            #print("First Value",Cand_Name)
        elif (row[2] not in str(Cand_Name)) and (row[2] != "Candidate"): 
            Cand_Name.append(row[2])
    
with open(data_output, newline="") as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter=",")
    for row_second in csvreader1:
        #print("W",WsValue[0],"Name:", row_second[2])
        if (row_second[2] == Cand_Name[0]) and (row_second[2] != "Candidate"):
            #total_votes1 = total_votes1 + int(row_second[0]) 
            Counter1 = Counter1 + 1
            #print("second",Cand_Name[0],"Total_vote",total_votes1)
        if (row_second[2] == Cand_Name[1]) and (row_second[2] != "Candidate"):
            #total_votes2 = total_votes2 + int(row_second[0]) 
            Counter2 = Counter2 + 1
            #print("second",Cand_Name[1],"Total_vote",total_votes2)
        if (row_second[2] == Cand_Name[2]) and (row_second[2] != "Candidate"):
            #total_votes3 = total_votes3 + int(row_second[0])
            Counter3 = Counter3 + 1
            #print("second",Cand_Name[2],"Total_vote",total_votes3)
        if (row_second[2] == Cand_Name[3]) and (row_second[2] != "Candidates"):
            #total_votes4 = total_votes4 + int(row_second[0])
            Counter4 = Counter4 + 1
            #print("Correy:",Cand_Name[3],"Total_vote",total_votes4)

percentage1 = round((float(Counter1)/float(total_votes) * 100),4)
percentage2 = round((float(Counter2)/float(total_votes) * 100),4)
percentage3 = round((float(Counter3)/float(total_votes) * 100),4)
percentage4 = round((float(Counter4)/float(total_votes) * 100),4)

print("Election Results")
print("-------------------------------")
print("Total Votes:",total_votes)
print("-------------------------------")
print(Cand_Name[0],"%.3f" %percentage1,"% (",Counter1,")")
print(Cand_Name[1],"%.3f" %percentage2,"% (",Counter2,")")
print(Cand_Name[2],"%.3f" %percentage3,"% (",Counter3,")")
print(Cand_Name[3],"%.3f" %percentage4,"% (",Counter4,")")
print("-------------------------------")
print("Winner:",Cand_Name[0],"with",round(max(percentage1,percentage2,percentage3,percentage4)), "% Votes")
print("-------------------------------")

f = open("C:\PyPoll.txt", "w")
f.write("Election Results")
f.write("\n--------------------------------")
f.write("\nTotal Value :" + str(total_votes))
f.write("\n--------------------------------")
f.write("\n"+Cand_Name[0]+": "+str("%.3f"%percentage1)+"% ("+str(Counter1)+")")
f.write("\n"+Cand_Name[1]+": "+str("%.3f" %percentage2)+"% ("+str(Counter2)+")")
f.write("\n"+Cand_Name[2]+": "+str("%.3f" %percentage3)+"% ("+str(Counter3)+")")
f.write("\n"+Cand_Name[3]+": "+str("%.3f" %percentage4)+"% ("+str(Counter4)+")")
f.write("\n--------------------------------")
f.write("\n"+"Winner:\t"+Cand_Name[0]+" with "+str(round(max(percentage1,percentage2,percentage3,percentage4)))+"% Votes")
f.write("\n--------------------------------")
                