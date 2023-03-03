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
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
headers = {
    "Accept": '*/*',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
}
#Входные данные прошлых парсов
#vuz_facultets2 = [68, 38, 103, 91, 41, 23, 38, 77, 63, 52, 61, 76, 92, 13, 41, 84, 29, 73, 17, 84, 107, 86, 79, 42, 82, 66, 52, 81, 107, 73, 77, 29, 70, 133, 60, 61, 54, 49, 90, 78, 80, 34, 97, 50, 36, 70, 25, 105, 51, 110, 93, 51, 45, 62, 97, 20, 32, 53, 36, 145, 37, 40, 31, 33, 54, 52, 87, 64, 46, 59, 37, 25, 72, 40, 37, 32, 69, 77, 38, 66, 59, 36, 49, 51, 23, 78, 22, 55, 8, 68, 16, 11, 8, 10, 48, 51, 41, 43, 39, 52, 7, 60, 77, 54, 21, 70, 46, 49, 23, 29, 21, 10, 36, 22, 38, 36, 47, 72, 71, 66, 48, 12, 53, 55, 21, 33, 48, 68, 7, 64, 40, 40, 34, 60, 25, 40, 58, 5, 44, 49, 38, 72, 36, 16, 57, 50, 8, 53, 54, 5, 32, 18, 8, 36, 18, 60, 11, 44, 42, 51, 21, 54, 28, 7, 20, 10, 8, 14, 43, 19, 20, 26, 7, 6, 53, 53, 10, 28, 42, 21, 21, 28, 49, 29, 5, 63, 45, 47, 8, 71, 54, 38, 5, 51, 29, 63, 13, 17, 12, 5, 34, 46, 19, 35, 24, 26, 6, 9, 25, 30, 40, 6, 29, 30, 32, 9, 22, 25, 7, 39, 47, 88, 14, 31, 65, 20, 7, 20, 44, 25, 39, 3, 22, 22, 29, 40, 44, 26, 43, 24, 32, 54, 45, 8, 22, 4, 6, 5, 13, 8, 36, 7, 38, 37, 17, 29, 22, 8, 4, 19, 99, 22, 31, 6, 9, 32, 46, 39, 25, 30, 3, 28, 15, 24, 5, 34, 35, 14, 49, 40, 14, 50, 24, 44, 22, 19, 37, 6, 14, 17, 32, 18, 15, 8, 20, 11, 19, 3, 32, 18, 22, 19, 7, 9, 18, 15, 36, 17, 13, 43, 18, 16, 1, 26, 13, 23, 19, 33, 25, 35, 32, 2, 6, 63, 25, 21, 16, 12, 20, 10, 22, 34, 10, 3, 12, 30, 29, 34, 10, 14, 11, 23, 19, 27, 10, 6, 8, 16, 28, 10, 42, 24, 3, 13, 23, 17, 17, 46, 11, 5, 21, 3, 27, 19, 9, 4, 1, 5, 2, 4, 5, 5, 83, 6, 1, 11, 9, 6, 7, 24, 9, 4, 9, 18, 10, 15, 44, 23, 2, 16, 3, 15, 9, 4, 5, 50, 8, 20, 4, 11, 6, 2, 0, 25, 10, 16, 9, 1]

vuz_facultets = [24, 9, 4, 9, 18, 10, 15, 44, 23, 2, 16]
itog = ['rostcons', 'mosconsv', 'egti', 'sarcons', 'usaaa', 'uralconsv', 'kazancons', 'sportacadem', 'magkmusic', 'marhi', 'vgik']
result = []# пироговку надо бы а то грустненько
for vuz in range(len(vuz_facultets)):
    if vuz_facultets[vuz] > 25 and not(itog[vuz] in ("kuzstu", "stgau", "bsaa", "pgusa", "tumgik")):
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://tabiturient.ru/vuzu/{itog[vuz]}/proxodnoi/")
        time.sleep(1)
        WebDriverWait(driver, 1.3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rezspec > div.mobpadd20.morediv > div > div'))).click()
        time.sleep(2.1)
        page = driver.page_source
        with open("index3.html", "w", encoding="utf-8") as file_3:
            file_3.write(page)
        with open("index3.html", encoding="utf-8") as file_main:
            src = file_main.read()
            soup = BeautifulSoup(src, "lxml")
    else:
        url = f"https://tabiturient.ru/vuzu/{itog[vuz]}/proxodnoi/"
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
    s = soup.find_all("div", class_="mobpadd20-3")
    number_vuz = []
    for i in s:
        number_vuz.append(i["id"][3:])
    const_vuz = soup.find("h2", class_="font4m fontshadow").next_element.next_element.next_element.text
    # через парс index2.html и выводом названий картинок
    '''for i in itog:
        url = f"https://tabiturient.ru/vuzu/{i}/proxodnoi/"
        req = requests.get(url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")
        pars_balliki = soup.find_all("span", class_="font11", text=re.compile("\d"))[1::2]
        print(pars_balliki)'''
    for id in number_vuz:
        driver = webdriver.Chrome(options=options)
        driver.get(f"https://tabiturient.ru/vuzu/{itog[vuz]}/proxodnoi/")
        #print(driver.find_element(By.XPATH, '//*[@id="resultdivshowmoreinfo"]/div[1]').text)
        time.sleep(0.7)
        if number_vuz.index(id) >= 25:
            WebDriverWait(driver, 1.2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rezspec > div.mobpadd20.morediv > div > div > center > img'))).click()
            time.sleep(2.5)
        WebDriverWait(driver, 1.2).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="vuz{id}"]/table[1]'))).click()
        time.sleep(3)
        page = driver.page_source
        with open("index3.html", "w", encoding="utf-8") as file_3:
            file_3.write(page)
        with open("index3.html", encoding="utf-8") as file_main:
            src = file_main.read()
        soup = BeautifulSoup(src, "lxml")
        #pars_cost = soup.find("span", class_="font2", text=re.compile("Бакалавриат | \d")).text
        #pars_cost = soup.find_all("span", class_="font2", text=re.compile("Бакалавриат | \d"))
        fack = []
        pars = soup.find("div", class_="bg1 bg1-2 p40 pm40").find_all("span", class_="font2")
        #парс стоимость всех программ
        pars_cost = [f_cost.find_all("span", class_="font2") for f_cost in soup.find_all("div", class_="table-cell-2 topmob2")]
        cost, olimp = [], []
        for i in pars_cost[0]:
            check_cost = "".join(str(i).split("<b>")[1].split("</b>")[0])
            if check_cost.isdigit():
                cost.append(check_cost)
            else:
                olimp.append(check_cost)
        try:
            pars_sub_choice = [i.text for i in list(soup.find("table", class_="cirfloat3 cirfloatalt").find_all("b", class_="font11"))]
        except AttributeError:
            pars_sub_choice = []
        pars_sub_mandatory = [j.text for j in soup.find("table", class_="cirfloat3").find_parent().find_all("b", class_="font11") if j.text not in pars_sub_choice]
        # Баллы связанные по форме обучения
        try:
            pars_sub_choice = [i.text for i in
                               list(soup.find("table", class_="cirfloat3 cirfloatalt").find_all("b", class_="font11"))]
        except AttributeError:
            pars_sub_choice = []
        pars_sub_mandatory = [j.text for j in
                              soup.find("table", class_="cirfloat3").find_parent().find_all("b", class_="font11") if
                              j.text not in pars_sub_choice]
        # Баллы связанные по форме обучения
        try:
            full = [soup.find("b", id=f"proxans1-id-{id}").text] + [soup.find("b", id=f"proxans1-id2-{id}").text]
            if full[1] == "Нет данных": full[1] = '0'
            try:
                last_ball = soup.find("td",
                                      class_=f"differ1-1-id-{id}").next_element.next_element.next_element.find_next(
                    "b").text
                if last_ball[1:].isdigit() and full[0].isdigit():
                    if last_ball[0] == "-":
                        last_ball = abs(int(last_ball)) + int(full[0])
                    else:
                        last_ball = int(full[0]) - int(last_ball[1:])
                elif last_ball[1:].isdigit():
                    last_ball = abs(int(last_ball))
                else:
                    last_ball = "Только платное"
            except:
                last_ball = "-"
            # парс стоимость всех программ
            cost_full, olimp_full = [], []
            for i in pars_cost[0]:
                check_cost = "".join(str(i).split("<b>")[1].split("</b>")[0])
                if check_cost.isdigit():
                    cost_full.append(check_cost)
                else:
                    olimp_full.append(check_cost)
            c = pars_cost.pop(0)
        except:
            full = []
            last_ball = "-"
            cost_full, olimp_full = ['Информация не предоставлена'], []
        try:
            distant = [soup.find("b", id=f"proxans2-id-{id}").text] + [soup.find("b", id=f"proxans2-id2-{id}").text]
            if distant[1] == "Нет данных": distant[1] = '0'
            try:
                last_ball_2 = soup.find("td",
                                        class_=f"differ1-2-id-{id}").next_element.next_element.next_element.find_next(
                    "b").text
                if last_ball_2[1:].isdigit() and distant[0].isdigit():
                    if last_ball_2[0] == "-":
                        last_ball_2 = abs(int(last_ball_2)) + int(distant[0])
                    else:
                        last_ball_2 = int(distant[0]) - int(last_ball_2[1:])
                elif last_ball_2[1:].isdigit():
                    last_ball_2 = abs(int(last_ball_2))
                else:
                    last_ball_2 = "Только платное"
            except:
                last_ball_2 = "-"
            # парс стоимость всех программ
            pars_cost_distant = [f_cost.find_all("span", class_="font2") for f_cost in
                                 soup.find_all("div", class_="table-cell-2 topmob2")]
            cost_distant, olimp_distant = [], []
            for i in pars_cost[0]:
                check_cost = "".join(str(i).split("<b>")[1].split("</b>")[0])
                if check_cost.isdigit():
                    cost_distant.append(check_cost)
                else:
                    olimp_distant.append(check_cost)
            c = pars_cost.pop(0)
        except:
            distant = []
            last_ball_2 = "-"
            cost_distant, olimp_distant = ['Информация не предоставлена'], []
        try:
            half = [soup.find("b", id=f"proxans3-id-{id}").text] + [soup.find("b", id=f"proxans3-id2-{id}").text]
            if half[1] == "Нет данных": half[1] = '0'
            try:
                last_ball_3 = soup.find("td",
                                        class_=f"differ1-2-id-{id}").next_element.next_element.next_element.find_next(
                    "b").text
                if last_ball_3[1:].isdigit() and half[0].isdigit():
                    if last_ball_3[0] == "-":
                        last_ball_3 = abs(int(last_ball_3)) + int(half[0])
                    else:
                        last_ball_3 = int(half[0]) - int(last_ball_3[1:])
                elif last_ball_3[1:].isdigit():
                    last_ball_3 = abs(int(last_ball_3))
                else:
                    last_ball_3 = "-"
            except:
                last_ball_3 = "Только платное"
            cost_half, olimp_half = [], []
            for i in pars_cost[0]:
                check_cost = "".join(str(i).split("<b>")[1].split("</b>")[0])
                if check_cost.isdigit():
                    cost_half.append(check_cost)
                else:
                    olimp_half.append(check_cost)
            c = pars_cost.pop(0)
        except:
            half = []
            last_ball_3 = "-"
            cost_half, olimp_half = ['Информация не предоставлена'], []
        if len(full) > 0:
            if len(cost_full) != 0:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": full[0],
                       "Балл(2021)": last_ball if full[0] != "NEW" else "Не существовало", "Форма обучения": "Очная",
                       "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                           pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
                       "Бюджетных мест": full[1],
                       pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                               " ") if len(
                           pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                       pars[5].text[:13]: pars[5].text[15:], "Стоимость": cost_full[0],
                       "Олимпиадники": olimp_full[0].split()[0] if len(olimp_full) > 0 else "-", "Вуз": const_vuz,
                       pars[1].text[:13]: pars[1].text[15:]})
            else:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": full[0],
                               "Балл(2021)": last_ball if full[0] != "NEW" else "Не существовало",
                               "Форма обучения": "Очная",
                               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(
                                   pars_sub_choice) + ")" if len(
                                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),
                               "Уровень программы": pars[4].text[19:],
                               "Бюджетных мест": full[1],
                               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace(
                                   "\n",
                                   " ") if len(
                                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                               pars[5].text[:13]: pars[5].text[15:], "Стоимость": "-",
                               "Олимпиадники": "-",
                               "Вуз": const_vuz,
                               pars[1].text[:13]: pars[1].text[15:]})
        if len(distant) > 0:
            if len(cost_distant) != 0:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": distant[0],
                       "Балл(2021)": last_ball_2 if distant[0] != "NEW" else "Не существовало", "Форма обучения": "Заочная",
                       "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                           pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
                       "Бюджетных мест": distant[1],
                       pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                               " ") if len(
                           pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                       pars[5].text[:13]: pars[5].text[15:], "Стоимость": cost_distant[0],
                       "Олимпиадники": olimp_distant[0].split()[0] if len(olimp_distant) > 0 else "-", "Вуз": const_vuz,
                       pars[1].text[:13]: pars[1].text[15:]})
            else:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": distant[0],
                               "Балл(2021)": last_ball_2 if distant[0] != "NEW" else "Не существовало",
                               "Форма обучения": "Заочная",
                               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(
                                   pars_sub_choice) + ")" if len(
                                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),
                               "Уровень программы": pars[4].text[19:],
                               "Бюджетных мест": distant[1],
                               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace(
                                   "\n",
                                   " ") if len(
                                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                               pars[5].text[:13]: pars[5].text[15:], "Стоимость":"-",
                               "Олимпиадники": "-",
                               "Вуз": const_vuz,
                               pars[1].text[:13]: pars[1].text[15:]})
        if len(half) > 0:
            if len(cost_half) != 0:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": half[0],
                       "Балл(2021)": last_ball_3 if half[0] != "NEW" else "Не существовало",
                       "Форма обучения": "очно-заочная",
                       "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                           pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
                       "Бюджетных мест": half[1],
                       pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                               " ") if len(
                           pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                       pars[5].text[:13]: pars[5].text[15:], "Стоимость": cost_half[0],
                       "Олимпиадники": olimp_half[0].split()[0] if len(olimp_half) > 0 else "-", "Вуз": const_vuz,
                       pars[1].text[:13]: pars[1].text[15:]})
            else:
                result.append({pars[3].text[:30]: pars[3].text[34:], "Балл": half[0],
                               "Балл(2021)": last_ball_3 if half[0] != "NEW" else "Не существовало",
                               "Форма обучения": "очно-заочная",
                               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(
                                   pars_sub_choice) + ")" if len(
                                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),
                               "Уровень программы": pars[4].text[19:],
                               "Бюджетных мест": half[1],
                               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace(
                                   "\n",
                                   " ") if len(
                                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
                               pars[5].text[:13]: pars[5].text[15:], "Стоимость": "-",
                               "Олимпиадники": "-",
                               "Вуз": const_vuz,
                               pars[1].text[:13]: pars[1].text[15:]})
        print(result)
        time.sleep(1)