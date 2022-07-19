import requests
from lxml import html
from collections import Counter
from .celery import app


@app.task(track_started=True)
def parse_page(site_url: str) -> Counter:
    page = requests.get(site_url)
    tree = html.fromstring(page.content)
    tree_elements = tree.cssselect('*')
    elements_tags = [x.tag for x in tree_elements]
    tags_data = Counter(elements_tags)
    return tags_data
