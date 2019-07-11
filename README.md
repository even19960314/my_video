# -
主流无水印视频(部分)


项目架构
ks:
        ks

        myks(django静态文件及视图函数)
        
        play_ks(核心代码):
	
                ks_sig.jar(Java jar包破解加密参数)
                
                ks_spider.py(获取评论数据接口)	
                
                kuaishou.py(加载视频接口,用户个人详情页接口)
                
        Dockerfile(构建Docker镜像)
        
        README.md
        
        manage.py
        
        requirements.txt(第三方依赖库)
        
        spider.py(封装了python requests get post请求)

使用时修改myks视图函数中JVM路径

交流QQ:86428264
微信:Dn54120
