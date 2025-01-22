from yhtypes import *

"""
这里全是私有函数 除非你清楚你正在做什么 否则请勿调用
"""

def buildBaseRequestBody(recvId:types, recvType:uandg):
    requestBody = {
        "recvId": recvId,
        "recvType": recvType.__str__(),
    }

    return requestBody

def buildUploadImageBody(recvId, recvType, content):
    body = buildBaseRequestBody(recvId=recvId, recvType=recvType)
    body["contentType"] = "image"
    body["content"] = {"imageKey":content}

    return body

def buildSendTextMessageBody(recvId, recvType:uandg, contentType:types, content):
    body = buildBaseRequestBody(recvId=recvId, recvType=recvType)
    body["contentType"] = contentType.__str__()
    body["content"] = {"text":content}

    return body