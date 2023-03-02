import json
import re
import os
import hashlib
import xlutils.copy
import xlwt
import xlrd
import requests
import pandas as pd


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

        print (path+' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path+' 目录已存在')
        return False



def jsonprovide(spuid,price1):
    
    headers = {
        'Host': 'imgateway.intramirror.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'urlNum': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; JEF-TN00 Build/HUAWEIJEF-TN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 IntraMirror/1.0 IMAndroid/1.0',
        'token': 'E2/Yfg1DOnb3+yaWJNPb70GLe4011LcTOlttIUMkbhk=',
        'X-Requested-With': 'com.intramirror.android',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    a = 'spuId={}&version=2.0'.format(spuid)
    a += 'a84926b827baf5d458a046a6129eb383'

    b = hashlib.md5(a.encode()).hexdigest()

    params = (
        ('spuId', spuid),
        ('version', '2.0'),
        ('signature', b),
    )
    response = requests.get(
        'http://imgateway.intramirror.com/imapp/spu', headers=headers, params=params)
    colorCode = price = re.findall(r"colorCode\"\:\"(.*?)\"", str(response.text))
    spuName1 = re.findall(r"name\"\:\"(.*?)\"", str(response.text))
    colorCode1 = re.findall(r"colorCode\"\:\"(.*?)\"", str(response.text))
    huohao1 = re.findall(r"designerId\"\:\"(.*?)\"", str(response.text))
    pinpai1 = re.findall(r"brand\"\:\"(.*?)\"", str(response.text))
    descrip1 = re.findall(r"description\"\:\"(.*?)\"", str(response.text))
   
    coverimage1 = re.findall(r"thumbnails\"\:\[\"(.*?)\"", str(response.text))
    jasondata = {
        "code": huohao1[0]+colorCode1[0],
        "price": price1,
        "saleVolume": "",
        "attribute1": spuName1[0],
        "attribute2": pinpai1[0],
        "attribute3": coverimage1[0],
        "detail": descrip1[0]


    }
    
    print(spuName1)
    path = os.getcwd()+'\\intermirror\\'+pinpai1[0]+'\\'+huohao1[0]+colorCode1[0]
    mkdir(path)
    filename =huohao1[0]+colorCode1[0]+'.json'
    
    
    with open(path+'\\'+filename, 'w', encoding='utf-8') as fp:
        json.dump(jasondata, fp, ensure_ascii=False)
    name = spuName1[0]+".jpg"
    imgdata = requests.get(url=coverimage1[0]).content
    with open(path+'\\'+name, "wb") as f:
        f.write(imgdata)

   

    

def getcolourcode(spuid):
    headers = {
        'Host': 'imgateway.intramirror.com',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/plain, */*',
        'urlNum': '0',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; JEF-TN00 Build/HUAWEIJEF-TN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 IntraMirror/1.0 IMAndroid/1.0',
        'token': 'E2/Yfg1DOnb3+yaWJNPb70GLe4011LcTOlttIUMkbhk=',
        'X-Requested-With': 'com.intramirror.android',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    }

    a = 'spuId={}&version=2.0'.format(spuid)
    a += 'a84926b827baf5d458a046a6129eb383'

    b = hashlib.md5(a.encode()).hexdigest()

    params = (
        ('spuId', spuid),
        ('version', '2.0'),
        ('signature', b),
    )
    response = requests.get(
        'http://imgateway.intramirror.com/imapp/spu', headers=headers, params=params)
    colorCode = price = re.findall(
        r"colorCode\"\:\"(.*?)\"", str(response.text))

    return colorCode


def fun(df, filename):
    n = 0
    for x in df['款号']:
        count = 0  # 记录匹配的商品数
        imprice = []
        discount = []

        print("款号"+x)
        truecolourcode = []
        truecolourcode.append(re.compile(r'.*\-').sub('', re.compile(r'.*\-').sub('', x)))
        x = re.compile(r'\-*').sub('', re.compile(r'\-\d\d.*').sub('', x))
        print(truecolourcode)
        print(x)
        headers = {
            'Host': 'imgateway.intramirror.com',
            'Connection': 'keep-alive',
            'Content-Length': '148',
            'Accept': 'application/json, text/plain, */*',
            'urlNum': '0',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; JEF-TN00 Build/HUAWEIJEF-TN00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.93 Mobile Safari/537.36 IntraMirror/1.0 IMAndroid/1.0',
            'content-type': 'application/json',
            'X-Requested-With': 'com.intramirror.android',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        data = {
            "skipErrorCorrection": False,
            "queryType": "1001",
            "keyword": x,  # 这个是搜索的内容
            "pageNo": 1,
            "pageSize": 30,
            "desc": True,
            "orderBy": 3
        }

        response = requests.post(
            'http://imgateway.intramirror.com/imapp/search/center/top/searchList', headers=headers, data=json.dumps(data))

        saleSpuId = re.findall(r"saleSpuId\"\:(.*?)\,", str(response.text))
        spuId = re.findall(r"spuId\"\:(.*?)\,", str(response.text))
        spuName = re.findall(r"spuName\"\:\"(.*?)\"", str(response.text))
        imprice = []
        discount = []
        #print(saleSpuId)
        #print(spuId)
        if(len(saleSpuId) >= 50):  # 结果大于50个视为搜索失败
            print("没有该商品信息")
        else:
            #print("共搜索到{}个商品".format(len(saleSpuId)))
            #print(spuName)
            for i in range(0, len(saleSpuId)):
                saleSpuId1 = saleSpuId[i]
                spuId1 = spuId[i]
                spudata = {
                    "saleSpuAndSpu": [
                        {
                            "saleSpuId": saleSpuId1,
                            "spuId": spuId1
                        }
                    ]
                }
                response = requests.post(
                    'http://imgateway.intramirror.com/imapp/spu/getSpuSkuInfo', headers=headers, data=json.dumps(spudata))

                if(str(getcolourcode(spuId1)).lower() == str(truecolourcode).lower()):  # 转化为小写比较

                    count = count+1
                    price = re.findall(
                        r"imPrice\"\:\"(.*?)\"", str(response.text))
                    discoun = re.findall(
                        r"imDiscount\"\:\"(.*?)\"", str(response.text))
                    imprice = imprice+price
                    discount = discount+discoun
                    try:
                        jsonprovide(spuId1, price)
                    except Exception as err:
                        print(err)
                    break
                    

            print("匹配的商品数:"+str(count))

            str1 = ','
            str1.join(str(i) for i in imprice)
            print(str1.join(str(i) for i in zip(imprice, discount)))
            #写入表格
            n = n+1
            data = xlrd.open_workbook(filename)
            ws = xlutils.copy.copy(data)  # 复制之前表里存在的数据
            table = ws.get_sheet(0)

            table.write(n, 2, str1.join(str(i)
                                        for i in zip(imprice, discount)))  # 最后一行追加数据

            ws.save(filename)
            print(n)
            print('\n')


print("爬取CELINE的数据")
filename = "CELINE.xls"
df = pd.read_excel(filename)
fun(df, filename)
