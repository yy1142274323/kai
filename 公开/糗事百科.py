import re, requests, time, json, os,asyncio,aiohttp
from copyheaders import headers_raw_to_dict
from fake_useragent import UserAgent
from lxml import etree
import random


if not os.path.exists('./糗事百科'):
   os.makedirs('./糗事百科')

async def get_content(link):

    async with aiohttp.ClientSession() as session:
        # time.sleep(random.uniform(1,5))
        response = await session.get(link)     #respo
        content  = await response.read()       #content = response.text(content)(json)
        return content


async def down(img):
    content = await get_content(img[1])
    print(img[1])
    with open('{}\\{}.jpg'.format('糗事百科',img[0]),'wb') as f:
        f.write(content)
        print('下载成功'+str(img[0]))


def run():
    for m in range(1,10):
        start = time.time()
        url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(m)
        headers = {'User-Agent': UserAgent().random}
        res = requests.get(url = url ,headers = headers).text
        # print(res)
        html = etree.HTML(res)
        lj = html.xpath('//*[@id="content"]/div/div[2]/div/div[2]/a/img/@src')

        # 创建携程对象
        loop = asyncio.get_event_loop()
        # 指定携程运行任务
        tasks = [asyncio.ensure_future(down((str(m) + '_' + str(i), 'http:'+ imgs))) for i, imgs in enumerate(lj)]

        loop.run_until_complete(asyncio.wait(tasks))

        end = time.time()
        print('用时{}秒'.format(end - start))


if __name__ == '__main__':
    run()











# LJ = 'https://www.qiushibaike.com' + lj_b

