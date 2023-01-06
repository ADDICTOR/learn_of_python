import requests
import os

# 用于识别xpath表达式的模块
from lxml import etree

# 伪装
headers = {
    'Referer':'referer: https://yys.163.com/media/picture.html',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie':'topbarnewsshow=1; usertrack=ezq0ZWOZZ0mBAxENAwuoAg==; __bid_n=1851d6638e8a2491104207; FEID=v10-83093757f4c3ad7c0f6144c32d2373eea3d8cb0a; __xaf_fpstarttimer__=1671608946524; __xaf_thstime__=1671608947095; FPTOKEN=f80BJd5NmlouqgCKmy50QE+e3Tct2xg1UuSUKhxwcWbpTFeA75+XRJOvLhZV+skA87OIJbWy6n5BNvg0vtmcjhQCmvDGggC/bxopplSwJ+ZtRrIh9CxUcRsJTAUClOd8OYK7AZfTh8hAtPXMSSm5f296lVFdykr3p20DbGV/P5RmnRbAGlqGuWLiUl49dtT0EXi/Skj8qH5RH8+uy2iyulfAnY7NJS1NvWgNnC1RwFbedP04qUCC9rP+SWP4Qjv2sAjkfD1HpeuaZCGp+tJdrLGHNY+YUQ78XwTlfcXaHWA5F2FSEmCzOeHbU75Uf2fMC9WDht7eqa9IUuyoCWbS569VvuKJ2/M2/eZNuqF4qrWVDlxxZdtJHZCT8IbmYhAxF4UufcXVKKpQJIdf2/wZug==|+1AfoObH7tf+8+wHkxG9oM7YRHJP5Wr9vtqlDV+kGCE=|10|54b90bc1206327dcd39d5ef076d28273; __xaf_fptokentimer__=1671608947267; vinfo_n_f_l_n3=d72f7cf1e0b43ce9.1.0.1671608943829.0.1671608955957; timing_user_id=time_L3RyKFDqCW; _nietop_foot=%u9634%u9633%u5E08%7Cyys.163.com; topbarnewsshow=1'
}

# 请求图片列表数据
list_url = 'https://yys.163.com/media/picture.html'
list_resp = requests.get(list_url,headers=headers)

# print(list_resp.text)ß
e = etree.HTML(list_resp.text)
print(e)

imgs1 = [url[:url.rindex('/')] + '/1920×1080.jpg' for url in e.xpath('//div[@class="tab-cont"][1]/div/div/img/@data-src')]
imgs2 = [url[:url.rindex('/')] + '/1920×1080.jpg' for url in e.xpath('//div[@class="tab-cont"][2]/div/div/img/@data-src')]

if not os.path.exists('heng'):
    os.makedirs('heng')
if not os.path.exists('shu'):
    os.makedirs('shu')

for url in imgs1:
    print(url)
    # https://yys.res.netease.com/pc/zt/20170731172708/data/picture/20221223/1/1920x1080.jpg
    resp = requests.get(url,headers=headers)
    file_name = url[url.rindex('picture'):url.rindex('/')].replace('/','_') + '.jpg'
    print('正在保存' + file_name + '壁纸')
    with open(f'heng/{file_name}', 'wb') as f:
        f.write(resp.content)
    break
