from .helpers import current_day, parse_to_bs


BYBIT_URL_V5 = "https://bybit-exchange.github.io/docs/changelog/v5"

def bybit_check_updates():
    day = current_day()
    page = parse_to_bs(BYBIT_URL_V5)

    '''
        We only care about the first with class 'anchor anchorWithStickyNavbar_LWe7', since it is where is stored the last date.
        
        This is the normal hexadecimal representation of last_day-> 0032 0030 0032 0033 002D 0031 0030 002D 0032 0036 200B
        So we need to remove the '200B' which is a zero width space
        https://www.fileformat.info/info/unicode/char/200b/index.htm

    '''
    last_day = page.find(class_="anchor anchorWithStickyNavbar_LWe7").get_text(strip=True).replace('\u200b', '')

    if day == last_day:
        return BYBIT_URL_V5 + "#" + last_day

    return None
