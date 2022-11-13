import urllib.request
import xml.etree.ElementTree as ET
url = "http://py4e-data.dr-chuck.net/comments_1430671.xml"
data = urllib.request.urlopen(url).read()
tree = ET.fromstring(data)
list_of_comment = tree.findall("comments/comment")
sum_of_comments_number = 0
for item in list_of_comment:
    name_item = item.find("name").text
    comment_count_item = item.find("count").text
    sum_of_comments_number = sum_of_comments_number + int(comment_count_item)
    print(str(name_item) + ": " + str(comment_count_item))
print("The sum number of all comments: " + str(sum_of_comments_number))