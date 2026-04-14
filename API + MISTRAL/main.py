import requests

MISTRAL_API_KEY = 'VCBxQwUcoVfRQOQtsmng9tibMMLXIo1i'
NEWSAPI_KEY = 'b6c6d63e078c436288b59d4cffdfa492'


def get_articles(topic):
    params = {"q": topic, "language": "ru", "sortBy": "publishedAt", "pageSize": 10, "apiKey": NEWSAPI_KEY}
    resp = requests.get("https://newsapi.org/v2/everything", params=params)
    data = resp.json()
    if data.get("status") != "ok":
        return []
    return [{"title": a.get("title", ""), "desc": a.get("description", "")} for a in data.get("articles", []) if a.get("title")]


def get_mistral_annotation(api_key, articles, topic):
    url = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    articles_text = "\n".join(f"{i+1}. {a['title']}. {a['desc']}" for i, a in enumerate(articles))
    prompt = f"Ты аналитик новостей. Тема: {topic}. Проанализируй статьи и напиши аннотацию на русском языке строго 250-300 слов. Выдели ключевые события, тренды и дай оценку ситуации. Статьи:\n{articles_text}\nОтвет только текстом, без вступлений."
    data = {"model": "mistral-small-latest", "messages": [{"role": "user", "content": prompt}], "temperature": 0.3, "max_tokens": 1200}
    resp = requests.post(url, headers=headers, json=data)
    if resp.status_code == 200:
        annotation = resp.json()['choices'][0]['message']['content'].strip()
        with open("text", "w", encoding="utf-8") as f:
            f.write(annotation)
        print(annotation)
        return annotation
    else:
        print(f"Ошибка Mistral: {resp.status_code} — {resp.text}")
        return None


if __name__ == "__main__":
    topic = "технологии и инновации"
    articles = get_articles(topic)
    if articles:
        get_mistral_annotation(MISTRAL_API_KEY, articles, topic)
    else:
        print("Новости не найдены.")