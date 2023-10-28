import datetime
import requests
from bs4 import BeautifulSoup

def current_day():
    return str(datetime.datetime.utcnow().date())

def parse_to_bs(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return soup

