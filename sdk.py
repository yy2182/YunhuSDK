import requests
from typing import Union
from sometypes import *
from json import loads

class Robot(object):
    def __init__(self, token):
        self.token = token

    def build_url(self, type:Union[send, upload]):
        if type != upload:
            return f"https://chat-go.jwzhd.com/open-apis/v1/bot/{type.__str__()}?token={self.token}"
        else:
            return f"https://chat-go.jwzhd.com/open-apis/v1/image/upload?token={self.token}"  # 傻逼云湖我得专门写个分支处理图片上传


    def uploadImage(self, imageAddress:str) -> str:
        """upload image to YunHu's server"""
        
        header = {"Content-Type": "multipart/form-data;"}

        # build body
        files=[('image',open(imageAddress,'rb'))]

        # do upload
        respon = requests.post(str(self.build_url(upload)), files=files, headers=header)

        # handle response
        return respon.text

    def send(self, 
            recvId, 
            recvType:uandg,
            contentType:types, 
            content,
            parentId=""):
        """给单个人或群发信息"""

        header = {"Content-Type": "application/json"}

        # build message body
        body = {
            "recvId": recvId,
            "recvType": recvType.__str__(),
            "contentType": contentType.__str__(),
            "content": {
                "text": content
            }
        }

        # do request
        respon = requests.post(self.build_url(send), json=body, headers=header)

        return respon.text
    
    def mass(self, recvIds:list, 
            recvType:uandg, 
            contentType:types, 
            content):  # TODO 具体实现
        """批量发信息"""
        pass

if __name__ == "__main__":
    bot = Robot("96274fc12eef473a9c71be5b1a230224")
    print(bot.uploadImage("./alhsk.jpg"))