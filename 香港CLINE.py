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


options.add_experimental_option(
    "excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(
    "C:\\Users\\weiyehan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.7\\chromedriver.exe", chrome_options=options)

baseurls = ['https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/']
womanurls = [ 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E8%BF%B7%E4%BD%A0%E5%9E%8B%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/',
             'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/']
manurls = [ 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%9E%8B%E5%B1%A5/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/',
           'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%85%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/']

allurls=['https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/triomphe/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/triomphe%E5%B8%86%E5%B8%83/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/cuir-triomphe/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/16/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/ava/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/cabas%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/belt%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/classic%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/sangle/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%89%8B%E8%A2%8B/%E6%9B%B4%E5%A4%9A%E6%AC%BE%E5%BC%8F/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/triomphe%E5%B8%86%E5%B8%83/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/essentials/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%B0%8F%E5%9E%8B%E7%9A%AE%E5%85%B7/%E6%89%8B%E8%A2%8B%E9%85%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/triomphe/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E9%AB%AE%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/alphabet%E6%89%8B%E8%A2%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E6%9B%B4%E5%A4%9A%E6%AC%BE%E5%BC%8F/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/maillon-triomphe/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/celine-sentimental/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/torsion/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/medaille-celine/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/etoile-celine/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E7%8F%A0%E5%AF%B6/systeme/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E5%A4%BE%E5%85%8B%E5%8F%8A%E5%A4%A7%E8%A4%B8/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E9%80%A3%E8%A1%A3%E8%A3%99%E5%8F%8A%E5%8D%8A%E8%BA%AB%E8%A3%99/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E9%87%9D%E7%B9%94%E8%A1%AB%E5%8F%8A%E8%A1%9B%E8%A1%A3/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E7%89%9B%E4%BB%94%E8%A3%9D/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E6%81%A4%E8%A1%AB%E5%8F%8A%E4%B8%8A%E8%A1%A3/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E9%95%B7%E8%A4%B2%E5%8F%8A%E7%9F%AD%E8%A4%B2/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E9%81%8B%E5%8B%95%E9%9E%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E5%B9%B3%E5%BA%95%E9%9E%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E6%B6%BC%E9%9E%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E9%9D%B4%E5%AD%90/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E9%AB%98%E8%B7%9F%E9%9E%8B/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/new/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/triomphe/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/monochroms/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/oversized/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/cat-eye/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/round/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/square/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/rectangular/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/aviator/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E5%A4%AA%E9%99%BD%E7%9C%BC%E9%8F%A1/%E5%9C%96%E6%A1%88/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E7%9A%AE%E5%B8%B6/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E5%B8%BD%E5%AD%90%E5%8F%8A%E7%B4%A1%E7%B9%94%E5%93%81%E9%85%8D%E9%A3%BE/', 'https://www.celine.com/zht-hk/celine-%E5%A5%B3%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E6%B2%99%E7%81%98%E9%85%8D%E9%A3%BE/']
allurls2=['https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/leather/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/college/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/casual/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%8E%A1%E9%9B%86/tailoring/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E5%A4%A7%E8%A4%B8%E5%8F%8A%E7%9F%AD%E8%BA%AB%E5%A4%96%E5%A5%97/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E5%A4%96%E5%A5%97%E5%8F%8A%E8%A4%B2%E5%AD%90/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E6%81%A4%E8%A1%AB/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E9%87%9D%E7%B9%94%E8%A1%AB/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E7%9A%AE%E8%A1%A3%E5%8F%8A%E7%9A%AE%E8%8D%89/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/t%E6%81%A4%E5%8F%8A%E9%81%8B%E5%8B%95%E8%A1%AB/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%9C%8D%E9%A3%BE/%E7%89%9B%E4%BB%94%E8%A3%9D/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%9E%8B%E5%B1%A5/%E9%81%8B%E5%8B%95%E9%9E%8B/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E5%B8%BD%E5%AD%90%E5%8F%8A%E9%B4%A8%E8%88%8C%E5%B8%BD/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E9%85%8D%E9%A3%BE/%E7%B4%A1%E7%B9%94%E7%89%A9%E9%A3%BE%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E6%96%B0%E5%93%81/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E8%80%B3%E7%92%B0/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E9%A0%B8%E9%8D%8A/', 'https://www.celine.com/zht-hk/celine-%E7%94%B7%E8%A3%9D/%E6%99%82%E5%B0%9A%E9%A6%96%E9%A3%BE/%E6%89%8B%E9%90%B2/']
for url0 in allurls2:

    driver.get(url0)
    
    urls=[]
    pagedown(10)
    sleep(5)
    
    imgurls=[]
    productids=[]
    names=[]
    colournames=[]
    prices=[]
    sort=driver.find_element_by_xpath("//div[@class='m-breadcrumb__items']/div[3]/a").text
    imgurls_xpaths = driver.find_elements_by_xpath("//ul[@class='o-listing-grid']/li/div[@class='m-product-listing']/a/div//div[1]/div[2]/img")
    for imgurls_xpath in  imgurls_xpaths:
        imgurl=imgurls_xpath.get_attribute("src")
        imgurls.append(imgurl)  
    productids_xpaths=driver.find_elements_by_xpath("//ul[@class='o-listing-grid']/li/div[@class='m-product-listing']")
    for productid_xpath in productids_xpaths:
        productid=productid_xpath.get_attribute("data-id")
        productids.append(productid)
        
    for names_xpath in imgurls_xpaths:
        name=names_xpath.get_attribute("alt").split("-")[0]
        colourname = names_xpath.get_attribute("alt").split("-")[1]
        
        names.append(name)
        colournames.append(colourname)
    price_xpaths=driver.find_elements_by_xpath("//p[@class='m-product-listing__meta-price f-body']")
    for price_xpath in  price_xpaths:
        price=price_xpath.text
        prices.append(price)
    for i in range(len(price_xpaths)):
        jasondata = {
            "ProductId": productids[i],
            "Name": names[i],
            "ColorCode": productids[i].split(".")[1],
            "ColorName": colournames[i],
            "Year": "",
            "Season": "",
            "Category": sort,
            "Gender": "男士",
            "Price": prices[i],
            "SaleVolume": "",
            "SaleVolumeDes": "",
            "Material": "",
            "Detail": ""
        }
        if(imgurls[i]!= None):
            
            path = os.getcwd()+'\\香港Celine\\' + productids[i]+'\\'
                
            mkdir(path)
            filename = productids[i]+".json"
            with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
                json.dump(jasondata, fp, ensure_ascii=False)

                #爬照片
            imgdata = requests.get(url=imgurls[i]).content
            jpgname = productids[i]+".jpg"
            with open(path+'\\'+jpgname, "wb") as f:
                f.write(imgdata)

    
    print(sort)
    print(imgurls)
    print(len(imgurls))
    print(productids)
    print(len(productids))
    print(names)
    print(len(names))
    print(colournames)
    print(len(colournames))
    print(prices)
    print(len(prices))
