from typing import Union

class user(object):
    def __str__():
        return "user"
    
class group(object):
    def __str__():
        return "group"
    
class text(object):
    def __str__():
        return "text"
    
class image(object):
    def __str__():
        return "image"
    
class file(object):
    def __str__():
        return "file"
    
class markdown(object):
    def __str__():
        return "markdown"

class html(object):
    def __str__():
        return "html"
    
class send(object):
    def __str__():
        return "send"
    
class batch_send(object):
    def __str__():
        return "batch_send"
    
class upload(object):
    def __str__():
        return "upload"
    
uandg = Union[user, group]  # user and group
types = Union[text, image, file, markdown, html]  # message types