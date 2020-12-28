import requests
from retrying import retry
import json
import os


class DoubanTVSpider:

    def __init__(self):  # 初始化一个类
        self.tmp_url1 = 'https://accounts.douban.com/j/mobile/login/basic'
        self.tmp_url2 = 'https://m.douban.com/mine/'
        self.tmp_url3 = 'https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start={}&count=18&loc_id=108288&_=0'

    @retry(stop_max_attempt_number=10, wait_fixed=1000)
    def _post_request(self, post_url, get_url_mine, post_data, post_headers):
        post_session = requests.session()
        post_session.post(post_url, data=post_data, headers=post_headers)
        post_response = post_session.get(get_url_mine, headers=post_headers, timeout=1)
        return post_response.content.decode()

    def post_request(self, post_url, get_url_mine, post_data, post_headers):
        try:
            post_res = self._post_request(post_url, get_url_mine, post_data, post_headers)
            # print('POST Request Content:\n', post_res)
        except Exception:
            post_res = 'Post Request Failed.'
        return post_res


    def save_post_data(self, post_res):
        try:
            with open('douban_post_res.html', 'w', encoding='utf-8') as f:
                f.write(post_res)
            print('Save Post Data Successfully.')
        except(IOError, TimeoutError):
            print('Save Post Data Failed.')

    def parse_data(self, get_str):
        list_s1 = json.loads(get_str)
        list_s2 = list_s1['subject_collection_items']
        total = list_s1['total']
        count = list_s1['count']
        return list_s2, total, count

    def file_exit_dec(self, file_name):
        try:
            os.remove(file_name)
        except IOError:
            print('File does not exit, now you can append the file by "with open"! ')

    def save_data(self, list_data, file_name):
        try:
            with open(file_name, 'a', encoding='utf-8') as f:
                for list_ele in list_data:
                    str_ele = json.dumps(list_ele, ensure_ascii=False)
                    f.write(str_ele)
                    f.write(',\n')
            print('Save Data Successfully!')
        except(IOError, Exception):
            print('Failed Saving The Data.')

    def run(self):  # 程序主体

        # ******************************************************************************************************
        # POST请求，获取登录豆瓣后的页面数据
        # 1、POST请求数据准备
        print('*' * 100)
        post_url = self.tmp_url1
        get_url_mine = self.tmp_url2
        post_headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36'}
        post_data = {'ck': '', 'redir': 'https://m.douban.com', 'name': 'aaa', 'password': 'bbb'}

        # 2、POST请求登录
        post_res = self.post_request(post_url=post_url, get_url_mine=get_url_mine, post_data=post_data,
                                     post_headers=post_headers)

        # 3、POST数据保存
        self.save_post_data(post_res)

        # ******************************************************************************************************
        # GET请求，获取豆瓣电视剧的数据
        # 1、GET请求数据准备
        print('\n', '*' * 100, '\n')
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Mobile Safari/537.36',
            'Referer': 'https://m.douban.com/tv/american'}
        get_cookie = 'bid=aaa; douban-fav-remind=bbb; __utmc=ccc; …………'
        cookie_para = {get_co.split('=')[0]: get_co.split('=')[1] for get_co in get_cookie.split('; ')}
        start = 0
        total = 20
        count = 0
        get_file_name = 'json_douban_tv.html'
        self.file_exit_dec(get_file_name)

        while start < total + count:
            get_url = self.tmp_url3.format(start)

            # 2、发送请求，获取响应
            get_str = self.get_request_2(get_url, headers, cookie_para)

            # 3、提取数据
            list_s, total, count = self.parse_data(get_str)

            # 4、保存数据
            self.save_data(list_s, get_file_name)

            # 5、准备下一次url
            start += count

if __name__ == '__main__':
    tecent = DoubanTVSpider()
    tecent.run()