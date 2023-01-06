# pip3 install requests
import requests

# 统一资源定位符，所需数据所在位置
url = 'https://webfs.ali.kugou.com/202212302044/3db3e430ffbdff149137b01b657bdae4/KGTX/CLTX001/4caf024f643333b0b08322b457550bf8.mp3'

# 伪装为浏览器，防止被反爬虫
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

# 发送请求到服务器，请求资源
resp = requests.get(url,headers=headers)

# 将从服务器获取的数据保存为对应格式
with open('music.mp3','wb') as f:
    f.write(resp.content)