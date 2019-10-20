# @Time : 2019/10/19 16:47
# @Author : GKL
# FileName : get_skin.py
# Software : PyCharm

import re
import time
import requests
from public.operation_db import *


def spider(tag, count, url, name):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    # 皮肤名称列表
    skin_name_list = re.findall(r'data-imgname="(.*?)"', response.text)[0].split('|')
    url_list = []
    for i in range(1, count+1):
        # 英雄皮肤url地址
        skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{0}/{0}-bigskin-{1}.jpg'.format(tag, i)
        url_list.append(skin_url)

    data_list = []
    for skin_name, url in zip(skin_name_list, url_list):
        data = [name, skin_name, url]
        data_list.append(data)

    # 插入数据
    insert_sql = 'insert into wzry_skin_url(name, skinName, skinUrl) values(%s, %s, %s)'
    save_batch_data(insert_sql, data_list)


if __name__ == '__main__':
    while True:
        select_sql = 'select name, url, count from wzry_detail_link where status=0 limit 1'
        tuple_data = select_data(select_sql)
        if tuple_data:
            # 英雄名称
            name = tuple_data[0][0]
            print(name)
            # 英雄详情
            url = tuple_data[0][1]
            # 英雄唯一标签
            tag = re.findall(r'\d+', url)[-1]
            # 英雄皮肤数量
            count = tuple_data[0][2]
            spider(tag, count, url, name)
            update_sql = 'update wzry_detail_link set status=1 where name = "%s"' % name
            update_data(update_sql)
            time.sleep(2)
        else:
            break


