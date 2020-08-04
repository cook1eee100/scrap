from bs4 import BeautifulSoup
import requests
import csv

movie_list_url = 'https://movie.naver.com/movie/running/current.nhn'

URL = movie_list_url
movie_list = []

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')


movie_code_list = soup.select('div.basic > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul.lst_detail_t1 > li')

# print(movie_code_list)

for hr in movie_code_list:
    a_tag = hr.select_one('dl > dt > a')
    movie_list.append({'title': a_tag.text, 'code': a_tag['href'].split("code=")[1]})


for l in movie_list:
    print(l)

with open("movie_data.csv", "w", newline="") as csvfile:
    fieldnames = ['title', 'code']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    for l in movie_list:
        csvwriter.writerow(l)
