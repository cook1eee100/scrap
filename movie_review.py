from bs4 import BeautifulSoup
import requests
import csv

movie_url = 'https://movie.naver.com/movie/running/current.nhn'
url = movie_url
movie_code_list = []

movie_response = requests.get(url)
movie_soup = BeautifulSoup(movie_response.text, 'html.parser')

movie_list = movie_soup.select('#content > div.article > div:nth-child(1) > div.lst_wrap > ul > li')
# print(movie_list)

for li in movie_list:
    a_tag = li.select_one('dl > dt > a')
    title = a_tag.text
    code = a_tag['href'].split("code=")[1]
    movie_code_list.append({"title": title, "code": code})
    
# print(movie_code_list)


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
    'cookie': 'NNB=HLGLUBDVW4BF6; MM_NEW=1; NFS=2; MM_NOW_COACH=1; NRTK=ag^#all_gr^#1_ma^#-2_si^#0_en^#0_sp^#0; nx_ssl=2; _fbp=fb.1.1595231225594.634287142; _ga=GA1.1.858167755.1595231225; _ga_4BKHBFKFK0=GS1.1.1595231224.1.1.1595231240.44; page_uid=Uylt3sp0JXVssmK56+lssssssUh-202741; JSESSIONID=08529A81EBA2526D6965A4F8595336A8; NM_VIEWMODE_AUTO=basic; csrf_token=bd0ef5d9-caf2-46f8-861a-8e54c40e722a',
}


for i, code_li in enumerate(movie_code_list):
    params = (
        ('code', movie_code_list[i]['code']),
        ('type', 'after'),
        ('isActualPointWriteExecute', 'false'),
        ('isMileageSubscriptionAlready', 'false'),
        ('isMileageSubscriptionReject', 'false'),
        ('page', '1')
    )
    review_response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
    review_soup = BeautifulSoup(review_response.text, 'html.parser')

    review_list = review_soup.select('body > div > div > div.score_result > ul > li')


    for j, li in enumerate(review_list):
        
        if li.select(f'div.score_reple > p > #_filtered_ment_{str(j)} > span._unfold_ment'):
            review = li.select_one(f'div.score_reple > p > #_filtered_ment_{str(j)} > span._unfold_ment > a')['data-src']
        else:
            review = li.select_one(f'div.score_reple > p > #_filtered_ment_{str(j)}').text.strip()
        title = movie_code_list[i]['title']+''
        score = li.select_one('div.star_score > em').text

        
        print(title, score, review)


    
