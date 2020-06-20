import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify())

list(soup.children)

for item in list(soup.children):
    #print(item)

html = list(soup.children)[2]

list(html.children)

body = list(html.children)[3]

list(body.children)

p = list(body.children)[1]

p.get_text()

soup.find_all('p')

soup.find_all('p')[0].get_text()

soup.find('p')

page2 = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page2.content, 'html.parser')


<p class="inner-text first-item" id="first">

<p class="inner-text">

<p class="outer-text first-item" id="second">

<p class="outer-text">

soup.find_all('p', class_='outer-text')

soup.find_all(class_="outer-text")

soup.find_all(id="first")

soup.select("div p")

page3 = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page3.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()

#print(period)
#print(short_desc)
#print(temp)

period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]

short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
#print(short_descs)
#print(temps)
#print(descs)

import pandas as pd
weather = pd.DataFrame({
        "period": periods,
         "short_desc": short_descs,
         "temp": temps,
         "desc":descs
    })



temp_nums = weather["temp"].str.extract("(?P<temp_num>\d+)", expand=False)
weather["temp_num"] = temp_nums.astype('int')
temp_nums

weather["temp_num"].mean()

is_night = weather["temp"].str.contains("Low")
weather["is_night"] = is_night
is_night

weather[is_night]