import os, requests,re,json
import asyncio  #并发请求
import time
import aiohttp  #完成网络请求并发任务
from copyheaders import headers_raw_to_dict
import tkinter,threading




if not os.path.exists('./妹子图'):
   os.makedirs('./妹子图')





async def get_content(link):
    async with aiohttp.ClientSession() as session:
        response = await session.get(link)  #response = requests.get()
        content = await response.read()  #content = response.text(content)(json)
        return content

async def down(img):
    content = await get_content(img[1])

    with open('{}\\{}.jpg'.format('妹子图', str(img[0])), 'wb') as l:
        l.write(content)
    time.sleep(0.01)
    print('下载成功' + str(img[0]))


def run():
    m = 1
    while True:
        print(m)
        star = time.time()
        url = 'https://www.mzitu.com/page/{}/'.format(m)
        head = headers_raw_to_dict(
            b'''
            accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            accept-encoding: gzip, deflate, br
            accept-language: zh-CN,zh;q=0.9
            cookie: Hm_lvt_cb7f29be3c304cd3bb0c65a4faa96c30=1608714338,1610959006; Hm_lpvt_cb7f29be3c304cd3bb0c65a4faa96c30=1610959069
            referer: https://www.mzitu.com/jiepai/
            sec-fetch-dest: document
            sec-fetch-mode: navigate
            sec-fetch-site: same-origin
            sec-fetch-user: ?1
            upgrade-insecure-requests: 1
            user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
            
            
            '''
        )



        res = requests.get(url = url,headers = head).text
        pattern = 'data-original="(.*?)" /></p>'
        r = re.findall(pattern,res)
        loop = asyncio.get_event_loop()
        tasks = [asyncio.ensure_future(down(('{}'.format(m)+'-{}'.format(i),img))) for i,img in enumerate(r)]

        loop.run_until_complete(asyncio.wait(tasks))

        m += 1
        edn = time.time()
        print('用时：',edn-star)



if __name__ == '__main__':
    run()






























