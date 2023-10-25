import sys
sys.path.append('.')
import requests
import numpy as np
import datetime
import res


def getData(url):
    params={'is_new_segment':1,'fetch_hot':1}
    response=requests.get(url,headers=res.header,params=params)
    if(response.status_code==200):
        return response
    else:
        return None
def parse_json(response):
    # for i in [3,4]:
    #     print(i)
    #     print('\n')
    #     print(response['groups'][i])
    # print('\n')
    # print('\n')
    navlist=np.append(response['groups'][3]['group'],response['groups'][4]['group'])
    #print(navlist)
    map={}
    i=0
    for nav in navlist:
        #print(nav)
        submap={}
        submap['title']=nav['title']
        submap['gid']=nav['gid']
        submap['containerid']=nav['containerid']
        map[i]=submap
        i+=1
        # print(nav['gid'])
        # print(nav['containerid'])
    return map
def parse_json_1(response):
    map={}
    response=response['statuses']
    i=0
    for nav in response:
       
        submap={}
        
        submap['id']=nav['id']
        submap['text_raw']=nav['text_raw']
        submap['screen_name']=nav['user']['screen_name']
        submap['created_at']=nav['created_at']
        submap['comments_count']=nav['comments_count']
        submap['reposts_count']=nav['reposts_count']
        submap['attitudes_count']=nav['attitudes_count']
        submap['source']=nav['source']
        map[i]=submap
        print(map[i])
        i+=1
   # print(map)

