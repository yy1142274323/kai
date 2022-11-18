import os,requests,re
import asyncio   #并发请求
import time
import aiohttp   #完成网络请求并发任务


if not os.path.exists(''):
   os.makedirs('./异步雪')



async def get_content(link):
   async with aiohttp.ClientSession() as session:
      response = await session.get(link)     #response = requests.get()
      content  = await response.read()       #content = response.text(content)(json)
      return content




#下载函数
async def down(img):
   # print(type(img[1]))
   # print(img[1])
   # j = 'https://img.zcool.cn/community/01a59f5a64b4e5a80120a123a9cb39.jpg'
   content = await get_content(img[1])
   # print(content)
   with open('{}\\{}.jpg'.format('异步雪', str(img[0])), 'wb') as l:
      l.write(content)
   # with open('{}\\{}.jpg'.format('异步雪中悍刀行', img[0]), 'wb') as l:
   #    l.write(content)


   print('下载成功'+str(img[0]))



#执行函数
def run():
   url = input(':')
   res = requests.get(url).text
   pattern = '<input type="hidden" id="dataInput" data-objid="(.*?)" data-objtype='
   id = re.findall(pattern, res)[0]
   # print(id)
   star = time.time()
   base_url ='https://www.zcool.com.cn/work/content/show?p=2&objectId={}'.format(id)
   response = requests.get(base_url)
   # print(response)
   image_list = response.json()['data']['allImageList']
   # print(image_list)
   # 创建携程对象

   loop = asyncio.get_event_loop()
   #指定携程运行任务

   # def taske():
   #    for i , img in enumerate(image_list):
   #       asyncio.ensure_future(down((i,img['url'])))
   # loop.run_until_complete(asyncio.wait(taske()))



   # tasks = [asyncio.ensure_future(down((i,imgs['url']))) for i,imgs in enumerate(image_list)]
   # loop.run_until_complete(asyncio.wait(tasks))
   tasks = []
   for i, imgs in enumerate(image_list):
      tasks.append(asyncio.ensure_future(down((i, imgs['url']))))
   loop.run_until_complete(asyncio.wait(tasks))


   end = time.time()
   print('以公允性了{}淼'.format(end-star))



if __name__ == '__main__':
   run()



# ```````````````````````````````````````````````````````````````````````````````````````````````````````````````````````


#
# if not os.path.exists('./异步爬取/'):
#    os.makedirs('./异步爬取/')
#
#
# async def get_content(link):
#    async with aiohttp.ClientSession() as session:
#       response = await session.get(link)
#       content = await response.read()
#       return content
#
#
# async def downloader(img):
#    content = await get_content(img[1])
#    # with open('./异步爬取' + str(img[0]) + '.jpg' + 'wb') as f:
#    #    f.write(content)
#    with open('{}\\{}.jpg'.format('异步爬取', str(img[0])), 'wb') as l:
#       l.write(content)
#    print('下载成功' + str(img[0]))
#

#

# def run():
#    start = time.time()
#    base_url = 'https://www.zcool.com.cn/work/content/show?p=2&objectId=6455837'
#    response = requests.get(base_url)
#    image_list = response.json()['data']['allImageList']
#    #创建携程对象
#    loop = asyncio.get_event_loop()
#    # 制修订携程运行的任务
#    tasks = [asyncio.ensure_future(downloader((i,image['url']))) for i, image in enumerate(image_list)]
#    loop.run_until_complete(asyncio.wait(tasks))
#    end = time.time()
#    print('共运行了{}秒'.format(end - start))
#
#
#
# if __name__ == '__main__':
#     run()



