from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "lxml")

# Get the text from all of the articles
articles = soup.select("span.titleline > a")

article_titles = []
article_links = []

for article in articles:
  article_titles.append(article.getText())
  article_links.append(article.get("href"))

article_updoots = [int(score.getText().split()[0]) for score in soup.select(".score")]

highest_doot = max(article_updoots)
print(f"Title: {article_titles[article_updoots.index(highest_doot)]}")
print(f"Link: {article_links[article_updoots.index(highest_doot)]}")
print(f"Score: {highest_doot}")



# with open("website.html") as file:
#   contents = file.read()

# soup = BeautifulSoup(contents, "lxml")

# print(soup.title.string)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#   # print(tag.getText())
#   print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# headings = soup.select(".heading")
# print(headings)


