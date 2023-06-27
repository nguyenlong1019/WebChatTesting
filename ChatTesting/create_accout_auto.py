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
with open(file='./credentials1.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    headers = next(reader)
    data = list(reader)


# Xác định chỉ số của các cột
username_index = headers.index('Username')
email_index = headers.index('Password')

print(data)



# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

# Tối đa hóa cửa sổ trình duyệt
driver.maximize_window()

# Mở trang web của ứng dụng
driver.get('http://127.0.0.1:8000/register/')
sleep(2.5)

url_home = "http://127.0.0.1:8000/"


excel_file_path = "./Report/create_data_report1.xlsx"
if not os.path.exists(excel_file_path):
    create_excel_file(excel_file_path)

for i in range(len(data)):
     # Định danh các phần tử trên trang web
    username_input = driver.find_element(By.ID, 'id_username')
    password1_input = driver.find_element(By.ID, 'id_password1')
    password2_input = driver.find_element(By.ID, 'id_password2')

    username_input.send_keys(data[i][1])
    password1_input.send_keys(data[i][2])
    password2_input.send_keys(data[i][2])
    
    # Định vị phần tử button để submit form
    button_submit = driver.find_element(By.XPATH, "/html/body/main/div/div/div[2]/form/button")
    button_submit.click()
    if driver.current_url == url_home:
        report_data = [(i+1), 'Đăng Ký Thành Công!']
        write_data_to_excel(report_data, excel_file_path)
        sleep(2)

        driver.get("http://127.0.0.1:8000/logout/")
    else:
        report_data = [(i+1), 'Đăng Ký Không Thành Công!']
        write_data_to_excel(report_data, excel_file_path)

    driver.get("http://127.0.0.1:8000/register/")

sleep(3)
driver.close()