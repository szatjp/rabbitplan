# coding:utf-8

'''
Created on 2011-11-17

@author: tongjp

'''

#from django.core import mail
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render_to_response

# 发送纯文本邮件
def sendtest():
    '''
    connection = mail.get_connection()
    # Manually open the connection
    connection.open()
    # Construct an e-mail message that uses the connection
    email1 = mail.EmailMessage('同京平，你好', '让我通过吧，my god!', 'smc-tjp@matsui.com.cn',
                          ['smc-oa@matsui.com.cn'], connection=connection)
    email1.send() # Send the e-mail
    connection.close()
    '''
    
    send_mail('你好, 同京平', '看到你太好了.', 'smc-oa@matsui.com.cn',
          ['smc-tjp@matsui.com.cn'], fail_silently=False)
    
    return 'success'


# 发送html邮件
def sendhtml(requset):
    subject, from_email, to = 'OA设备管理周报', 'smc-oa@matsui.com.cn', 'smc-tjp@matsui.com.cn'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>\
                   <table border="1"><tr><th>人名</th><th>学历</th></tr><tr><td>储娇</td><td>博士</td></tr></table>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return render_to_response('autotask/checkend.html') 
    #return 'success'    