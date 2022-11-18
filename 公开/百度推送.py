import requests, re, json

def get_urls(sitemap_url):
    # 爬取URL列表
    r = requests.get(sitemap_url).text
    s = re.findall(r'<loc>(.*)</loc>', r)
    # 由于百度推送一次最多推送2000条，如果超过两千，就取最后2000条推送
    print('已经成功爬取{0}条网址'.format(len(s)))
    if len(s) > 2000:
        s = s[-2000:]
    urls = '\n'.join(s)
    return urls

# def post_message_wechat(text):
#     # 推送推送结果至管理员微信
#     # 请获取属于你的corpid、corpsecret、agentid,替换下面代码中的*****
#     # 请参考：https://www.htm.fun/archives/python-flask-api-server-jiang.html
#     # 如果不需要该功能，请删掉第37行的 post_message_wechat(text) 即可
#
#     data = {
#         'corpid': '*****',
#         'corpsecret': '*****',
#         'agentid': '*****',
#         'text': text
#     }
#     r = requests.post('https://api.htm.fun/api/Wechat/text/',data=data)

def post_url_baidu(baidu_api_url,sitemap_url):
    # 进行推送到百度站长中心
    headers = {'Content-Type': 'text/plain'}
    urls = get_urls(sitemap_url)
    s = requests.post(baidu_api_url, headers=headers, data=urls).content
    s = json.loads(s)
    print(s)
    if 'success' in s.keys():
        text = '今日已成功提交-{}-条推送到百度站长剩余提交数量-{}-'.format(s['success'],s['remain'])
    else:
        text = '推送失败，请检查原因！'
    # post_message_wechat(text)
    print(text)

if __name__ == '__main__':
    # 将下方的baidu_api_url和sitemap_url换成你自己的URL即可！
    post_url_baidu('http://data.zz.baidu.com/urls?site=www.677688521.xyz&token=2afmGj1FTp2G07eo','http://677688521.xyz/sitemap.xml')










'''
a:2:{s:5:"child";a:1:{i:1;a:4:{i:0;a:6:{i:0;s:14:"TE插件仓库";i:1;s:14:"TE插件仓库";i:2;s:40:"extending.php?panel=TeStore%2Fmarket.php";i:3;s:13:"administrator";i:4;b:0;i:5;s:0:"";}i:1;a:6:{i:0;s:12:"蜘蛛日志";i:1;s:18:"查看蜘蛛日志";i:2;s:41:"extending.php?panel=RobotsPlus%2FLogs.php";i:3;s:13:"administrator";i:4;b:0;i:5;s:0:"";}i:2;a:6:{i:0;s:15:"Access控制台";i:1;s:21:"Access插件控制台";i:2;s:47:"extending.php?panel=Access%2Fpage%2Fconsole.php";i:3;s:10:"subscriber";i:4;b:0;i:5;s:0:"";}i:3;a:6:{i:0;s:15:"Access控制台";i:1;s:21:"Access插件控制台";i:2;s:47:"extending.php?panel=Access%2Fpage%2Fconsole.php";i:3;s:10:"subscriber";i:4;b:0;i:5;s:0:"";}}}s:4:"file";a:3:{i:0;s:20:"TeStore%2Fmarket.php";i:1;s:21:"RobotsPlus%2FLogs.php";i:2;s:27:"Access%2Fpage%2Fconsole.php";}}

a:2:{s:5:"child";a:2:{i:1;a:3:{i:1;a:6:{i:0;s:15:"Access控制台";i:1;s:21:"Access插件控制台";i:2;s:47:"extending.php?panel=Access%2Fpage%2Fconsole.php";i:3;s:10:"subscriber";i:4;b:0;i:5;s:0:"";}i:2;a:6:{i:0;s:12:"蜘蛛日志";i:1;s:18:"查看蜘蛛日志";i:2;s:41:"extending.php?panel=RobotsPlus%2FLogs.php";i:3;s:13:"administrator";i:4;b:0;i:5;s:0:"";}i:3;a:6:{i:0;s:14:"TE插件仓库";i:1;s:14:"TE插件仓库";i:2;s:40:"extending.php?panel=TeStore%2Fmarket.php";i:3;s:13:"administrator";i:4;b:0;i:5;s:0:"";}}i:3;a:0:{}}s:4:"file";a:3:{i:1;s:27:"Access%2Fpage%2Fconsole.php";i:2;s:21:"RobotsPlus%2FLogs.php";i:4;s:20:"TeStore%2Fmarket.php";}}

'''






