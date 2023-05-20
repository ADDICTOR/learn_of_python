# python内置的requests模块，该模块主要用于发送HTTP请求，相比urllib更为简洁
import requests
import json

# 伪装为浏览器
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'Cookie':'kg_mid=299ea5533f5160fb2e16fbd30385be1b; kg_dfid=2mSkjw0E3dkQ460cB50YwQtz; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; Hm_lvt_aedee6983d4cfc62f509129360d6bb3d=1672361644; kg_mid_temp=299ea5533f5160fb2e16fbd30385be1b; Hm_lpvt_aedee6983d4cfc62f509129360d6bb3d=1672411679'
}


# 音乐列表
list_url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672411679489&mid=299ea5533f5160fb2e16fbd30385be1b&uuid=299ea5533f5160fb2e16fbd30385be1b&dfid=2mSkjw0E3dkQ460cB50YwQtz&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=885f33072bc842b1538c1d44312c4c1d'
list_resp = requests.get(list_url,headers=headers)
song_list = json.loads(list_resp.text[12:-2])['data']['lists']
# print(list_resp.text)
for i,s in enumerate(song_list):
    print(f'{i+1}---{s.get("FileName")}---{s.get("EMixSongID")}')

num = input("请输入希望下载哪一首音乐：")
# song_name = f'{song_list[int(num)-1].get("FileNmae")}.mp3'

# 获取音乐url地址的url地址
info_url = f'https://wwwapi.kugou.com/yy/index.php?r=play/getdata&encode_album_audio_id={song_list[int(num)-1].get("EMixSongID")}'
info_resp = requests.get(info_url,headers=headers)


# 音乐的url地址
music_url = info_resp.json()['data']['play_url']
music_resp = requests.get(music_url,headers=headers)

# 将从服务器获取的数据保存为对应格式文件
with open('music.mp3', 'wb') as f:
    f.write(music_resp.content)

'''
服务器响应的数据结果
.text    代表访问的数据是文字
.content 代表访问的数据是多媒体文件(图片、音乐、视频、文件)
.json()  代表访问的数据是json类型
'''