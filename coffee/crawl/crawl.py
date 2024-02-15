import requests
from bs4 import BeautifulSoup
from coffee.models import Product

# 일리가 사이트 크롤링


# def coffee_crawl():
#     r = requests.get(
#         "https://smartstore.naver.com/tiffanyshoes/category/66b4d3e8680349b2891c8ef5f30d0145?cp=1"
#     )
#     # soup = BeautifulSoup(r.text, "lxml" )
#     soup = BeautifulSoup(r.text, "html.parser")

#     coffee_list = soup.select("ul._3ba8S41U2S.tCv2enlAmw li")

#     for idx, item in enumerate(coffee_list, start=1):
#         # 상품명
#         pname = item.select_one("strong._16P0LCXnI1").text

#         # 가격
#         price = item.select_one("strong._24X3qV1tN4 span._3XLnd6iWP5").text

#         # 상품 설명
#         pinfo = item.select_one("p._2wkBtsgL3d").text

#         # 제품 사진
#         pic = item.select_one("img._25CKxIKjAk")["src"]

#         # print(idx,pname,price,pinfo,pic)
#         p = Product(name=pname, price=price, src=pic, description=pinfo)
#         p.save()


# def coffee_crawl():
#     r = requests.get(
#         "https://smartstore.naver.com/coffeespeakskorea/category/1f18a0b616874e2b8e5ca1e8e0aad0d5?cp=1"
#     )


# soup = BeautifulSoup(r.text, "html.parser")

# speaks_list = soup.select("ul.wOWfwtMC_3.FR2H3hWxUo li")

# # print(speaks_list)
# for idx, item in enumerate(speaks_list, start=1):
#     # 상품명
#     pname = item.select_one("strong._26YxgX-Nu5").text
#     # 상품 가격
#     price = item.select_one("strong.zOuEHIx8DC span._2DywKu0J_8").text
#     # 상품 설명
#     pinfo = item.select_one("p._1enCFJskWo").text
#     # 상품 이미지
#     pic = item.select_one("img._25CKxIKjAk")["src"]

#     # print(idx,pname,price,pinfo,pic)
#     p = Product(name=pname, price=price, src=pic, description=pinfo)
#     p.save()


# 커피용품 크롤링
# def coffee_crawl():
#     r = requests.get(
#         "https://smartstore.naver.com/kitchenchois/category/0018ac2fab384df2861be101b956dce8?cp=1"
#     )

#     soup = BeautifulSoup(r.text, "html.parser")

#     acc_list = soup.select("ul.wOWfwtMC_3._3cLKMqI7mI li")

#     # print(acc_list)
#     for idx, item in enumerate(acc_list, start=1):
#         # 상품명
#         pname = item.select_one("strong._26YxgX-Nu5").text
#         # 상품 가격
#         price = item.select_one("span._2DywKu0J_8").text
#         # 상품 설명
#         # pinfo = item.select_one("p._1enCFJskWo").text

#         # 상품 설명 (내용이 없는 경우에도 처리)
#         pinfo = item.select_one("p._1enCFJskWo")
#         if pinfo:
#             pinfo = pinfo.text
#         else:
#             pinfo = "No description available"
#         # 상품 이미지
#         pic = item.select_one("img._25CKxIKjAk")["src"]

#         # print(idx,pname,price,pinfo,pic)
#         p = Product(name=pname, price=price, src=pic, description=pinfo)
#         p.save()


# 커피 머그잔,유리잔 크롤링
# def coffee_crawl():
#     r = requests.get(
#         "https://smartstore.naver.com/zipsoon-e/category/fac3dfbd28424047b6ca9c88099e8c4f?cp=1"
#     )

#     soup = BeautifulSoup(r.text, "html.parser")

#     cups_list = soup.select("ul.wOWfwtMC_3._3cLKMqI7mI li")

#     # print(speaks_list)
#     for idx, item in enumerate(cups_list, start=1):
#         # 상품명
#         pname = item.select_one("strong._26YxgX-Nu5").text
#         # 상품 가격
#         price = item.select_one("strong.zOuEHIx8DC span._2DywKu0J_8").text
#         # 상품 설명 (내용이 없는 경우에도 처리)
#         pinfo = item.select_one("p._1enCFJskWo")
#         if pinfo:
#             pinfo = pinfo.text
#         else:
#             pinfo = "No description available"
#         # 상품 이미지
#         pic = item.select_one("img._25CKxIKjAk")["src"]

#         # print(idx,pname,price,pinfo,pic)
#         p = Product(name=pname, price=price, src=pic, description=pinfo)
#         p.save()
