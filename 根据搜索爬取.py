from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
import re


def pagedown(page):

  for i in range(0, page):
    sleep(0.5)
    js = "window.scrollTo(100,{});".format(i*1000)
    driver.execute_script(js)


def mkdir(path):

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:

        os.makedirs(path)

        print(path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return False


count = 0


def search(data):
  driver.get('https://m.dewu.com/router/product/search/ProductSearchResult')
  sleep(1)
  #这里可能需要输入验证码
  driver.find_element_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-box > uni-view > uni-view.search-background > uni-view > uni-input > div > form > input').send_keys(data)
  #按enter
  driver.find_element_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-box > uni-view > uni-view.search-background > uni-view > uni-input > div > form > input').send_keys(Keys.ENTER)
  pagedown(5)

  lis = driver.find_elements_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-detail > uni-view.hotList.search-result-list > uni-view')
  for li in lis:
    price = li.find_element_by_css_selector(
        '.unit').text+li.find_element_by_css_selector('.price').text
    title = li.find_element_by_css_selector('.productTitle').text
    soldNum = li.find_element_by_css_selector('.soldNum').text
    imgurl = li.find_element_by_css_selector('img').get_attribute('src')

    count = count+1

    num = re.sub(r'\【(.*?)\】', "", title)

    pinpai = num.split(" ")
    jasondata = {
        "ProductId": "",
        "Name": num,
        "Price": price,
        "saleVolume": soldNum,
        "detail": ""


    }
    try:
        path = os.getcwd()+'\\得物\\'+pinpai[0]+'\\'+title
        mkdir(path)
        filename = title+".json"
        with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
            json.dump(jasondata, fp, ensure_ascii=False)

        imgdata = requests.get(url=imgurl).content

    #爬照片
        name = title+".jpg"
        with open(path+'\\'+name, "wb") as f:
            f.write(imgdata)
    except Exception as err:
        print(err)


options = webdriver.ChromeOptions()

# 忽略无用的日志
options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(
    "C:\\Users\\weiyehan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe", chrome_options=options)
search('女士包')
sleep(100)
