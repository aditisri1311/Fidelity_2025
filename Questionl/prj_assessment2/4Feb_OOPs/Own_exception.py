class TooYoungException(Exception):
    def __init__(self, msg):
        self.msg = msg
age =5
if age<18:
    raise TooYoungException("Please wait")