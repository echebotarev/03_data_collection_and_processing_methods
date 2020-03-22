from get_html import get_html

def get_date(url):
  tree = get_html(url)
  dates = tree.xpath("//span[@class='note__text breadcrumbs__text js-ago']/@datetime")
  return dates[0] if dates else None

def get_mail_data(links, url):
  output = []
  for link in links:
    href = link.xpath('./@href')[0]
    href = href if href.find('http') != -1 else url + href[1:]

    data = {
      'href': href,
      'title': link.xpath('./text()')[0] if link.xpath('./text()') else link.xpath('./span/text()')[0],
      'datetime': get_date(href),
      'newsmaker': 'mail'
    }

    output.append(data)

  return output