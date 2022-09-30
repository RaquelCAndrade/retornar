import random

import requests


def get_trend_topics():
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAH%2BjhgEAAAAA5DiYJzVYpqQ9hhha7jvroTKobms%3DVqEVKQlDRuHcBuKm9jfQAnPo38qtG3ThvxZMD5uWJKXCZ2OMoX"

    url = "https://api.twitter.com/1.1/trends/place.json"

    trend_headers = {"Authorization": f"Bearer {bearer_token}"}

    trend_args = {"id": 23424768}

    response = requests.get(url, headers=trend_headers, params=trend_args)

    list_topics = []

    for i in range(0, 10):
        list_topics.append(response.json()[0]["trends"][i])

    return random.choice(list_topics)


def salve_topic():
    topic_to_save = get_trend_topics()
    with open("resultado.txt", "w", encoding="UTF-8") as file:
        file.write(f"O assunto sorteado do dia foi: {topic_to_save['name']}")
