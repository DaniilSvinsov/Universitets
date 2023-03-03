import re
import time
from bs4 import BeautifulSoup
import requests
import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
useragent = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={useragent.random}")
headers = {
    "Accept": '*/*',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
}
driver = webdriver.Chrome(options=options)
driver.get(f"https://tabiturient.ru/vuzu/rudn/proxodnoi/")
time.sleep(1)
WebDriverWait(driver, 0.8).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="vuz16929"]/table[1]'))).click()
time.sleep(1)
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
pars_cost = [f_cost.find_all("span", class_="font2") for f_cost in soup.find_all("div", class_="table-cell-2 topmob2")]
print(pars_cost)
try:
    pars_sub_choice = [i.text for i in list(soup.find("table", class_="cirfloat3 cirfloatalt").find_all("b", class_="font11"))]
except AttributeError:
    pars_sub_choice = []
pars_sub_mandatory = [j.text for j in soup.find("table", class_="cirfloat3").find_parent().find_all("b", class_="font11") if j.text not in pars_sub_choice]
# Баллы связанные по форме обучения
try:
    full = [soup.find("b", id=f"proxans1-id-16929").text] + [soup.find("b", id=f"proxans1-id2-16929").text]
    if full[1] == "Нет данных": full[1] = '0'
    try:
        last_ball = soup.find("td",class_=f"differ1-1-id-16929").next_element.next_element.next_element.find_next("b").text
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
    distant = [soup.find("b", id=f"proxans2-id-16929").text] + [soup.find("b", id=f"proxans2-id2-16929").text]
    if distant[1] == "Нет данных": distant[1] = '0'
    try:
        last_ball_2 = soup.find("td",class_=f"differ1-2-id-16929").next_element.next_element.next_element.find_next("b").text
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
    half = [soup.find("b", id=f"proxans3-id-16929").text] + [soup.find("b", id=f"proxans3-id2-16929").text]
    if half[1] == "Нет данных": half[1] = '0'
    try:
        last_ball_3 = soup.find("td",class_=f"differ1-2-id-16929").next_element.next_element.next_element.find_next("b").text
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
        print({pars[3].text[:30]:pars[3].text[34:],"Балл":full[0],"Балл(2021)":last_ball if full[0] != "NEW" else "Не существовало","Форма обучения": "Очная","Экзамены ЕГЭ":';'.join(pars_sub_mandatory)+";("+"/".join(pars_sub_choice)+")" if len(pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),"Уровень программы":pars[4].text[19:],"Бюджетных мест":full[1],pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n", " ") if len(pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],pars[5].text[:13]: pars[5].text[15:], "Стоимость": cost_full[0],"Олимпиадники": olimp_full[0].split()[0] if len(olimp_full) > 0 else "-", pars[1].text[:13]:pars[1].text[15:]})
    else:
        print({pars[3].text[:30]: pars[3].text[34:], "Балл": full[0],
               "Балл(2021)": last_ball if full[0] != "NEW" else "Не существовало", "Форма обучения": "Очная",
               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
               "Бюджетных мест": full[1],
               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                       " ") if len(
                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
               pars[5].text[:13]: pars[5].text[15:], "Стоимость": "-",
               "Олимпиадники": "-",
               pars[1].text[:13]: pars[1].text[15:]})
if len(distant) > 0:
    if len(cost_distant) != 0:
        print({pars[3].text[:30]: pars[3].text[34:], "Балл": distant[0],"Балл(2021)" : last_ball_2 if distant[0] != "NEW" else "Не существовало","Форма обучения": "Заочная","Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),"Уровень программы":pars[4].text[19:],"Бюджетных мест":distant[1], pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n", " ") if len(pars) >= 7 else "Без профиля",pars[5].text[:13]: pars[5].text[15:], pars[5].text[:13]: pars[5].text[15:],"Стоимость": cost_distant[0],"Олимпиадники":olimp_distant[0].split()[0] if len(olimp_distant) > 0 else "-", pars[1].text[:13]: pars[1].text[15:]})
    else:
        print({pars[3].text[:30]: pars[3].text[34:], "Балл": distant[0],
               "Балл(2021)": last_ball_2 if distant[0] != "NEW" else "Не существовало", "Форма обучения": "Заочная",
               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
               "Бюджетных мест": distant[1],
               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                       " ") if len(
                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
               pars[5].text[:13]: pars[5].text[15:], "Стоимость": "-",
               "Олимпиадники": "-",
               pars[1].text[:13]: pars[1].text[15:]})
if len(half) > 0:
    if len(cost_half) != 0:
        print({pars[3].text[:30]: pars[3].text[34:], "Балл": half[0],"Балл(2021)":last_ball_3 if half[0] != "NEW" else "Не существовало","Форма обучения": "очно-заочная","Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(pars_sub_choice) > 0 else ";".join(pars_sub_mandatory),"Уровень программы":pars[4].text[19:],"Бюджетных мест":half[1], pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n", " ") if len(pars) >= 7 else "Без профиля",pars[5].text[:13]: pars[5].text[15:], pars[5].text[:13]: pars[5].text[15:],"Стоимость": cost_half[0],"Олимпиадники":olimp_half[0].split()[0] if len(olimp_half) > 0 else "-", pars[1].text[:13]: pars[1].text[15:]})
    else:
        print({pars[3].text[:30]: pars[3].text[34:], "Балл": half[0],
               "Балл(2021)": last_ball_3 if half[0] != "NEW" else "Не существовало", "Форма обучения": "очно-заочная",
               "Экзамены ЕГЭ": ';'.join(pars_sub_mandatory) + ";(" + "/".join(pars_sub_choice) + ")" if len(
                   pars_sub_choice) > 0 else ";".join(pars_sub_mandatory), "Уровень программы": pars[4].text[19:],
               "Бюджетных мест": half[1],
               pars[6].text[:17] if len(pars) >= 7 else "Профиль программы": pars[6].text[19:].replace("\n",
                                                                                                       " ") if len(
                   pars) >= 7 else "Без профиля", pars[5].text[:13]: pars[5].text[15:],
               pars[5].text[:13]: pars[5].text[15:], "Стоимость": "-",
               "Олимпиадники": "-",
               pars[1].text[:13]: pars[1].text[15:]})
time.sleep(2)