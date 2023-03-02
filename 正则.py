import re
data = "100%小牛皮\n疊層皮革直鞋踭\n0.6英寸（15毫米）鞋跟\n圓形\n傳統便鞋結構，綴以手縫裙飾\n金色CELINE TRIOMPHE標誌\n小山羊皮鞋墊\n手繪皮革外底\n布萊克鞋身結構\n鞋面較窄，選擇平常尺碼大半碼更為舒適\n參考編號：334773001C.38NO\n尺码 39 39,5 40 40,5 41 41,5 42 42,5 43 43,5 44 44,5 45 45,5 46"
if re.search(r'鞋跟', data):
    miaoshu = "鞋跟"
    canshu=re.findall(r'\n(.*?)鞋跟', data)
    

