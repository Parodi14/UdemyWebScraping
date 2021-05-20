headers = {

    "referer": "https://www.udemy.com/courses/search/?src=ukw&q=python",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36",
}

for i in range (1,4):
    url_api = 'https://www.udemy.com/api-2.0/search-courses/?fields[locale]=simple_english_title&src=ukw&q=python&p=' + str(i

    response = requests.get(url_api, headers=headers)

data = response.json()

cursos = data ["cursos"]
for curso in cursos:
    print(curso["tittle"])
    print(curso["num_reviews"])
    print(curso["rating"])

    input()




