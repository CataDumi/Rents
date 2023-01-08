from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
from transformation import Transformation
import matplotlib.pyplot as plt

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

driver.maximize_window()
driver.get("https://www.imobiliare.ro/")
time.sleep(2)

trigger_cookie=driver.find_element(By.XPATH,'//*[@id="cautator"]/div[2]/h1').click()
# print('Am facut click')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[5]/div/div/div/div/div[2]/div[2]/div[2]/a'))).click()

location=driver.find_element(By.CLASS_NAME,'form-control').send_keys(Keys.BACKSPACE*11)
time.sleep(0.1)

location=driver.find_element(By.CLASS_NAME,'form-control').send_keys('Bucuresti')
time.sleep(1)

ap=driver.find_element(By.XPATH,'//*[@id="b_cautator_form"]/div[2]/div[2]/div[1]/div[2]/button').click()
time.sleep(1)
type=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/main/div/div[1]/section/div[2]/div[1]/form/div[2]/div[2]/div[1]/div[2]/ul/li[1]/ul/li[1]/a').click()
time.sleep(1)

type=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/main/div/div[1]/section/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/button/span[1]').click()
time.sleep(1)
choice=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/main/div/div[1]/section/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div/ul/li[2]/a/span[1]').click()
time.sleep(1)

search=driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/main/div/div[1]/section/div[2]/div[1]/form/div[2]/div[4]/div[1]/input').click()
time.sleep(3)

# filter=driver.find_element(By.ID,'btn_vezi_filtrele').click()



# WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,'grupa_64'))).click()
wait = WebDriverWait(driver, 30)

sector_1={}
sector_2={}
sector_3={}
sector_4={}
sector_5={}
sector_6={}

while True:
        rents = [rent.text for rent in wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'pret-mare')))]
        locations = [location.text for location in
                     wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'location_txt')))]
        # print(rents)
        # print(locations)

        dict={rents[i]:locations[i] for i in range(len(rents))}
        # print(dict)
        for key in dict:
                if 'Sector 1' in dict[key]:
                    sector_1[key] = dict[key]
                elif 'Sector 2' in dict[key]:
                    sector_2[key] = dict[key]
                elif 'Sector 3' in dict[key]:
                    sector_3[key] = dict[key]
                elif 'Sector 4' in dict[key]:
                    sector_4[key] = dict[key]
                elif 'Sector 5' in dict[key]:
                    sector_5[key] = dict[key]
                elif 'Sector 6' in dict[key]:
                    sector_6[key] = dict[key]
        # print("Am scos listele cerute\n\n")
        try:
            WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CLASS_NAME,'inainte'))).click()
            time.sleep(1)
        except TimeoutException:
            # print('E gata programul')
            break
# print('Urmeaza etapa selectarii datelor si introducerii lor in df')


list=[sector_1,sector_2,sector_3,sector_4,sector_5,sector_6]
names=['sector_1','sector_2','sector_3','sector_4','sector_5','sector_6']
values=[]

for item in range(len(names)):
    list[item] = Transformation(name=names[item], dict=list[item])
    item=pd.read_csv(f'sector_{item+1}.csv')
    values.append(item['Rent'].mean())

print(values)
fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(names, values, color=['maroon','red','yellow','blue','orange','purple'],
        width=0.4)

# Add title, axis labels, and legend
plt.title('Rent prices for apartments in different sectors of Bucharest')
plt.xlabel('Sector')
plt.ylabel('Price (EUR)')


plt.show()

