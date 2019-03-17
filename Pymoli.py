import os
import csv
import datetime

states={
'Alaska': 'AK',
'Alabama': 'AL',
'Arkansas': 'AR',
'American Samoa': 'AS',
'Arizona': 'AZ',
'California': 'CA',
'Colorado': 'CO',
'Connecticut': 'CT',
'District of Columbia': 'DC',
'Delaware': 'DE',
'Florida': 'FL',
'Georgia': 'GA',
'Guam': 'GU',
'Hawaii': 'HI',
'Iowa': 'IA',
'Idaho': 'ID',
'Illinois': 'IL',
'Indiana': 'IN',
'Kansas': 'KS',
'Kentucky': 'KY',
'Louisiana': 'LA',
'Massachusetts': 'MA',
'Maryland': 'MD',
'Maine': 'ME',
'Michigan': 'MI',
'Minnesota': 'MN',
'Missouri': 'MO',
'Northern Mariana Islands': 'MP',
'Mississippi': 'MS',
'Montana': 'MT',
'National': 'NA',
'North Carolina': 'NC',
'North Dakota': 'ND',
'Nebraska': 'NE',
'New Hampshire': 'NH',
'New Jersey': 'NJ',
'New Mexico': 'NM',
'Nevada': 'NV',
'New York': 'NY',
'Ohio': 'OH',
'Oklahoma': 'OK',
'Oregon': 'OR',
'Pennsylvania': 'PA',
'Puerto Rico': 'PR',
'Rhode Island': 'RI',
'South Carolina': 'SC',
'South Dakota': 'SD',
'Tennessee': 'TN',
'Texas': 'TX',
'Utah': 'UT',
'Virginia': 'VA',
'Virgin Islands': 'VI',
'Vermont': 'VT',
'Washington': 'WA',
'Wisconsin': 'WI',
'West Virginia': 'WV',
'Wyoming': 'WY'
}
i=0
value = 0
Name = []
SSN=[]
file = open("PyBoss.csv",'w')

file.write("Emp ID,"+"First Name,"+"Last Name,"+"DOB,"+"SSN,"+"State")
file = open("PyBoss.csv",'a+')
data_output = os.path.join("HomeWork","employee_data.csv")

with open(data_output, newline="") as csvfile:


   csvreader = csv.reader(csvfile, delimiter=",")
   next(csvreader)
   for row in csvreader:

      Name = row[1].split()
      FirstName = Name[0]
      LastName = Name[1]
      date_time_obj = datetime.datetime.strptime(row[2], '%Y-%m-%d').date()
      SSN = row[3].split("-")
      file.write("\n"+row[0]+","+FirstName+","+LastName +","+str(date_time_obj)+","+"***-**-"+SSN[2]+","+states[row[4]])
      #print(row[0],FirstName,LastName,str(date_time_obj),"***-**-",SSN[2],states[row[4]])

    

