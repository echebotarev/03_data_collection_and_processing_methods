from get_html import get_html

main_link = 'https://yandex.ru/'

def get_date(url):
  tree = get_html(url)
  dates = tree.xpath("//time[@class='g-date']/@datetime")
  return dates[0] if dates else None

def get_yandex_data(links):
  output = []
  for link in links:
    href = link.xpath('./@href')[0]
    href = href if href and href.find('http') != -1 else main_link + href[1:]

    data = {
      'href': href,
      'title': link.xpath('./text()')[0],
      'datetime': None,
      'newsmaker': 'yandex'
    }

    output.append(data)

  return output