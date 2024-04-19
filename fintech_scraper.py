from bs4 import BeautifulSoup
import requests

# se_apprentice_fintech = requests.get("https://www.linkedin.com/jobs/search/?currentJobId=3849870181&distance=25&f_E=1%2C2&f_I=6%2C43&geoId=103644278&keywords=apprenticeship%20software%20engineer&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true")

page_to_scrape = requests.get('http://quotes.toscrape.com')
soup = BeautifulSoup(page_to_scrape.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

for quote, author in zip(quotes, authors):
    print(quote.text + '-' + author.text)