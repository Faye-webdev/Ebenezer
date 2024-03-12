from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from time import sleep
import csv

UserId = input('Enter your UserId: ')
Password = input('Enter your password: ')


edgeService = Service(r"C:\Users\sowem\OneDrive\Desktop\index\msedgedriver.exe")
edgeDriver = webdriver.Edge(service=edgeService)


url = 'https://ssb-prod.ec.gram.edu/PROD/twbkwbis.P_WWWLogin'

edgeDriver.get(url)

edgeDriver.find_element(By.ID, 'UserID').send_keys(UserId)
edgeDriver.find_element(By.ID, 'PIN').send_keys(Password)
login_button = edgeDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Login']")
login_button.click()

print('Logged in successfully!')

sleep(1)

edgeDriver.get('https://ssb-prod.ec.gram.edu/PROD/twbkwbis.P_GenMenu?name=bmenu.P_StuMainMnu')

sleep(1)

edgeDriver.get('https://ssb-prod.ec.gram.edu/PROD/twbkwbis.P_GenMenu?name=bmenu.P_AdminMnu')

sleep(1)

edgeDriver.get('https://ssb-prod.ec.gram.edu/PROD/bwskogrd.P_ViewTermGrde')

sleep(1)

Submit_button = edgeDriver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
Submit_button.click()

sleep(1)

grades = edgeDriver.find_elements(By.CLASS_NAME, "datadisplaytable")
grade_tr = grades[1].find_element(By.TAG_NAME, "tbody")
grade_trr = grade_tr.find_elements(By.TAG_NAME, "tr")
grade_header = []
for grade in grade_trr:
    for grade_cell in grade.find_elements(By.TAG_NAME, "th"):
        grade_header.append(grade_cell.text)
print(grade_header)
grade_bdy = []
item = []
for grade in grade_trr:
    for grade_cll in grade.find_elements(By.TAG_NAME, "td"):
        grade_bdy.append(grade_cll.text.strip())
if '' in grade_bdy:
    grade_bdy.remove('')

new_2d_array = []
current_row = []


for item in grade_bdy:
    if item == '':
        if current_row:
            new_2d_array.append(current_row)
        current_row = []
    else:
        current_row.append(item)

if current_row:
    new_2d_array.append(current_row)

print(new_2d_array)

result_dicts = []

for row in new_2d_array:
    pairs = zip(grade_header, row)

    result_dict = dict(pairs)
    result_dicts.append(result_dict)

print(result_dicts)

csv_file_path = 'grades.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    fieldnames = result_dicts[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in result_dicts:
        writer.writerow(row)

print(f'Data written to {csv_file_path}')






