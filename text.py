import sys
sys.path.append('.')
import requests
import numpy as np
import res
from datetime import datetime
def parse_json(response):
    map={}
    response=response['statuses']
    i=0
    for nav in response:
       
        submap={}
        
        submap['id']=str(nav['id'])
        submap['text_raw']=nav['text_raw']
        submap['screen_name']=nav['user']['screen_name']
        submap['created_at']=str(datetime.strptime(nav['created_at'], "%a %b %d %H:%M:%S %z %Y").strftime("%Y-%m-%d %H:%M:%S"))
        submap['comments_count']=str(nav['comments_count'])
        submap['reposts_count']=str(nav['reposts_count'])
        submap['attitudes_count']=str(nav['attitudes_count'])
        submap['source']=nav['source']
        map[i]=submap
        
        i+=1
    return map
def get_data(navs,typeNum=3,pageNum=2):


    url='https://weibo.com/ajax/feed/hottimeline'

    for i in range(min(len(navs),typeNum)):
        for j in range(pageNum):
            params={'group_id':navs[i]['gid'],'containerid':navs[i]['containerid'],'extparam':'discover|new_feed','max_id':j,'count':10}
            print(f"正在爬取{navs[i]['title']}")
            yield  parse_json(requests.get(url,headers=res.header,params=params).json())