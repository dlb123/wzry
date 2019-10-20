# @Time : 2019/10/19 15:49
# @Author : GKL
# FileName : get_detail.py
# Software : PyCharm

import  requests

from public.operation_db import *

url = 'https://pvp.qq.com/web201605/js/herolist.json'

resp = requests.get(url).json()
data_list = []
for i in resp:
    if 'skin_name' in i:

        skin_name = i['skin_name'].split('|')
        name = i['cname']
    else:
        skin_name = [i['title']]

    count = len(skin_name)

    detail_link = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(i['ename'])
    name = i['cname']
    data = [name, detail_link, count]
    data_list.append(data)



insert_sql = 'insert into wzry_detail_link(name, url, count) values(%s, %s, %s)'
save_batch_data(insert_sql, data_list)
