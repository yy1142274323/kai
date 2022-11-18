import requests,json
#
#
#
#
# url = 'https://vd3.bdstatic.com/mda-km7kmcf7565asjj0/sc/cae_h264_clips/1607421602/mda-km7kmcf7565asjj0.mp4'
#
# f = requests.get(url).content
#
# with open('视频\\{}.mp4'.format('1'), 'wb') as l:
#     l.write(f)
#
#

'https://jx.muzzz.cn/api/dsp/32C3D946380DCD222C5B55243B2F00FC88A3123D2C17F25816/1/?url=https://h5.ippzone.com/pp/post/404046885542?zy_to=copy_link%26share_count=1%26m=65a735b628fdcf6780a0ad9c440f2aef%26app=%26type=post%26did=f166323b1530394e%26mid=83612128%26pid=404046885542'

url_jx = 'https://jx.muzzz.cn/api/dsp/32C3D946380DCD222C5B55243B2F00FC88A3123D2C17F25816/1/'

data = {
    'url':'http://share.ippzone.com/pp/post/387219376882'
}

response = requests.post(url=url_jx,data = data).text
r = json.loads(response)
print(r)

