import requests
from twilio.rest import Client

account_sid = "your account sid"
auth_token = "your auth token"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?symbol=IBM&apikey=demo"
STOCK_API_KEY = "your api key"
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "your api key"
news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
    "sortBy": "publishedAt",
    "pageSize": 3,
    "page": 1
}


def get_news():
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()

    articles = response.json()["articles"]
    three_articles = articles[:3]
    formatted_articles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in
                          three_articles]

    for article in formatted_articles:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=article,
            from_="+13126516779",
            to="+5517996013875"
        )


def get_stocks_info():
    response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in data.items()]

    yesterday = data_list[0]
    yesterday_closing_price = float(yesterday["4. close"])

    day_before_yesterday = data_list[1]
    day_before_yesterday_closing_price = float(day_before_yesterday["4. close"])

    difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)
    if difference > yesterday_closing_price * 0.05:
        get_news()
