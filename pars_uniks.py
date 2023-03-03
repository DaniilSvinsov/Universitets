import re
from bs4 import BeautifulSoup
import requests
import json
'''url = "///C:/Users/higgo/AppData/Roaming/JetBrains/PyCharmCE2022.2/scratches/index2.html"
req = requests.get(url, headers=headers)
src = req.text
with open("index1.html", "w", encoding="utf-8") as file_1:
    file_1.write(src)
soup = BeautifulSoup(src, "lxml")'''
'''a = ['Москва', 'Москва', 'Spb', 'Ростов-на-дону', 'Нновгород', 'Ekaterinburg', 'Москва', 'Spb', 'Красноярск', 'Москва', 'Tatarstan', 'Москва', 'Москва', 'Ростов-на-дону', 'Москва', 'Владивосток', 'Spb', 'Tatarstan', 'Москва', 'Москва', 'В городе севастополе', 'Ростов-на-дону', 'Сахаякутия', 'Томск', 'Москва', 'Нновгород', 'Москва', 'Новосибирск', 'Samara,', 'Тумэн', 'Bashkortostan', 'Краснодар', 'Челябинск', 'Spb', 'Москва', 'Красноярск', 'Белгородcity in central region russia', 'Воронеж', 'Москва', 'Завивка', 'Spb', 'Ставрополь', 'Spb', 'Spb', 'Москва', 'Архангельск', 'Spb', 'Алтайский край', 'Саратов', 'Samara,', 'Москва', 'Москва', 'Томск', 'Воронеж', 'Омск', 'Калининград', 'Тумэн', 'Завивка', 'Москва', 'Москва', 'Москва', 'Москва', 'Мордовия', 'Москва', 'Киров', 'Иркутск', 'Новосибирск', 'В городе севастополе', 'Tatarstan', 'Bashkortostan', 'Чечня', 'Иркутск', 'Orel', 'Пензаcity in volga region russia', 'Мариэль', 'Тула', 'Новосибирск', 'Мариэль', 'Чувашияrussia_ subjects. kgm', 'Bashkortostan', 'Кемеровоcity in siberia russia', 'Томск', 'Xabarovk', 'Bashkortostan', 'Карелия!', 'Новгород', 'Москва', 'Удмуртия', 'Нновгород', 'Tatarstan', 'Челябинск', 'Москва', 'Москва', 'Оренбургcity in volga region russia', 'Spb', 'Белгородcity in central region russia', 'Vladimir', 'Москва', 'Тамбов', 'Москва', 'Москва', 'Вологда', 'Ekaterinburg', 'Волгоград', 'Москва', 'Волгоград', 'Spb', 'Spb', 'Краснодар', 'Москва', 'Тула', 'Кемеровоcity in siberia russia', 'Ростов-на-дону', 'Нновгород', 'Spb', 'Spb', 'Москва', 'Краснодар', 'Чечня', 'Алтайский край', 'Spb', 'Саратов', 'Курск', 'Красноярск', 'Коми', 'Оренбургcity in volga region russia', 'Дагестан', 'Spb', 'Астрахань', 'Bashkortostan', 'Кабардино-балкария', 'Разан', 'Москва', 'Spb', 'Томск', 'Spb', 'Волгоград', 'Bashkortostan', 'Удмуртия', 'Чечня', 'Samara,', 'Воронеж', 'Алтайский край', 'Ярославль', 'Ростов-на-дону', 'Москва', 'Zabaikal', 'Псков', 'Тверь', 'Москва', 'Москва', 'Бранск', 'Омск', 'Воронеж', 'Новосибирск', 'Новосибирск', 'Ставрополь', 'Xmao', 'Samara,', 'Ярославль', 'Мордовия', 'Челябинск', 'Буратия', 'Ульяновск', 'Кострома', 'Челябинск', 'Разан', 'Воронеж', 'Ингушетия', 'Завивка', 'Ульяновск', 'Ярославль', 'Ульяновск', 'Саратов', 'Омск', 'Вологда', 'Томск', 'Ростов-на-дону', 'Курск', 'Омск', 'Краснодар', 'Дагестан', 'Тываrussia_ subjects. kgm', 'Саратов', 'Ивановоcity in central region russia', 'Москва', 'Калининград', 'Томск', 'Samara,', 'Ekaterinburg', 'Волгоград', 'Омск', 'Калугаcity in central region russia', 'Нновгород', 'Ekaterinburg', 'Москва', 'Кемеровоcity in siberia russia', 'Samara,', 'Ставрополь', 'Саратов', 'Бранск', 'Ekaterinburg', 'Ekaterinburg', 'Омск', 'Spb', 'Tatarstan', 'Дагестан', 'Spb', 'Xmao', 'Разан', 'Xakasia', 'Красноярск', 'Spb', 'Xabarovk', 'Буратия', 'Курск', 'Красноярск', 'Чувашияrussia_ subjects. kgm', 'Кальмукия', 'Samara,', 'Новосибирск', 'Tatarstan', 'Волгоград', 'Москва', 'Тамбов', 'Воронеж', 'Тверь', 'Дагестан', 'Xabarovk', 'Ekaterinburg', 'Новосибирск', 'Тамбов', 'Липецк', 'Челябинск', 'В городе севастополе', 'Тумэн', 'Kurgan', 'Пензаcity in volga region russia', 'Краснодар', 'Ekaterinburg', 'Кемеровоcity in siberia russia', 'Нновгород', 'Краснодар', 'Положение дел в отрасли', 'Москва', 'Владивосток', 'Москва', 'Челябинск', 'Дагестан', 'Удмуртия', 'Tatarstan', 'Нновгород', 'Adugeya', 'Kcr', 'Астрахань', 'Иркутск', 'Мурманск', 'Кемеровоcity in siberia russia', 'Коми', 'Иркутск', 'Оренбургcity in volga region russia', 'Алтайский край', 'Воронеж', 'Ульяновск', 'Adugeya', 'Spb', 'Москва', 'Белгородcity in central region russia', 'Новосибирск', 'Ярославль', 'Spb', 'Завивка', 'Spb', 'Ekaterinburg', 'Алтайский край', 'Удмуртия', 'Алтайский край', 'Новосибирск', 'Удмуртия', 'Нновгород', 'Spb', 'Смоленскrussia_ subjects. kgm', 'Положение дел в отрасли', 'Новосибирск', 'Буратия', 'Kurgan', 'Ивановоcity in central region russia', 'Липецк', 'Иркутск', 'Tatarstan', 'Spb', 'Завивка', 'Омск', 'Архангельск', 'Xabarovk', 'Altairepubric', 'Москва', 'Иркутск', 'Москва', 'Тумэн', 'Краснодар', 'Сахаякутия', 'Владивосток', 'Тверь', 'Москва', 'Вологда', 'Ставрополь', 'Xabarovk', 'Нновгород', 'Краснодар', 'Москва', 'Владивосток', 'Ивановоcity in central region russia', 'Киров', 'Xmao', 'Москва', 'Sakhalin', 'Новосибирск', 'Zabaikal', 'Ивановоcity in central region russia', 'Ульяновск', 'Гамбургwaters_ world- class. kgm', 'Положение дел в отрасли', 'Tatarstan', 'Липецк', 'Spb', 'Гамбургwaters_ world- class. kgm', 'Orel', 'Иркутск', 'Владивосток', 'Положение дел в отрасли', 'Spb', 'Xmao', 'Москва', 'Волгоград', 'Мурманск', 'Чувашияrussia_ subjects. kgm', 'Ярославль', 'Смоленскrussia_ subjects. kgm', 'Пензаcity in volga region russia', 'Разан', 'Смоленскrussia_ subjects. kgm', 'Киров', 'Завивка', 'Москва', 'Кострома', 'Ивановоcity in central region russia', 'Ставрополь', 'Курск', 'Ростов-на-дону', 'Бранск', 'Астрахань', 'Tatarstan', 'Samara,', 'Магадан', 'Оренбургcity in volga region russia', 'Москва', 'Нновгород', 'Москва', 'Spb', 'Kurgan', 'Кабардино-балкария', 'Samara,', 'Уоа:', 'Бранск', 'Белгородcity in central region russia', 'Кемеровоcity in siberia russia', 'Гамбургwaters_ world- class. kgm', 'Spb', 'Алтайский край', 'Orel', 'Челябинск', 'Тверь', 'Красноярск', 'Иркутск', 'Нновгород', 'Нновгород', 'Буратия', 'Tatarstan', 'Москва', 'Владивосток', 'Ростов-на-дону', 'Волгоград', 'Ивановоcity in central region russia', 'Ярославль', 'Камчатка', 'Vladimir', 'Ekaterinburg', 'Тумэн', 'В городе севастополе', 'Смоленскrussia_ subjects. kgm', 'Orel', 'Москва', 'Москва', 'Москва', 'Samara,', 'В городе севастополе', 'Псков', 'Москва', 'Ставрополь', 'Камчатка', 'Сахаякутия', 'Xabarovk', 'Samara,', 'Псков', 'Сахаякутия', 'Xabarovk', 'Завивка', 'Москва', 'Чувашияrussia_ subjects. kgm', 'Москва', 'Москва', 'Xmao', 'Ekaterinburg', 'Spb', 'Курск', 'Москва', 'Spb', 'Москва', 'Завивка', 'Москва', 'Владивосток', 'В городе севастополе', 'Bashkortostan', 'Коми', 'Ростов-на-дону', 'Москва', 'Ekaterinburg', 'Саратов', 'Ekaterinburg', 'Ekaterinburg', 'Tatarstan', 'Tatarstan', 'Челябинск', 'Москва', 'Москва', 'Ярославль', 'Москва', 'Москва', 'Xabarovk', 'Тамбов', 'Москва', 'Москва', 'Карелия!', 'Положение дел в отрасли', 'Новосибирск', 'Омск', 'Москва', 'Смоленскrussia_ subjects. kgm', 'Воронеж', 'Москва', 'Челябинск', 'Spb', 'Москва', 'С открытыми глазами', 'С открытыми глазами', 'С открытыми глазами', 'Vk2', 'Telegram', 'Пользователь 3', 'Login3', 'Грузчик', 'Конверт', 'Пароль', 'Грузчик', 'Vk2', 'Конверт', 'Грузчик']
b = ['moscow', 'moscow', 'spb', 'rostov-on-don', 'nnovgorod', 'ekaterinburg', 'moscow', 'spb', 'krasnoyarsk', 'moscow', 'tatarstan', 'moscow', 'moscow', 'rostov-on-don', 'moscow', 'vladivostok', 'spb', 'tatarstan', 'moscow', 'moscow', 'sevastopol', 'rostov-on-don', 'sahayakutia', 'tomsk', 'moscow', 'nnovgorod', 'moscow', 'novosibirsk', 'samara', 'tumen', 'bashkortostan', 'krasnodar', 'chelyabinsk', 'spb', 'moscow', 'krasnoyarsk', 'belgorod', 'voronez', 'moscow', 'perm', 'spb', 'stavropol', 'spb', 'spb', 'moscow', 'archangelsk', 'spb', 'altayskykray', 'saratov', 'samara', 'moscow', 'moscow', 'tomsk', 'voronez', 'omsk', 'kaliningrad', 'tumen', 'perm', 'moscow', 'moscow', 'moscow', 'moscow', 'mordovia', 'moscow', 'kirov', 'irkutsk', 'novosibirsk', 'sevastopol', 'tatarstan', 'bashkortostan', 'chechna', 'irkutsk', 'orel', 'penza', 'mariel', 'tula', 'novosibirsk', 'mariel', 'chuvashia', 'bashkortostan', 'kemerovo', 'tomsk', 'xabarovk', 'bashkortostan', 'karelia', 'novgorod', 'moscow', 'udmurtia', 'nnovgorod', 'tatarstan', 'chelyabinsk', 'moscow', 'moscow', 'orenburg', 'spb', 'belgorod', 'vladimir', 'moscow', 'tambov', 'moscow', 'moscow', 'vologda', 'ekaterinburg', 'volgograd', 'moscow', 'volgograd', 'spb', 'spb', 'krasnodar', 'moscow', 'tula', 'kemerovo', 'rostov-on-don', 'nnovgorod', 'spb', 'spb', 'moscow', 'krasnodar', 'chechna', 'altayskykray', 'spb', 'saratov', 'kursk', 'krasnoyarsk', 'komi', 'orenburg', 'dagestan', 'spb', 'astrakhan', 'bashkortostan', 'kabardino-balkariya', 'razan', 'moscow', 'spb', 'tomsk', 'spb', 'volgograd', 'bashkortostan', 'udmurtia', 'chechna', 'samara', 'voronez', 'altayskykray', 'yaroslavl', 'rostov-on-don', 'moscow', 'zabaikal', 'pskov', 'tver', 'moscow', 'moscow', 'bransk', 'omsk', 'voronez', 'novosibirsk', 'novosibirsk', 'stavropol', 'xmao', 'samara', 'yaroslavl', 'mordovia', 'chelyabinsk', 'buratia', 'ulyanovsk', 'kostroma', 'chelyabinsk', 'razan', 'voronez', 'ingushetia', 'perm', 'ulyanovsk', 'yaroslavl', 'ulyanovsk', 'saratov', 'omsk', 'vologda', 'tomsk', 'rostov-on-don', 'kursk', 'omsk', 'krasnodar', 'dagestan', 'tyva', 'saratov', 'ivanovo', 'moscow', 'kaliningrad', 'tomsk', 'samara', 'ekaterinburg', 'volgograd', 'omsk', 'kaluga', 'nnovgorod', 'ekaterinburg', 'moscow', 'kemerovo', 'samara', 'stavropol', 'saratov', 'bransk', 'ekaterinburg', 'ekaterinburg', 'omsk', 'spb', 'tatarstan', 'dagestan', 'spb', 'xmao', 'razan', 'xakasia', 'krasnoyarsk', 'spb', 'xabarovk', 'buratia', 'kursk', 'krasnoyarsk', 'chuvashia', 'kalmukia', 'samara', 'novosibirsk', 'tatarstan', 'volgograd', 'moscow', 'tambov', 'voronez', 'tver', 'dagestan', 'xabarovk', 'ekaterinburg', 'novosibirsk', 'tambov', 'lipetsk', 'chelyabinsk', 'sevastopol', 'tumen', 'kurgan', 'penza', 'krasnodar', 'ekaterinburg', 'kemerovo', 'nnovgorod', 'krasnodar', 'soa', 'moscow', 'vladivostok', 'moscow', 'chelyabinsk', 'dagestan', 'udmurtia', 'tatarstan', 'nnovgorod', 'adugeya', 'kcr', 'astrakhan', 'irkutsk', 'murmansk', 'kemerovo', 'komi', 'irkutsk', 'orenburg', 'altayskykray', 'voronez', 'ulyanovsk', 'adugeya', 'spb', 'moscow', 'belgorod', 'novosibirsk', 'yaroslavl', 'spb', 'perm', 'spb', 'ekaterinburg', 'altayskykray', 'udmurtia', 'altayskykray', 'novosibirsk', 'udmurtia', 'nnovgorod', 'spb', 'smolensk', 'soa', 'novosibirsk', 'buratia', 'kurgan', 'ivanovo', 'lipetsk', 'irkutsk', 'tatarstan', 'spb', 'perm', 'omsk', 'archangelsk', 'xabarovk', 'altairepubric', 'moscow', 'irkutsk', 'moscow', 'tumen', 'krasnodar', 'sahayakutia', 'vladivostok', 'tver', 'moscow', 'vologda', 'stavropol', 'xabarovk', 'nnovgorod', 'krasnodar', 'moscow', 'vladivostok', 'ivanovo', 'kirov', 'xmao', 'moscow', 'sakhalin', 'novosibirsk', 'zabaikal', 'ivanovo', 'ulyanovsk', 'amur', 'soa', 'tatarstan', 'lipetsk', 'spb', 'amur', 'orel', 'irkutsk', 'vladivostok', 'soa', 'spb', 'xmao', 'moscow', 'volgograd', 'murmansk', 'chuvashia', 'yaroslavl', 'smolensk', 'penza', 'razan', 'smolensk', 'kirov', 'perm', 'moscow', 'kostroma', 'ivanovo', 'stavropol', 'kursk', 'rostov-on-don', 'bransk', 'astrakhan', 'tatarstan', 'samara', 'magadan', 'orenburg', 'moscow', 'nnovgorod', 'moscow', 'spb', 'kurgan', 'kabardino-balkariya', 'samara', 'eao', 'bransk', 'belgorod', 'kemerovo', 'amur', 'spb', 'altayskykray', 'orel', 'chelyabinsk', 'tver', 'krasnoyarsk', 'irkutsk', 'nnovgorod', 'nnovgorod', 'buratia', 'tatarstan', 'moscow', 'vladivostok', 'rostov-on-don', 'volgograd', 'ivanovo', 'yaroslavl', 'kamchatka', 'vladimir', 'ekaterinburg', 'tumen', 'sevastopol', 'smolensk', 'orel', 'moscow', 'moscow', 'moscow', 'samara', 'sevastopol', 'pskov', 'moscow', 'stavropol', 'kamchatka', 'sahayakutia', 'xabarovk', 'samara', 'pskov', 'sahayakutia', 'xabarovk', 'perm', 'moscow', 'chuvashia', 'moscow', 'moscow', 'xmao', 'ekaterinburg', 'spb', 'kursk', 'moscow', 'spb', 'moscow', 'perm', 'moscow', 'vladivostok', 'sevastopol', 'bashkortostan', 'komi', 'rostov-on-don', 'moscow', 'ekaterinburg', 'saratov', 'ekaterinburg', 'ekaterinburg', 'tatarstan', 'tatarstan', 'chelyabinsk', 'moscow', 'moscow', 'yaroslavl', 'moscow', 'moscow', 'xabarovk', 'tambov', 'moscow', 'moscow', 'karelia', 'soa', 'novosibirsk', 'omsk', 'moscow', 'smolensk', 'voronez', 'moscow', 'chelyabinsk', 'spb', 'moscow', 'eye-open', 'eye-open', 'eye-open', 'vk2', 'telegram', 'user3', 'login3', 'loader', 'envelope', 'password', 'loader', 'vk2', 'envelope', 'loader']
print(dict(zip(b,a)))'''
# Перевести и составить словарь для ускорения
city = {'moscow': 'Москва', 'spb': 'Санкт-Петербрг', 'rostov-on-don': 'Ростов-на-дону', 'nnovgorod': 'Нижний Новгород', 'ekaterinburg': 'Екатеринбург', 'krasnoyarsk': 'Красноярск', 'tatarstan': 'Татарстан', 'vladivostok': 'Владивосток', 'sevastopol': 'Севастополь', 'sahayakutia': 'Якутия', 'tomsk': 'Томск', 'novosibirsk': 'Новосибирск', 'samara': 'Самара', 'tumen': 'Тюмень', 'bashkortostan': 'Башкортостан', 'krasnodar': 'Краснодар', 'chelyabinsk': 'Челябинск', 'belgorod': 'Белгород', 'voronez': 'Воронеж', 'perm': 'Пермь', 'stavropol': 'Ставрополь', 'archangelsk': 'Архангельск', 'altayskykray': 'Алтайский край', 'saratov': 'Саратов', 'omsk': 'Омск', 'kaliningrad': 'Калининград', 'mordovia': 'Мордовия', 'kirov': 'Киров', 'irkutsk': 'Иркутск', 'chechna': 'Чечня', 'orel': 'Орел', 'penza': 'Пенза', 'mariel': 'Мариэль', 'tula': 'Тула', 'chuvashia': 'Чувашия', 'kemerovo': 'Кемерово', 'xabarovk': 'Хабаровск', 'karelia': 'Карелия', 'novgorod': 'Великий Новгород', 'udmurtia': 'Удмуртия', 'orenburg': 'Оренбург', 'vladimir': 'Владимир', 'tambov': 'Тамбов', 'vologda': 'Вологда', 'volgograd': 'Волгоград', 'kursk': 'Курск', 'komi': 'Коми', 'dagestan': 'Дагестан', 'astrakhan': 'Астрахань', 'kabardino-balkariya': 'Кабардино-балкария', 'razan': 'Рязань', 'yaroslavl': 'Ярославль', 'zabaikal': 'Забайкалье', 'pskov': 'Псков', 'tver': 'Тверь', 'bransk': 'Брянск', 'xmao': 'Хмао', 'buratia': 'Бурятия', 'ulyanovsk': 'Ульяновск', 'kostroma': 'Кострома', 'ingushetia': 'Ингушетия', 'tyva': 'Тыва', 'ivanovo': 'Иваново', 'kaluga': 'Калуга', 'xakasia': 'Хакасия', 'kalmukia': 'Калмыкия', 'lipetsk': 'Липецк', 'kurgan': 'Курган', 'soa': 'Северная Осетия', 'adugeya': 'Адыгея', 'kcr': 'Карачаево-Черкесская Республика', 'murmansk': 'Мурманск', 'smolensk': 'Смоленск', 'altairepubric': 'Алтай', 'sakhalin': 'Сахалин', 'amur': 'Амур', 'magadan': 'Магадан', 'eao': 'Биробиджан', 'kamchatka': 'Камчатка'}

headers = {
    "Accept": '*/*',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 YaBrowser/23.1.1.1138 Yowser/2.5 Safari/537.36"
}
with open("index2.html", encoding="utf-8") as file_main:
    src = file_main.read()

soup = BeautifulSoup(src, "lxml")
info = []
pars_name_stud = soup.find("div", id="resultdiv0").find_all("span", class_="font3")
name_stud = [i.text for i in pars_name_stud]
pars_ball = soup.find_all("b", class_="font2", text=re.compile("(\d?)"))[::4]
#print(pars_ball)
avg_ball = [j.text for j in pars_ball]
pars_students = soup.find_all("b", class_="font11", text=re.compile("\d"))
alone_student = pars_students[1::2]
facultet = pars_students[::2]
s_student = [stud.text for stud in alone_student]
result_facultet = [fac.text for fac in facultet]
print(result_facultet)
pars_town = soup.find_all("img", class_="img3")
source_town = [(source["src"].split("/")[-1][:-4]) for source in pars_town]
print(facultet)
# img
'''k = 0    
pars_image = []
pars_logo = soup.find_all("img", class_="vuzlistimg")
for i in pars_logo:
    url_img = i['src']
    req_img = requests.get(url=url_img, headers=headers)
    logo = req_img.content
    pars_image.append(f"logos/{name_stud[k]}.jpg")
    with open(f"logos/{name_stud[k]}.jpg", "wb") as file_img:
        file_img.write(logo)
        if k != len(pars_logo)-1:
            print(f"Осталось картинок {len(pars_logo) - k - 1} из {len(pars_logo)}")
        else:
            print("Ура победа!!!")
    k += 1
print(pars_image)'''
#ввод в json
for i in range(len(name_stud)):
    info += [{"Название": name_stud[i], "Средний балл": float(avg_ball[i]) if avg_ball[i] != '?' and float(avg_ball[i]) < 100 else '?', "Количество мест": s_student[i], "Количество образовательных программ": result_facultet[i],"Город": city[source_town[i]]}]
print(info)
with open("Universitets.json", "w") as file:
    json.dump(info, file, indent=4, ensure_ascii=False)






















































