import requests
import re
import parsel

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36 Edg/81.0.416.45"
}


def download_img(img_url, img_name):
    r = requests.get(img_url, headers=headers)
    if r.status_code == 200:
        with open(f'D:\\Projects\\spider\\{img_name}.jpg', 'wb') as f:
            f.write(r.content)


def get_img(url):
    resp = requests.get(url, headers=headers)
    sel = parsel.Selector(resp.text)
    img_tags = sel.css('.bang_list li .pic a img')
    for img in img_tags:
        img_url = img.css('::attr(src)').extract_first()
        img_name = img.css('::attr(alt)').extract_first()
        yield img_url,img_name


if __name__ == '__main__':
    for i in range(1,6):
        url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{}'.format(i)
        for img_url,img_name in get_img(url):
            download_img(img_url,img_name)
