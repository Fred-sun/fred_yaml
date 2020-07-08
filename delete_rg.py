import os
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(flag,key):
    """Send an email to remind successfully deleted and undeleted resource group"""
    from_addr = 'xiuxi.sun@qq.com'
    password = 'djwgzuhzrqwubbcb'
    to_addr = ['v-xisu@microsoft.com', ]
    smtp_server = 'smtp.qq.com'
    if flag:
        content = "Success delete: " + key
    else:
        content = "Unsuccess delete: " + key

    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = Header(from_addr)
    msg['Subject'] = Header("Delete Unuse Resource Group")
    server = smtplib.SMTP_SSL()
    server.connect(smtp_server,465)
    server.login(from_addr, password)
    for mail_box in to_addr:
        msg['To'] = Header(mail_box)
        server.sendmail(from_addr, mail_box, msg.as_string())
    server.quit()


def Get_RG():
    """ Get resource group list func """

    list_id = []
    get_item = 'az group list --subscription f64d4ee8-be94-457d-ba26-3fa6b6506cef --output json'
    ret = os.popen(get_item).readlines()
    reg = '"id": "/subscriptions/f64d4ee8-be94-457d-ba26-3fa6b6506cef/'
    for resource in ret:
        if reg in resource:
            item = re.split(r'"|/',resource)[7]
            if item.startswith('sampletest'):
                list_id.append(item)

    return list_id

def Delete_RG(key):
     """ Delete resource group func """

     success_flag = True
     del_item = 'az group delete -y --name '
     print("The resource group :%s will be delete:"%key)
     try:
         os.system(del_item + key)
     except Exception:
         success_flag = False
         print(" Delete resource group %s error"%key)
     finally:
         send_mail(success_flag,key)

def main():

     list_id = Get_RG()
     for key in list_id:
         Delete_RG(key)

if __name__ == "__main__":
    main()
