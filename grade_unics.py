import time
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
result = []
uniks =['spbpsysoc', 'mgu', 'chifk', 'nes', 'dvart', 'sevmsu', 'bagsurb', 'krags', 'rostcons', 'mosconsv', 'egti', 'sarcons', 'usaaa', 'uralconsv', 'kazancons', 'sportacadem', 'magkmusic', 'marhi', 'vgik', 'theatrinsyar', 'gitis', 'asou', 'dvgafk', 'rachmaninov', 'rgufksmit', 'mguu', 'glazunovcons', 'sogpi', 'nsuada', 'sibsport', 'litinstitut', 'sgiismol', 'vgifk', 'ippolitovka', 'uralgufk', 'lesgaft', 'agprf']
try:
    #Перебор всех вузов
    for i in uniks:
        main_grade, add_grade = "Оценка отсутствует", "Оценка отсутствует"
        url = f"https://tabiturient.ru/vuzu/{i}/about/"
        useragent = UserAgent()
        options = webdriver.ChromeOptions()
        options.add_argument(f"user-agent={useragent.random}")
        headers = {
            "Accept": '*/*',
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
        }
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(2)
        page = driver.page_source
        # Выгруженный html код страницы записывается в файл
        with open("index4.html", "w", encoding="utf-8") as file_3:
            file_3.write(page)
        with open("index4.html", encoding="utf-8") as file_main:
            src = file_main.read()
            soup = BeautifulSoup(src, "lxml")
        #Парсинг инфы
        name_uniks = soup.find_all("h2", class_="font4m fontshadow")[1].text
        if soup.find("td", class_="ocenka") != None:
            main_grade = soup.find("b", class_="font5").text
        grade_all = soup.find_all("span", class_="font3")
        #Проверка на нужные данные(Оценки, а не другая информация)
        if len(grade_all) < 7:
            grade_all = "Оценка отсутствует"
        else:
            add_grade = soup.find_all("b", class_="font4")
        time.sleep(1)
        #Запись в результирующую переменную
        if grade_all != "Оценка отсутствует":
            result.append({"Вуз": name_uniks, "Общая оценка вуза":main_grade, "Состояние и оснащение корпусов вуза":grade_all[0].text, "Удобство расположения корпусов вуза": grade_all[2].text, "Качество образования":grade_all[4].text, "Качество работы административного аппарата":grade_all[5].text, "Дополнительные активности в вузе":grade_all[8].text, "Качество общепита": grade_all[10].text,"Средняя стоимость обеда в столовой":add_grade[0].text, "Средние затраты на дорогу в месяц":add_grade[1].text})
        elif main_grade.isdigit():
            result.append({"Вуз": name_uniks, "Общая оценка вуза":main_grade})
    #Запись в json
    with open("grades.json", "a") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
except:
    with open("grades.json", "w") as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    print(result)




