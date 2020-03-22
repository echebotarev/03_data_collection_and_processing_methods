import requests
from lxml import html

def get_html(url):
  header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
  }

  response = requests.get(
    url,
    headers = header
  ).text

  return html.fromstring(response)