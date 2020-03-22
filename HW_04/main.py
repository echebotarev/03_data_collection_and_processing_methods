from pprint import pprint

from HW_03.Mongo import Mongo
mongo = Mongo('news')

from get_html import get_html
from get_mail_data import get_mail_data
from get_lenta_data import get_lenta_data
from get_yandex_data import get_yandex_data

newsmaker_links = {
  'mail': 'https://news.mail.ru/',
  'lenta': 'https://lenta.ru/parts/news/',
  'yandex': 'https://yandex.ru/news/'
}

def get_links(html, newsmaker):
  match = {
    'mail': "//a[@class='list__text']|//a[contains(@class, 'newsitem__title')]|//a[contains(@class, 'link link_flex')]",
    'lenta': "//h3/a|//div[@class='item']/a",
    'yandex': "//h2[@class='story__title']/a"
  }

  return html.xpath(match[newsmaker])

def get_data(links, newsmaker):
  result = None
  if newsmaker == 'mail':
    result = get_mail_data(links, newsmaker_links[newsmaker])
  elif newsmaker == 'lenta':
    result = get_lenta_data(links)
  elif newsmaker == 'yandex':
    result = get_yandex_data(links)

  return result


result = []
for key in newsmaker_links:
  tree = get_html(newsmaker_links[key])
  links = get_links(tree, key)

  result.extend(get_data(links, key))

mongo.set_many(result)
pprint(result)

