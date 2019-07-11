# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:11:53 2019

@author: 一文 --最远的你们是我最近的爱
"""

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse

import json

import time

import jpype

from play_ks.ks_spider import Ks_spider

import os

import multiprocessing

from play_ks.kuaishou import kuaishou


def load_jar():# 加载jar包
    
    jarpath = os.path.join(os.path.abspath("."), "/code/play_ks/")
        
    jvmPath = jpype.getDefaultJVMPath()
        
    jpype.startJVM(jvmPath, "-ea","-Djava.class.path=%s" % (jarpath + 'ks_sig.jar'))
    
    return jpype.JClass("SingatureUtil")
        
def get_index_info(q):
    
    javaClass = load_jar()
    
    info = kuaishou(javaClass).pro()
    
    q.put(info)
    
def get__comment_info(q,uid,pid):
    
    javaClass = load_jar()
    
    info = Ks_spider(javaClass).get_args(uid,pid)
    
    q.put(info)
    
def get__video_info(q,uid):
    
    javaClass = load_jar()
    
    info = kuaishou(javaClass).zuoping(uid)
    
    q.put(info)
    

def index(request):#首页API随机加载20视频

    start=time.time()

    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=get_index_info, args=[q])
    
    p.daemon = True
    
    p.start()
        
    info = q.get()
    
    index_info = []
        
    for i in info:
        
        try:
        
            if i['main_mv_urls'][1]['url'][0:13] == 'http://txmov2':
                                
                i['play_url'] = i['main_mv_urls'][1]['url']

                index_info.append(i)
                
            
            if i['main_mv_urls'][1]['url'][0:13] != 'http://txmov2':
                
                i['play_url'] = i['main_mv_urls'][0]['url']
                
                index_info.append(i)
                
        except KeyError:
            
            info.remove(i)
            
    index_info = [i for i in index_info if i['play_url'][0:13]=='http://txmov2']
        
    context = {'filmlist':index_info}
    
    p.terminate()
            
    print('耗时:',time.time()-start)

    return render(request, 'myks/index.html',context)#    return JsonResponse(context)

def comment(request):#作品评论接口
    
    uid = request.GET.get('uid')
    
    pid = request.GET.get('pid')
    
    start=time.time()

    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=get__comment_info, args=[q,uid,pid])
    
    p.daemon = True
    
    p.start()
        
    info = q.get()
    
    print('耗时:',time.time()-start)
    
    context = {'comment_info':info}
    
    return JsonResponse(context)

    
def pc(request):

    uid = request.GET.get('uid')
    
    start=time.time()

    q = multiprocessing.Queue()
    
    p = multiprocessing.Process(target=get__video_info, args=[q,uid])
    
    p.daemon = True
    
    p.start()
        
    info = q.get()
    
    print('耗时:',time.time()-start)
    
    context = {'comment_info':info}
    
    return JsonResponse(context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

