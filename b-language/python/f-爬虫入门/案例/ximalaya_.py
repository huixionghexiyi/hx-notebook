import requests
import re
import parsel
session = requests.session()  # 使用session方法
headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45',
}
'''下载音频'''


def download_media(media_url, media_name):
    r = requests.get(media_url, headers=headers)
    if r.status_code == 200:
        with open(f'D:\\\day_word\\{media_name}.m4a', 'wb') as f:
            f.write(r.content)
    else:
        print(r.status_code)


# download_media(
#     'https://fdfs.xmcdn.com/group77/M09/E8/89/wKgO316IL4zx1jA8AAykB8kPS_o078.m4a', 'test')
# '''获取链接API'''


def media_api(trick_id):
    api_url = f'https://www.ximalaya.com/revision/play/v1/audio?id={trick_id}&ptype=1'
    response = requests.get(api_url, headers=headers)
    return response.json().get('data').get('src')


def get_totle_page(url):
    r = requests.get(url, headers=headers)
    sel = parsel.Selector(r.text)
    sound_list = sel.css('.sound-list ul li div a')
    for sound in sound_list:
        media_url = sound.css('a::attr(href)').extract_first().split('/')[-1]
        media_name = sound.css('a::attr(title)').extract_first()
        yield media_url, media_name
    # return r.content


if __name__ == '__main__':
    for page in range(1,13):
        url = f'https://www.ximalaya.com/waiyu/5257748/p{page}'
        try:
            for url, name in get_totle_page(url):
                # print(url,name)
                url = media_api(url)
                # print(url)
                download_media(url, name)
        except Exception as e:
            print( e.args)


