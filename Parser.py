from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests
import xlwt

def parse():
    url = 'https://www.chitai-gorod.ru/' # передаем необходимый URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4
    block = soup.findAll('div', class_='product-title__head') # находим контейнер с нужным классом
    block1 = soup.findAll('div', class_='product-title__author')  # находим контейнер с нужным классом
    block2 = soup.findAll('div', class_='product-price__value product-price__value--discount')  # находим  контейнер с нужным классом
    description = ''
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Test')
    count = 1
    ws.write(count, 1, 'Название книги')
    ws.write(count, 2, 'Автор')
    ws.write(count, 3, 'Цена')

    def process_data(block, column):
        nonlocal count
        for data in block:
            description = data.text
            description = description.replace("\r", "")
            description = description.replace("\n", "")
            description = description.rstrip()
            description = description.lstrip()
            print(description)
            ws.write(count + 1, column, description)
            count += 1

    process_data(block, 1)
    count = 1
    process_data(block1, 2)
    count = 1
    process_data(block2, 3)
    wb.save('C:/Users/Рома/Desktop/output.xls')
parse()