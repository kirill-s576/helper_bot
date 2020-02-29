from applications.app_router import AppRouter
from utils.user import User

class Request(object):
    def __init__(self, message_or_call):
        try:
            self.call = message_or_call
            self.message = message_or_call.message
        except:
            self.call = None
            self.message = message_or_call

        self.for_app = ""
        self.user = User().set(self.message.chat.id)
        self.application = AppRouter(self)


class Responce(object):
    def __init__(self, request):
        self.text = ""
        self.keyboard = ""

    def send(self):
        pass



def main_router(com):
    request = Request(com)
    responce = Responce(request)
    responce.send()