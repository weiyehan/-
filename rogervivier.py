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



allurls = ['https://www.rogervivier.com/hk-zt/Shoes/All-Shoes/c/267/page/1/',
           'https://www.rogervivier.com/hk-zt/Bags/All-Bags/c/268/page/1/',
           'https://www.rogervivier.com/hk-zt/Accessories/All-Accessories/c/269/page/1/'
           ]
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; JEF-TN00 Build/HUAWEIJEF-TN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 IntraMirror/1.0 IMAndroid/1.0'}
sleep(5)
for url0 in allurls:
    options.add_experimental_option(
        "excludeSwitches", ['enable-automation', 'enable-logging'])
    driver = webdriver.Chrome(
    "C:\\Users\\weiyehan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe", chrome_options=options)

    sort=url0.split('/')[4]
    print(sort)
    driver.get(url0)
    #pagedown(10)
    imgurls=[]
    names=[]
    prices=[]
    productids=[]
    colours=[]
    imgurl_xpaths = driver.find_elements_by_xpath(
        '//div[@class="Product-grid-item-img-container lazyload-container"]/picture[2]/img')
    for imgurl_xpath in imgurl_xpaths:
        imgurl = imgurl_xpath.get_attribute('src')
        imgurls.append(imgurl)
        productid=imgurl.split('/')[5]
        productids.append(productid)
    name_xpaths = driver.find_elements_by_xpath(
        '//div[@class="Product-grid-item-container Wishlist-adder-container w1of4 w1of2@sm"]/a')
    for name_xpath in name_xpaths:
        words = name_xpath.get_attribute('aria-label')
        name=words.split(',')[0]
        names.append(name)
        colour=words.split(',')[1]
        colours.append(colour)
        price=words.split(',')[2]+words.split(',')[3]
        prices.append(price)
    print(imgurls)
    print(len(imgurls))
    print(productids)
    print(len(productids))
    print(names)
    print(len(names))
    print(prices)
    print(len(prices))
    driver.close()
    for i in range(0,len(imgurls)):
        jasondata = {
            "ProductId": productids[i],
            "Name": names[i],
            "ColorCode": "",
            "ColorName": colours[i],
            "Year": "",
            "Season": "",
            "Category": sort,
            "Gender": "女士",
            "Price": prices[i],
            "SaleVolume": "",
            "SaleVolumeDes": "",
            "Material": "",
            "Detail": ""
        }
        path = os.getcwd()+'\\香港ROGER VIVIER\\' + productids[i]+'\\'

        mkdir(path)
        filename = productids[i]+".json"
        with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
            json.dump(jasondata, fp, ensure_ascii=False)

                #爬照片
        imgdata = requests.get(url=imgurls[i],headers=headers).content
        jpgname = productids[i]+".jpg"
        with open(path+'\\'+jpgname, "wb") as f:
            f.write(imgdata)
    
    
    
