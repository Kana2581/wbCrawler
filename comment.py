import sys
sys.path.append('.')
import requests
import numpy as np
import res
def parse_json(response):
    map={}
    response=response['data']
    i=0
    for nav in response:
       
        submap={}
        
    
        submap['text_raw']=nav['text_raw']
        submap['screen_name']=nav['user']['screen_name']
        submap['created_at']=nav['created_at']

        submap['like_counts']=nav['like_counts']
        submap['source']=nav['source']
        map[i]=submap
        print(map[i])
        i+=1
    return map
def get_data(id):


    url='https://weibo.com/ajax/statuses/buildComments'

    params={'id':id,'is_show_bulletin':'2','is_mix':0,'count':20}
    print(f"正在爬取评论id{id}")
    parse_json(requests.get(url,headers=res.header,params=params).json())
    #4958949038098777
get_data(4958949038098777)