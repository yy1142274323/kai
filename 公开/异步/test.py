import os,requests
import asyncio   #并发请求
import time
import aiohttp   #完成网络请求并发任务


if not os.path.exists('./异步抓取'):
   os.makedirs('./异步抓取')



async def get_content(link):
   async with aiohttp.ClientSession() as session:
      response = await session.get(link)     #response = requests.get()
      content  = await response.read()       #content = response.text(content)(json)
      return content


#下载函数
async def down(img):
   content = await get_content(img[1])
   # print(content)
   with open('{}\\{}.jpg'.format('异步抓取', str(img[0])), 'wb') as l:
      l.write(content)
   print('下载成功'+str(img[0]))

   # 执行函数


def run():
    star = time.time()
    base_url = 'https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837'
    response = requests.get(base_url)

    image_list = response.json()['data']['allImageList']
    # 创建携程对象
    loop = asyncio.get_event_loop()
    # 指定携程运行任务
    # tasks = [asyncio.ensure_future(down((i, imgs['url']))) for i, imgs in enumerate(image_list)]
    # loop.run_until_complete(asyncio.wait(tasks))
    tasks = []
    for i, imgs in enumerate(image_list):
        tasks.append(asyncio.ensure_future(down((i, imgs['url']))))
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print('一共运行了{}秒'.format(end - star))


if __name__ == '__main__':
    run()



'''

async def func1():
    print(1)
    await asyncio.sleep(1)
    print(2)


async def func2():
    print(3)
    await asyncio.sleep(2)
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))


'''















