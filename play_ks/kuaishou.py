# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:11:53 2019

@author: 一文 --最远的你们是我最近的爱
"""

import requests
from spider import Spider

class kuaishou:
    
    def __init__(self,javaClass):
        
        self.t = javaClass()
        
        self.rst2 =[]
        
        self.pcursor = None
        
        self.datalist = []
        
    
    def get_movies(self):#随机获取20个视频
        
        try:
            
            url = 'http://101.251.217.216/rest/n/feed/hot?isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=59942a6c1d534a51844dfda37e92afc3&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=23&refreshTimes=7&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=510e56b366931c4cb008c51ee44664c2'
            
            return Spider().get_html(url)
        
        except Exception as e :
            
            print(e.args)
    
    def get_info(self):
        
        url = 'http://140.143.173.241/rest/n/feed/hot?isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&extId=59942a6c1d534a51844dfda37e92afc3&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&type=7&page=1&coldStart=false&count=20&pv=false&id=23&refreshTimes=7&pcursor=&source=1&needInterestTag=false&client_key=3c2cd3f3&os=android&sig=510e56b366931c4cb008c51ee44664c2'
    
        r = requests.get(url)
        
        r.encoding = r.apparent_encoding
        
        rst = r.json()['feeds']
        
        for i in rst :
            
            if  'main_mv_urls'and 'main_mv_urls_sd_h265' in i :
                caption = i['caption']  #标题
                
                commenet_count = i['comment_count'] #评论人数
                
                headurl  = i['headurls'][1]['url']  #作品图片url连接
                
                like_count = i['like_count']  #点赞人数
                
                bourl = i['main_mv_urls_sd_h265'][1]['url'] #播放地址
                
                xiaurl = i['main_mv_urls'][1]['url'] #下载地址
            
                photo_id = i['photo_id']  
                
                if 'soundTrack' in i :
                    soundTrack_music_url = i['soundTrack']['audioUrls'][0]['url'] #音乐链接
                    
                    soundTrack_img = i['soundTrack']['avatarUrls'][0]['url'] #图片链接
                    
                    soundTrack_id  = i['soundTrack']['id']
                    
                    soundTrack_artist  = i['soundTrack']['artist']
                    
                    soundTrack_name = i['soundTrack']['name']
                    
                    soundTrack_type = i['soundTrack']['type']
                    
                    try :
                        
                        soundTrack_user_eid =i['music']['user']['eid']
                       
                        
                    
                    except KeyError:
                        soundTrack_user_eid = " "
                
                elif 'music' in i :
                    soundTrack_music_url = i['music']['audioUrls'][0]['url'] #音乐链接
                    
                    soundTrack_img = i['music']['avatarUrls'][0]['url'] #图片链接
                    
                    soundTrack_id  = i['music']['id']
                    
                    soundTrack_artist  = i['music']['artist']
                    
                    soundTrack_name = i['music']['name']
                    
                    soundTrack_type = i['music']['type']
                    
                    try :
                        
                        soundTrack_user_eid =i['music']['user']['eid']
            
                    
                    except KeyError:
                        soundTrack_user_eid = " "
                
                try :
                    kwaiId  =i['kwaiId'] 
                except KeyError:
                    kwaiId='此账号无快手id'
                
                user_headurl = i['headurls'][0]['url']  #下载
                
                view_headurl = i['headurls'][1]['url']  #查看头部url
            
                user_id = i['user_id'] 
                
                user_name = i['user_name'] 
                
                user_sex = i['user_name'] 
                
                if 'F' in user_sex:
                    
                    user_sex = '女'
                    
                elif 'M' in user_sex :
                    
                    user_sex = '男'
                
                else :
                    
                    user_sex = ''
                    
                times = i['time'] #更新时间 
                
                timestamp = i['timestamp']
                
                user_type = i['type']
                    
                view_count = i['view_count']  #播放人数
                
                
                data = {'caption':caption,'commenet_count':commenet_count,'headurl':headurl,'like_count':like_count,\
                        'bourl':bourl,'xiaurl':xiaurl,'photo_id':photo_id,'soundTrack_music_url':soundTrack_music_url,\
                        'soundTrack_img':soundTrack_img,'soundTrack_id':soundTrack_id,'soundTrack_artist':soundTrack_artist,'soundTrack_name':soundTrack_name,\
                        'soundTrack_type':soundTrack_type,'soundTrack_user_eid':soundTrack_user_eid,'user_headurl':user_headurl,\
                        'view_headurl':view_headurl,'kwaiId':kwaiId,\
                        'user_id':user_id,'user_name':user_name,'user_sex':user_sex,'time':times,\
                        'timestamp':timestamp,'user_type':user_type,'view_count':view_count
                        }
                
                if data not in self.datalist:
                    
                     self.datalist.append(data)
            else :
                
                print('此视频为图片视频')
                
    
    def java(self,srcstr):#调用java jar包获取加密参数sig
          
        sig = self.t.run(srcstr)
      
        return sig
    
    def get_zuoping(self,url,vurl):
        
        sig = self.java(vurl)
        
        v_url = url+vurl+'&sig='+sig.lower()
        
        r = requests.get(v_url)
        
        r.encoding = r.apparent_encoding
        
        rst = r.json()
        
        self.rst2.append(rst['feeds'])
        
        return rst 
    
    def pro(self):
        
        infos = self.get_movies()
        
        pids = [(i['photo_id'],i['user_id']) for i in infos['feeds']]
                
        ls = []
        
        for i in pids:
            
            info = self.zuoping(i[1])
            
            try:
                
                sp = [j for j in info['feeds'] if j['photo_id'] == i[0]]

                ls.append(sp)
                
            except KeyError:
                
                print('error')
            
        ls = [i for i in ls if len(i)!=0]
        
        ls = [i[0] for i in ls]
                                            
        return ls
    
    
    def zuoping(self,user_id):
     
        url = 'http://api.ksapisrv.com/rest/n/feed/profile2?'
        
        url = 'http://140.143.173.241/rest/n/feed/profile2?'
        
        vurl = 'isp=CMCC&mod=vivo%28vivo%20x5m%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_d1f47e9473209293&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560817030537&ver=6.1&retryTimes=1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&referer=ks%3A%2F%2Fprofile%2F1253495500%2F5254856356897643841%2F1_a%2F1636737039616946179_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id)
        
        rst2 = self.get_zuoping(url,vurl)
            
        self.pcursor=rst2['pcursor']
        
        print(rst2['pcursor'])
        
        return rst2
    
    def dowork(self,user_id,pcursor):
        
        url = 'http://140.143.173.241/rest/n/feed/profile2?'
    
        vurl = 'isp=CMCC&mod=lemobile%28le%20x620%29&lon=116.41025&country_code=cn&kpf=ANDROID_PHONE&did=ANDROID_72c3ac6bd3184a67&kpn=KUAISHOU&net=WIFI&app=0&oc=MYAPP%2C1&ud=0&hotfix_ver=&c=MYAPP%2C1&sys=ANDROID_5.1.1&appver=6.1.0.8039&ftt=&language=zh-cn&iuid=&lat=39.916411&did_gt=1560736770695&ver=6.1&max_memory=192&token=&user_id={}&lang=zh&count=30&privacy=public&pcursor={}&referer=ks%3A%2F%2Fprofile%2F118261131%2F5211227733411179550%2F1_i%2F1636757237963010050_h86%2F8&client_key=3c2cd3f3&os=android'.format(user_id,pcursor)           
        
        try:
            
            rst =self.get_zuoping(url,vurl)
            
            self.pcursor = rst['pcursor'] 
            
            print(rst['pcursor'])
        
        except Exception as e:
           
            print(e.args)
    
    def zuopinghou(self,user_id):

        while True :
            
            self.dowork(user_id,self.pcursor)
                              
            if self.pcursor == 'no_more' :
                
                break 
            
if __name__ == '__main__' :
    
    x = kuaishou()

    
    








