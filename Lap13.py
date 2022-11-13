import urllib.request
from bs4 import BeautifulSoup

url = "http://py4e-data.dr-chuck.net/comments_1430669.html"
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

span_tags = soup.findAll("span")
sum_result = 0 
line_result = 0
for i in span_tags:
    line_result = line_result + 1
    sum_result = sum_result + int(i.text)
print("Sum = {0}".format(sum_result))
print("Line = {0}".format(line_result))