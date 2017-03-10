#coding:utf-8

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog2',      #数据库里的database名称
        'USER': 'root',         #进入数据库的用户名
        'PASSWORD': '100200',   #密码
        'HOST': '127.0.0.1',
        'PORT': '3306',
        }
    }
 
email_conf={
    "EMAIL_BACKEND" : 'django.core.mail.backends.smtp.EmailBackend', #email后端    
    "EMAIL_USE_TLS" : False,  #是否使用TLS安全传输协议    
    "EMAIL_USE_SSL" : True,    #是否使用SSL加密，qq企业邮箱要求使用，网易邮箱则不需要
    "EMAIL_HOST" : 'smtp.126.com',   #发送邮件的邮箱 的 SMTP服务器
    "EMAIL_PORT" : 25,    #发件箱的SMTP服务器端口
    "EMAIL_HOST_USER" : 'jaket5219999@126.com',   #发送邮件的邮箱地址
    "EMAIL_HOST_PASSWORD" : '9999',       #发送邮件的邮箱密码
    "DEFAULT_FROM_EMAIL" : 'jaket5219999@126.com',      #这项可要可不要
}

#七牛云存储的权限校验机制基于一对密钥，分别称为Access Key和Secret Key。
#其中Access Key是公钥，Secret Key是私钥。这一对密钥可以从七牛的后台获取。
qiniu_keys={
    'access_key':"-1E2wJUzd-EXy7Yfimpv4OoCVJrWt2OBDzfUmiqb",
    'secret_key':"1idK013nXsDQEnyvhLxxKm0mKLGwZ4e9ZhBGu_BC",
}
qiniu_bucket={
    'bucket_name':'ziyituixun',   #要上传的空间  
    'bucket_domain':'okw0cf8ob.bkt.clouddn.com',    #获取文件url路径时对应的私有域名
}
qiniu_conf=dict(qiniu_keys,**qiniu_bucket)    #so pythonic to add two dict
