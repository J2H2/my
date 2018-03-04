from bs4 import BeautifulSoup


def clean_tag(string: str) -> str:
    if string is None:
        return ''
    return BeautifulSoup(string, 'html.parser').text
