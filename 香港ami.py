from pydoc import doc
from this import s
from turtle import delay
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
import re
import paramiko
import stat
import hashlib
options = webdriver.ChromeOptions()

host = '47.98.181.105'  # sftp主机
port = 22  # 端口
username = 'datateam'  # sftp用户名
password = 'Top2@123'  # 密码


def create_dir(sftp, remoteDir):
    try:
        if stat.S_ISDIR(sftp.stat(remoteDir).st_mode):  # 如果remoteDir存在且为目录，则返回True
            print(remoteDir + ' 目录  已存在')
    except Exception as e:
        sftp.mkdir(remoteDir)
        print("在远程sftp上创建目录：{}".format(remoteDir))

# 上传sftp,上传成功打印路径


def upload_sftp(hostname, username, password, local_dir, remote_dir):
    try:
        t = paramiko.Transport((hostname, 22))
        t.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        create_dir(sftp, remote_dir)
        #判断本地路径是文件夹还是文件
        if os.path.isdir(local_dir):
            print("本地路径是文件夹")
            for root, dirs, files in os.walk(local_dir):
                for file in files:
                    local_file = os.path.join(root, file)
                    remote_file = os.path.join(remote_dir, file)
                    sftp.put(local_file, remote_file)
                    #判断是否上传成功，成功打印路径
                    if sftp.stat(remote_file).st_size == os.path.getsize(local_file):
                        print("上传成功：{}".format(remote_file))
                    else:
                        print("上传失败：{}".format(remote_file))
        else:
            print("本地路径是文件")
            sftp.put(local_dir, remote_dir)

    except Exception as e:
        print(e)


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

        print(path+' 本地创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 本地目录已存在')
        return False


def pagedown(page):

  for i in range(0, page):
    sleep(0.5)
    js = "window.scrollTo(100,{});".format(i*1000)
    driver.execute_script(js)


manurls = ['https://www.amiparis.com/hk/shopping/man/clothing',
           'https://www.amiparis.com/hk/shoppingoman/bags',
           'https://www.amiparis.com/hk/sets/man/swimwear-man',
           'https://www.amiparis.com/hk/shopping/man/Jewelry',
           'https://www.amiparis.com/hk/shopping/man/accessories',
           'https://www.amiparis.com/hk/sets/man/denim-man',
           'https://www.amiparis.com/hk/sets/man/trousers-man',
           'https://www.amiparis.com/hk/sets/man/shoes-man',
           'https://www.amiparis.com/hk/sets/man/underwear-man',
           'https://www.amiparis.com/hk/sets/man/jackets-coats-man',
           'https://www.amiparis.com/hk/sets/man/sweaters-cardigans-man',
           'https://www.amiparis.com/hk/sets/man/suits-man'
           
           ]

womanurls = [
            'https://www.amiparis.com/hk/shopping/woman/clothing',
             'https://www.amiparis.com/hk/sets/woman/swimwear-woman',
             'https://www.amiparis.com/hk/shopping/woman/bags',
             'https://www.amiparis.com/hk/shopping/woman/Jewelry',
             'https://www.amiparis.com/hk/shopping/woman/accessories',
             'https://www.amiparis.com/hk/sets/woman/knitwear-woman',
             'https://www.amiparis.com/hk/sets/woman/denim-woman',
             'https://www.amiparis.com/hk/sets/woman/shorts-skirts-woman',
             'https://www.amiparis.com/hk/sets/woman/blazers-suits-woman'
             
             ]
for baseurl in manurls:
    sort1 = baseurl.split('/')[len(baseurl.split('/'))-1]
    sort=sort1.split('-')[0]
    options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(
        "C:\\Users\\weiyehan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe", chrome_options=options)

    driver.get(baseurl)
    pagedown(5)
    sleep(7)
    
    imgurls=[]
    names=[]
    prices=[]
    imgurl_xpaths = driver.find_elements_by_xpath(
        '//div[@class="css-79elbk e1y3efn70"]/a[1]/div[1]/img[1]')
    for imgurl_xpath in imgurl_xpaths:
        imgurl = imgurl_xpath.get_attribute('src')
        imgurls.append(imgurl)
    name_xpaths = driver.find_elements_by_xpath(
        '//div[@class="css-79elbk e1y3efn70"]/a[1]/div[2]/div[1]/span[1]')
    price_xpaths = driver.find_elements_by_xpath('//div[@class="e1y3efn78 css-1ge6h5a e1izcwgw0"]/span[1]')
    for namexpath  in name_xpaths:
        name = namexpath.text
        names.append(name)
    for price_xpath in price_xpaths:
        price=price_xpath.text
        prices.append(price)
    driver.close()
    print(names)
    print(len(names))
    for i in range(0,len(imgurls)-1):
        if(names[i]!='' and i!=len(imgurls)-1 and names[i]!=names[i+1]):
            jasondata = {
                "ProductId": "",
                "Name": names[i],
                "ColorCode": "",
                "ColorName": "",
                "Year": "",
                "Season": "",
                "Category": sort,
                "Gender": "man",
                "Price": prices[i],
                "SaleVolume": "",
                "SaleVolumeDes": "",
                "Material": "",
                "Detail": ""
            }
            path = os.getcwd()+'\\香港Ami\\' + names[i]+'\\'

            mkdir(path)
            filename = names[i]+".json"
            with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
                json.dump(jasondata, fp, ensure_ascii=False)

                #爬照片
            imgdata = requests.get(url=imgurls[i]).content
            jpgname = names[i]+".jpg"
            with open(path+'\\'+jpgname, "wb") as f:
                f.write(imgdata)
    
    
   
