# -*- coding: UTF-8 -*-"



'''

'''


import smtplib
import poplib
from email.parser import Parser
from email.mime.text import MIMEText
from email.header import decode_header


def decode_str(s):
    for value, charset in decode_header(s):
        if charset:
            value = value.decode(charset)
        yield value


class MailRobot():
    '''
    # 邮件机器人
    '''
    def __init__(self):
        self.smtpHost = 'smtp.yeah.net'                 #发件邮箱的smtp服务器地址
        self.popHost = 'pop.yeah.net'                   #收件邮箱的pop3服务器地址
        self.userName = 'ShawnGe yeah'                  #邮箱用户名
        self.mailName = 'shawnge'                       #邮箱名
        self.mailPWD = "GuidovanRossum00"               #授权码
        self.mailPostfix = 'yeah.net'                   #邮箱的后缀
            
    def getRawMsg(self):
        '''
        Get the raw message<~email.message.Message> which is encrypted by base 64.
        '''
        try:
            server = poplib.POP3(self.popHost)
            print(server.getwelcome().decode('utf-8'))
            receiver = '{0}@{1}'.format(self.mailName, self.mailPostfix)
            # 身份认证
            server.user(receiver)
            server.pass_(self.mailPWD)
            # 读取邮件列表
            _, msgNum, _ = server.list()    # response, msg_num, octets
            # 总邮件数
            totalMailsNum=len(msgNum)
            # 从最后一封邮件开始收取        
            for i in reversed(range(1, totalMailsNum+1)):
                # 读取邮件
                resp_, mailMessageLines, octets_ = server.retr(i)  #response, msg lines, octets、
                msgContent = b'\r\n'.join(mailMessageLines).decode('gbk')   # 合并msg lines
                # 解析邮件
                yield resp_, Parser().parsestr(text=msgContent), octets_
                
        except Exception:
            raise
        
        finally:
            server.quit()