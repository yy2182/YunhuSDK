import requests
from typing import Union
from yhtypes import *
import bodyBuilder
from json import loads

class Robot(object):
    def __init__(self, token):
        self.token = token

    def build_url(self, type:Union[send, upload, batch_send]):
        if type != upload:
            return f"https://chat-go.jwzhd.com/open-apis/v1/bot/{type.__str__()}?token={self.token}"
        else:
            return f"https://chat-go.jwzhd.com/open-apis/v1/image/upload?token={self.token}"  # 傻逼云湖我得专门写个分支处理图片上传

    def uploadImage(self, imageStream:str) -> str:
        """upload image to YunHu's server"""

        # Build request body
        files = {"image":imageStream}

        respon = requests.post(self.build_url(upload), files=files)

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
        若contentType为image 则在content输入图片文件
        """

        header = {"Content-Type": "application/json"}

        match contentType:
            case image.__str__():
                body = bodyBuilder.buildUploadImageBody(recvId=recvId, recvType=recvType,content=content)
            case _:
                body = bodyBuilder.buildSendTextMessageBody(recvId=recvId, recvType=recvType, contentType=contentType.__str__(), content=content)

        # do request
        respon = requests.post(self.build_url(send), json=body, headers=header)

        return respon.text
    
    def mass(self, recvIds:list, 
            recvType:uandg, 
            contentType:types, 
            content):
        """批量发信息"""

        # build body
        match contentType:
            case image.__str__():
                bodyBuilder.buildBatchSendImageBody(recvIds=recvIds,recvType=recvType,content=content)
            case _:
                body = bodyBuilder.buildBatchSendMessageBody(recvIds=recvIds, recvType=recvType, contentType=contentType.__str__(), content=content)

        # do request
        requests.post(self.build_url(batch_send), json=body)
