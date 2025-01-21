import requests
from typing import Union
from typesofyh import *
from json import loads

class Robot(object):
    def __init__(self, token):
        self.token = token

    def build_url(self, type:Union[send, upload]):
        if type != upload:
            return f"https://chat-go.jwzhd.com/open-apis/v1/bot/{type.__str__()}?token={self.token}"
        else:
            return f"https://chat-go.jwzhd.com/open-apis/v1/image/upload?token={self.token}"  # 傻逼云湖我得专门写个分支处理图片上传


    def uploadImage(self, imageStream:str) -> str:
        """upload image to YunHu's server"""

         # build body
        imageFile = open(imageStream,'rb')
        files = {"image":imageFile}

        # do upload
        respon = requests.post(self.build_url(upload), files=files)

        imageFile.close()

        # handle response
        try:
            return loads(respon.text)["data"]["imageKey"]
        except:
            return respon.text

    def send(self, 
            recvId, 
            recvType:uandg,
            contentType:types, 
            content,
            parentId=""):
        """
        给单个人或发信息
        若contentType为image 则在content输入图片文件（用open打开的）
        """

        header = {"Content-Type": "application/json"}

        if contentType == image:
            content = self.uploadImage(content)

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