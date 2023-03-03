# Exploratory Data Analysis of Privacy Aspects of Each App


import os

no_data_collected = 0
No_data_shared = 0
data_encrypted = 0
data_deleted = 0
committed = 0

files = os.listdir("Apps_Data_Safety")
for file in files:
    dir = "Apps_Data_Safety/" + str(file)
    with open(dir) as f:
        contents = f.read()
        #print(contents)
    
        ## No Data Collected
        if "No data collected" in contents:
            no_data_collected += 1
        
        if "No data shared with third parties" in contents:
            No_data_shared += 1
        
        if "Data is encrypted in transit" in contents:
            data_encrypted += 1
        
        if "You can request that data be deleted" in contents:
            data_deleted += 1
        
        if "Committed to follow the Play Families Policy" in contents:
            committed += 1

print("No Data collected " + str(no_data_collected))
print("No data shared with third parties " + str(No_data_shared))
print("You can request that data be deleted " + str(data_deleted))
print("Data is encrypted in transit " + str(data_encrypted))
print("Committed to follow the Play Families Policy " + str(committed))
