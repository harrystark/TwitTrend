import requests
from bs4 import BeautifulSoup


def currentTrends(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'html.parser')
    trend_cards = soup.find_all("ol", {"class":"trend-card__list"})
    trends = []
    for card in trend_cards:
        trend = getTrendsFromCard(card)
        trends.append(trend)
    return trends;

def getTrendsFromCard(card):
    trends = card.find_all("a")
    output = []
    trend = ()
    for t in trends:
        t = (t.get_text(), t["href"])
        output.append(t)
    return output

# def 
if __name__ == "__main__":
    trend = currentTrends("https://trends24.in/india/")
    print(trend)