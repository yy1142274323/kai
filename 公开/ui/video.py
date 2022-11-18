import requests, json, os, sys, re, time
from copyheaders import headers_raw_to_dict


path = os.path.dirname(os.path.realpath(sys.argv[0]))

class Haokan(object):
    def first(self):
        headers = headers_raw_to_dict(
            b'''
            accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
            accept-encoding: gzip, deflate, br
            accept-language: zh-CN,zh;q=0.9
            cache-control: max-age=0
            cookie: BIDUPSID=49CAC47FE4B80211CDB92D98DD8CC4D2; PSTM=1603100046; BAIDUID=49CAC47FE4B8021148EF8FD12BDA92F1:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=33213_1445_33221_33212_33306_33236_31660_33284_33183_33181_33313_33312_33311_33310_33218_33309_26350_33199_33308_33307_33240_33217_33148_33216_33215_33185; BA_HECTOR=042k0g8h21242g016h1fto4tk0q; delPer=0; PSINO=2; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1608259061; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1608259061
            sec-fetch-dest: document
            sec-fetch-mode: navigate
            sec-fetch-site: none
            sec-fetch-user: ?1
            upgrade-insecure-requests: 1
            user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
            
            '''
        )

        url = 'https://haokan.baidu.com/author/1628033331417655'

        r = requests.get(url = url, headers = headers).text
        # print(r)
        pattern = 'video_src":"(.*?)mp4'

        video_url_list = re.findall(pattern, r)
        # print(video_url_list)
        for video_url in video_url_list:
            video_url = video_url + 'mp4'
            print(video_url)





    def next_page(self):
        # headers = headers_raw_to_dict(
        #     b'''
        #     accept: */*
        #     accept-encoding: gzip, deflate, br
        #     accept-language: zh-CN,zh;q=0.9
        #     cache-control: no-cache
        #     content-type: application/x-www-form-urlencoded
        #     cookie: BIDUPSID=49CAC47FE4B80211CDB92D98DD8CC4D2; PSTM=1603100046; BAIDUID=49CAC47FE4B8021148EF8FD12BDA92F1:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=33213_1445_33221_33212_33306_33236_31660_33284_33183_33181_33313_33312_33311_33310_33218_33309_26350_33199_33308_33307_33240_33217_33148_33216_33215_33185; BA_HECTOR=042k0g8h21242g016h1fto4tk0q; delPer=0; PSINO=2; Hm_lvt_4aadd610dfd2f5972f1efee2653a2bc5=1608259061; PC_TAB_LOG=video_details_page; COMMON_LID=4ce67626a9a197de23e4aec059b4caf2; Hm_lpvt_4aadd610dfd2f5972f1efee2653a2bc5=1608259209; ab_sr=1.0.0_ZWQ0YWQ0ODY3OGQ5MWQ2NmE2ZTAyYzUxMjViNjhjODRkNWI4NGQxOTk3YWQxNzRkNjBjZmFhY2JkNDdjZjVlMmI2YTY1MjA4ZjEzODI2ZDFmOTgzNTIzYjI2OWU3MmIw; reptileData=%7B%22data%22%3A%22b77ebd5bde6610c2772b6003d90ad55b0193aa4daea5261521a0222b03cf5a8772ff8abf3cda4f3bc2a1cae01ea8057e3d559e3120ff9c5ef177af86a2901620f3953208925593e8ee3beff677c679f1fd873b5c8f0f38bb2aac0c9ad74dca316217695432b8696ea9897263b60518473438db678bf7ba472bc0a2614d0288a2%22%2C%22key_id%22%3A%2230%22%2C%22sign%22%3A%22ce7098d9%22%7D
        #     referer: https://haokan.baidu.com/author/1628033331417655
        #     sec-fetch-dest: empty
        #     sec-fetch-mode: cors
        #     sec-fetch-site: same-origin
        #     user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
        #
        #     '''
        # )

        # ti = 16082207990005

        ti = time.time() * 10000 + 3
        url = 'https://haokan.baidu.com/author/1628033331417655?_format=json&rn=16&ctime={}&_api=1'.format(str(ti))
        r = requests.get(url = url).text
        print(r)
        res = json.loads(r)
        v_list = res['data']['response']['results']
        # print(v_list)
        print('共有 {} 个视频'.format(str(len(v_list))))
        n = 1
        for vi in v_list:
            title = vi['content']['title']
            video_url = vi['content']['video_src']
            print('标题为：{0}，视频链接为：{1}'.format(title, video_url))
            self.download(video_url, n)
            n += 1



    def download(self, video_url, n):
        url = video_url

        r = requests.get(url = url).content

        with open(path + '\\' + '视频下载\\{}.mp4'.format(str(n)), 'wb') as f:
            f.write(r)


class Xigua(object):
    def first(self):
        headers = headers_raw_to_dict(
            b'''
            accept: application/json, text/plain, */*
            accept-encoding: gzip, deflate, br
            accept-language: zh-CN,zh;q=0.9
            cookie: ttwid=1%7C3EPCbeISsv4_lAsPmdgy0XC5QuNIVnJoclKNaSQfMEE%7C1608264585%7C304fc598dc868a59f8f677f615d973359d761cf587ee06c6eccd52bb99c81a51; ixigua-a-s=0; MONITOR_WEB_ID=f207f603-00be-4e05-bc58-50336369eaf6; Hm_lvt_db8ae92f7b33b6596893cdf8c004a1a2=1608264588; Hm_lpvt_db8ae92f7b33b6596893cdf8c004a1a2=1608264588; _ga=GA1.2.23026382.1608264588; _gid=GA1.2.1429506454.1608264588
            referer: https://www.ixigua.com/home/95767439500
            sec-fetch-dest: empty
            sec-fetch-mode: cors
            sec-fetch-site: same-origin
            tt-anti-token
            user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36
            
            
            '''
        )

        url = 'https://www.ixigua.com/api/videov2/author/video?author_id=95767439500&type=video&max_time=0&_signature=_02B4Z6wo00f015ms2MwAAIBCJo21dV06BbOZrdxAALnC8b'
        r = requests.get(url = url, headers = headers).text
        result = json.loads(r)
        print(result)
        res_list = result['data']['data']
        for res in res_list:
            # print(res)
            title = res['abstract']
            video_url = res['article_url']

    def download(self):
        url = 'https://v9-xg-web-s.ixigua.com/18f30c511023af9c9319c61e8730af55/5fdc3cbc/video/tos/cn/tos-cn-o-0004/9e68346e49354c42be7f2aca259ee4e3/media-video-avc1/'

        r = requests.get(url = url).content

        with open(path + '\\' + '视频下载\\{}.mp4'.format(str(111)), 'wb') as f:
            f.write(r)

if __name__ == '__main__':
    # h = Haokan()
    # h.next_page()
    # h.first()

    x = Xigua()
    x.first()
    # x.download()














