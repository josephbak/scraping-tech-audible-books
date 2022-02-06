# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://www.audible.com/search?keywords=book&node=18573211011&page=1&ref=a_search_c4_pageNum_0&pf_rd_p=1d79b443-2f1d-43a3-b1dc-31a2cd242566&pf_rd_r=2BH9QDWK6AZNJ37XWE3M")
# amazon_webpage = response.text

# soup = BeautifulSoup(amazon_webpage, "html.parser")
# # print(soup.title)

# prices = soup.find_all(name="span", class_="bc-text bc-size-base bc-color-base")
# # print(price)

# # for i in prices:
# #     print(i.getText())
# # print(type(list(prices)))

# print(str(prices[1]))

# new_price = [ele.getText().strip() for ele in prices if "$" in str(ele)]
# print(new_price)
# print(len(new_price))

print("Scrapy and Beautiful Soup are used.")