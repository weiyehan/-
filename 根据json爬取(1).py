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





def search(data, name,pinpai):
    
  driver.get('https://m.dewu.com/router/product/search/ProductSearchResult')
  sleep(1)
  #这里可能需要输入验证码
  driver.find_element_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-box > uni-view > uni-view.search-background > uni-view > uni-input > div > form > input').send_keys(data)
  #按enter
  driver.find_element_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-box > uni-view > uni-view.search-background > uni-view > uni-input > div > form > input').send_keys(Keys.ENTER)
  
  sleep(2)
  lis = lis = driver.find_elements_by_css_selector(
      'body > uni-app > uni-page > uni-page-wrapper > uni-page-body > uni-view > uni-view > uni-view.search-detail > uni-view.hotList.search-result-list > uni-view')
  print(data)
  if len(lis)<= 2:
    for li in lis:
        try:
            price = li.find_element_by_css_selector(
                '.unit').text+li.find_element_by_css_selector('.price').text
            title = li.find_element_by_css_selector('.productTitle').text
            soldNum = li.find_element_by_css_selector('.soldNum').text
            imgurl = li.find_element_by_css_selector('img').get_attribute('src')

        

        

        
            jasondata = {
                "ProductId": data,
                "Name": name,
                "Price": price,
                "saleVolume": soldNum,
                "detail": title


            }
        
            path = os.getcwd()+'\\得物\\'+pinpai+'\\'+data
            mkdir(path)
            filename = data+".json"
            with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
                json.dump(jasondata, fp, ensure_ascii=False)

            imgdata = requests.get(url=imgurl).content

        #爬照片
            name = data+".jpg"
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


path1 = os.getcwd()+'\\intermirror\\'
dirs1 = os.listdir(path1)

# 输出所有文件和文件夹
for pingpai in dirs1:
    path2 = path1+pingpai
    dirs2 = os.listdir(path2)
    for huohao in dirs2:
        path3 = path2+'\\'+huohao
        dirs3 = os.listdir(path3)
        path4 = path3+'\\'+huohao+".json"
        try:
            with open(path4, 'r', encoding='utf-8') as f:
                jsondata = json.load(f)
                name = jsondata['Name']
                search(huohao, name,pingpai)
        except Exception as err:
            print(err)


