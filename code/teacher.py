#Code to find out wether the app is teacher approved or not

import pandas as pd
df = pd.read_csv('review_kids_apps.csv')
k = df['app_name'].unique()
length = len(k)
print(length)
count = 0
teach_array = []
for ele in k:
    print(count)
    string = ''
    count = count + 1
    url = "https://play.google.com/store/apps/details?id=" + str(ele)
    driver.get(url)
    try:
        Teacher = driver.find_elements(By.XPATH, './/div[@class="g1rdde"]')
        for ele in Teacher:            
            string = string + str(ele.text)
        if "Teacher Approved" in string:
            teach_array.append(1)
            #print(str(count) + "Yes")
        else:
            print(str(count) + "No")
            #teach_array.append(0)
    except:
        print(str(count) + "No")
        teach_array.append(0)

teachers_df = pd.DataFrame()
teachers_df['App'] = k
teachers_df['Teacher Approved'] = teach_array
