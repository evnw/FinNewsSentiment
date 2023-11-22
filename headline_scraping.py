import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import pandas as pd

# r = requests.get('https://www.google.com/search?q=aapl&tbs=cdr%3A1%2Ccd_min%3A11%2F20%2F2023%2Ccd_max%3A11%2F20%2F2023&tbm=nws')


def get_headlines(ticker, day, month, year, num_headings=6):
    start_date = datetime(year,month,day)
    end_date = datetime(year,month,day) + timedelta(days=1)

    endpoint = f"https://www.google.com/search?q=\"{ticker}\"+after%3A{start_date.year}%2F{start_date.month}%2F{start_date.day}+before%3A{end_date.year}%2F{end_date.month}%2F{end_date.day}&tbm=nws"
    r = requests.get(endpoint)
    soup = BeautifulSoup(r.text, 'html.parser')

    return [[heading.get_text(), ticker, f"{day}/{month}/{year}"] for heading in soup.find_all('h3')[0:num_headings]]

def get_historic(start, end):
    headings = []
    headings += get_headlines('aapl', 10, 10, 2023)
    headings += get_headlines('googl', 10, 10, 2023)
    headings = pd.DataFrame(headings, columns=['headline', 'ticker', 'date'])
    print(headings)