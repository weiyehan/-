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
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; JEF-TN00 Build/HUAWEIJEF-TN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 IntraMirror/1.0 IMAndroid/1.0'}

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


options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(
    "C:\\Users\\weiyehan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe", chrome_options=options)

baseurls = ['https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/']
womanurls = ['https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E8%BF%B7%E4%BD%A0%E5%9E%8B%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/',
             'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/']
manurls = ['https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%9E%8B%E5%B1%A5/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/',
           'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%85%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/']

allurls = [
    'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%9E%8B%E5%B1%A5/']

for url0 in allurls:

    driver.get(url0)

    urls = []
    pagedown(10)
    sleep(5)

    imgurls = []
    productids = []
    names = []
    colournames = []
    prices = []
    nexturls=[]
    
    imgurls_xpaths = driver.find_elements_by_xpath(
        "//ul[@class='o-listing-row s-scrollable']/li/div[@class='m-product-listing']/a/div//div[1]/div[2]/img")
    nexturl_xpaths = driver.find_elements_by_xpath(
        "//ul[@class='o-listing-row s-scrollable']/li/div[@class='m-product-listing']/a")
    productids_xpaths = driver.find_elements_by_xpath(
        "//ul[@class='o-listing-row s-scrollable']/li/div[@class='m-product-listing']")
    for productid_xpath in productids_xpaths:
        productid = productid_xpath.get_attribute("data-id")
        productids.append(productid)
    for nexturl_xpath in nexturl_xpaths:
        nexturl = nexturl_xpath.get_attribute("href")
        nexturls.append(nexturl)
    for names_xpath in imgurls_xpaths:
        name = names_xpath.get_attribute("alt").split(" - ")[0]
        colourname = names_xpath.get_attribute("alt").split(" - ")[1]

        names.append(name)
        colournames.append(colourname)
    price_xpaths = driver.find_elements_by_xpath(
        "//p[@class='m-product-listing__meta-price f-body']/strong")
    for price_xpath in price_xpaths:
        price = price_xpath.text
        prices.append(price)
    
    print(productids)
    print(len(productids))
    print(names)
    print(len(names))
    print(colournames)
    print(len(colournames))
    print(nexturls)
    #换行
    print("\n")

    print(len(nexturls))
    print(prices)
    print(len(prices))
    try:


        for i in range(len(price_xpaths)):
            detail=""
            try:

                driver.get(nexturls[i])
                price = driver.find_element_by_xpath(
                    "//span[@class='o-product__title-price prices']/strong").text
                imgurl1 = driver.find_element_by_xpath("//div[@class='o-product__imgs']/ul/li[1]//img").get_attribute("src")
                imgurl2 = driver.find_element_by_xpath(
                    "//div[@class='o-product__imgs']/ul/li[2]//img").get_attribute("src")
                size = driver.find_elements_by_xpath(
                    "//div[@class='m-form-dd']/ul[@id='dd_productSize']/li[@class='m-form-dd__item']")
                sizes=""
                for s in size:
                    sizes = sizes+" "+s.get_attribute("data-mformdd-attr-value")
                
                try:
                    description = driver.find_element_by_xpath(
                        "//div[@class='a-text f-body']/p").text
                    
                except Exception as e:
                    print(e)
                if description == "":
                    try:
                        driver.find_element_by_xpath(
                            '//*[@id = "form-product"]/div[2]/button').click()
                        sleep(1)
                        description = driver.find_element_by_xpath(
                            "/html/body/section[3]/div[2]/div/div/div[1]/div/p").text
                    except Exception as e:
                        print(e)
                detail = description
                print("size:"+sizes)
                print(description)
                print(price)
                print(imgurl1.split("?")[0])
                print(imgurl2.split("?")[0])
                miaoshu=""
                canshu=""
                if re.search(r'鞋跟', detail):
                    miaoshu = "鞋跟"
                    canshu = re.findall(r'\n(.*?)鞋跟', detail)[0]
                jasondata = {
                    "ProductId": productids[i],
                    "Name": names[i],
                    "ColorCode": productids[i].split(".")[1],
                    "ColorName": colournames[i],
                    "Year": "",
                    "Season": "",
                    "Category": "shoes",
                    "Gender": "男士",
                    "Price": price,
                    "SaleVolume": miaoshu,
                    "SaleVolumeDes": canshu,
                    "Material": description.splitlines()[0],
                    "Detail": detail,
                    "sizeCodeList": sizes

                }
                path = os.getcwd()+'\\香港Celine\\' + productids[i]+'\\'

                mkdir(path)
                filename = productids[i]+".json"
                with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
                    json.dump(jasondata, fp, ensure_ascii=False)

                        #爬照片
                imgdata = requests.get(url=imgurl1.split("?")[0], headers=headers).content
                jpgname = productids[i]+"NO.1"+".jpg"
                with open(path+'\\'+jpgname, "wb") as f:
                    f.write(imgdata)
                imgdata = requests.get(url=imgurl2.split("?")[0], headers=headers).content
                jpgname = productids[i]+"NO.2"+".jpg"
                with open(path+'\\'+jpgname, "wb") as f:
                    f.write(imgdata)
            except Exception as e:
                print(e)
                print("error")
                continue
    except Exception as e:
        print(e)
        print("error")
        continue

        

    
