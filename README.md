# Manage Cookies for Scrapy
This library automatically saves cookies 
and allows cookies to be used on the next session.
With this library, you will not need to re-authorize on the site.

# How to usage
In the scrapy project, make sure you are in the folder where located middleware.py. \
Install: \
With repository files: 
```
git clone https://github.com/r1nko/scrapy_manage_cookies ./
```

Without: 
```
wget https://raw.githubusercontent.com/r1nko/scrapy_manage_cookies/main/manage_cookies.py
```

Import to your spider:
```python
from .. import manage_cookies
```

In func where you need use cookies write:
```python
cookies = manage_cookies.get_cookies()
```

In the last func of spider you need to save cookies:
```python
manage_cookies.save_cookies(response)
```

Full example:
```python
import scrapy

from .. import manage_cookies


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        cookies = manage_cookies.get_cookies()
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse, cookies=cookies)

    def parse(self, response):
        manage_cookies.save_cookies(response)
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```


