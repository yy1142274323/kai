import os, requests
import asyncio  #并发请求
import time
import aiohttp  #完成网络请求并发任务
from copyheaders import headers_raw_to_dict
from lxml import etree




if not os.path.exists('./斗图'):
   os.makedirs('./斗图')

async def get_content(link):
    async with aiohttp.ClientSession() as session:
        response = await session.get(link)  #response = requests.get()
        content = await response.read()  #content = response.text(content)(json)
        return content


async def down(img):
    content = await get_content(img[1])
    # print(content)
    with open('{}\\{}.jpg'.format('斗图', str(img[0])), 'wb') as l:
        l.write(content)
    print('下载成功' + str(img[0]))



def run():
    i = 1
    while True:
        print(i)
        url = 'https://www.doutula.com/photo/list/?page={}'.format(i)
        print(url)
        head = headers_raw_to_dict(
            b'''
            Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            Accept-Encoding: gzip, deflate, br
            Accept-Language: zh-CN,zh;q=0.9
            Cache-Control: max-age=0
            Connection: keep-alive
            Cookie: _agep=1610438977; _agfp=86dc59f14ae99892fd80f6d65252ed6c; _agtk=c493164cffb5e8fc2cb54565c81747c4; Hm_lvt_2fc12699c699441729d4b335ce117f40=1610438978,1611026697; Hm_lpvt_2fc12699c699441729d4b335ce117f40=1611036080
            Host: www.doutula.com
            Referer: https://www.doutula.com/photo/list/?page=2
            Sec-Fetch-Dest: document
            Sec-Fetch-Mode: navigate
            Sec-Fetch-Site: same-origin
            Sec-Fetch-User: ?1
            Upgrade-Insecure-Requests: 1
            User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36
            
            '''
        )
        res = requests.get(url= url,headers = head).text
        # print(res)
        # 创建携程对象
        loop = asyncio.get_event_loop()
        html = etree.HTML(res)
        # print(html)
        # titlt = html.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a/p/text()')
        # print(titlt)

        imgs = html.xpath('//*[@id="pic-detail"]/div/div[2]/div[2]/ul/li/div/div/a/img/@data-backup')
        # print(img)


        # for m,img in enumerate(imgs):
        tasks = [asyncio.ensure_future(down(('{}'.format(i)+'-{}'.format(m),img))) for m,img in enumerate(imgs)]
        # tasks.append(asyncio.ensure_future(down((m,img))))
        loop.run_until_complete(asyncio.wait(tasks))




        i+=1


if __name__ == '__main__':
    run()




