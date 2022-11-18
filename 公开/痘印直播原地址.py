import requests
import re


class DouYin:

    def __init__(self, rid):
        self.rid = rid

    def get_real_url(self):
        try:
            if 'v.douyin.com' in self.rid:
                room_id = re.findall(r'(\d{19})', requests.get(url=self.rid).url)[0]
            else:
                room_id = self.rid
            room_url = 'https://webcast.amemv.com/webcast/reflow/{}'.format(room_id)
            response = requests.get(url=room_url).text
            rtmp_pull_url = re.search(r'"rtmp_pull_url":"(.*?flv)"', response).group(1)
            hls_pull_url = re.search(r'"hls_pull_url":"(.*?m3u8)"', response).group(1)
            real_url = [rtmp_pull_url, hls_pull_url]
        except:
            raise Exception('直播间不存在或未开播或参数错误')
        return real_url


def get_real_url(rid):
    try:
        dy = DouYin(rid)
        return dy.get_real_url()
    except Exception as e:
        print('Exception：', e)
        return False


if __name__ == '__main__':
    r = input('请输入抖音直播间room_id或分享链接：\n')
    print(get_real_url(r))