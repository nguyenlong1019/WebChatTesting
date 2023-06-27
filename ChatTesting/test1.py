import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import openpyxl
import os


def write_data_to_excel(data, excel_file_path):
    workbook = openpyxl.load_workbook(excel_file_path)
    sheet = workbook.active

    sheet.append(data)

    workbook.save(excel_file_path)
    workbook.close()


def create_excel_file(excel_file_path):
    workbook = openpyxl.Workbook()
    workbook.save(excel_file_path)




# đọc dữ liệu
with open(file='./Data/credentials.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)

# Xác định chỉ số của các cột
username_index = headers.index('Username')
email_index = headers.index('Password')

print(data)


# đọc dữ liệu
with open(file='./Data/data_test1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    new_data = list(reader)

print(new_data)

# Xác định chỉ số của các cột
new_username_index = headers.index('NewUsername')
new_email_index = headers.index('Email')
search_char = headers.index('Search')
room_url = headers.index('RoomURL')
profile_url = headers.index('ProfileURL')

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Tối đa hóa cửa sổ trình duyệt
driver.maximize_window()

# Mở trang web của ứng dụng
driver.get('http://127.0.0.1:8000/login/')
sleep(2.5)

url_home = "http://127.0.0.1:8000/"

excel_file_path = "./Report/test1.xlsx"
if not os.path.exists(excel_file_path):
    create_excel_file(excel_file_path)

for i in range(len(data)):
     # Định danh các phần tử trên trang web
    username_input = driver.find_element(By.ID, 'username')
    password_input = driver.find_element(By.ID, 'password')

    username_input.send_keys(data[i][1])
    password_input.send_keys(data[i][2])

    # Định vị phần tử button submit
    button_submit = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/button")
    button_submit.click()

    if driver.current_url == url_home:

        # click python
        python_topic_btn = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/ul/li[2]/a')
        python_topic_btn.click()
        sleep(2)

        # click js
        js_topic_btn = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/ul/li[5]/a')
        js_topic_btn.click()
        sleep(2)
        
        # clic All
        all_topic_btn = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/ul/li[1]/a')
        all_topic_btn.click()
        sleep(2)

       



        # room
        driver.get(new_data[i][6])
        sleep(2)

        # profile
        driver.get(new_data[i][7])
        sleep(2)

        # home
        driver.get('http://127.0.0.1:8000/')
        sleep(2)

        # 404
        btn_404 = driver.find_element(By.XPATH, '/html/body/main/div/div[1]/a')
        btn_404.click()
        sleep(2)
        
        driver.get('http://127.0.0.1:8000/')
        sleep(2)
        # edit profile
        driver.get("http://127.0.0.1:8000/update-user/")
        sleep(2)

        new_username = driver.find_element(By.XPATH, '//*[@id="id_username"]')
        new_username.clear()
        sleep(1)
        new_username.send_keys(new_data[i][1])
        sleep(2)
        new_email = driver.find_element(By.XPATH, '//*[@id="id_email"]')
        new_email.clear()
        sleep(1)
        new_email.send_keys(new_data[i][4])
        sleep(2)

        submit_btn = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/div[3]/button")
        submit_btn.click()

        sleep(3)
    else:
        pass
    driver.get("http://127.0.0.1:8000/logout/")
    driver.get("http://127.0.0.1:8000/login/")

sleep(2.5)
driver.close()