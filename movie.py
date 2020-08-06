from bs4 import BeautifulSoup
import requests
import csv

movie_list_url = 'https://movie.naver.com/movie/running/current.nhn'

URL = movie_list_url
movie_list = []

moive_response = requests.get(URL)
movie_soup = BeautifulSoup(moive_response.text, 'html.parser')


movie_code_list = movie_soup.select('div.basic > div[id=container] > div[id=content] > div.article > div.obj_section > div.lst_wrap > ul> li')
# movie_soup.select(#content > div.article > div.obj_section > div.lst_wrap > ul > li)

# print(movie_code_list)

for hr in movie_code_list:
    a_tag = hr.select_one('dl > dt > a')
    movie_list.append({'title': a_tag.text, 'code': a_tag['href'].split("code=")[1]})
        # a_tag.get_text
        # a_tag.contents[0]

# for l in movie_list:
#     print(l)

# with open("movie_data.csv", "w", newline="") as csvfile:
#     fieldnames = ['title', 'code']
#     csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     for l in movie_list:
#         csvwriter.writerow(l)



# for movie in movie_list:
#     movie_code = movie['code']
#     review_url = f'https://movie.naver.com/movie/bi/mi/point.nhn?code={movie_code}#tab'
#     review_response = requests.get(review_url)
#     review_soup = BeautifulSoup(review_response.text, "html.parser")
    
#     print(review_soup.select('body > div > div > div.score_result > ul'))




headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=HLGLUBDVW4BF6; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NRTK=ag^#all_gr^#1_ma^#-2_si^#0_en^#0_sp^#0; nx_ssl=2; _fbp=fb.1.1595231225594.634287142; _ga=GA1.1.858167755.1595231225; _ga_4BKHBFKFK0=GS1.1.1595231224.1.1.1595231240.44; page_uid=Uylt3sp0JXVssmK56+lssssssUh-202741; JSESSIONID=C44EADA69BA02BE5DBAB69EE8805D335; NM_VIEWMODE_AUTO=basic; csrf_token=9e05ca1d-8293-4a1d-b66f-13cbce90ae60',
}

params = (
    ('code', '189069'),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)



review_response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
review_soup = BeautifulSoup(review_response.text, 'html.parser')

review_list = review_soup.select('body > div > div > div.score_result > ul> li')

# print(len(review_list))


for i, li in enumerate(review_list):
    rating = li.select_one(f'div.star_score > em')
    review = li.select_one(f'div.score_reple > p > #_filtered_ment_{str(i)}')
    print(rating.text, review.text.strip())
