import json,requests

class ApiTelegram:
    def __init__(self):
        self.url = 'https://api.telegram.org/bot{token}/sendMessage'
        with open("./config/config.json","r") as f:
            conf = json.load(f.read())
        self.token = conf["KEY_TELEGRAM"]
    def sendMessage(self,message):
        try:
            url = self.url.format(token=self.token)
            data = {'chat_id':"5266064105",'text':message}
            response = requests.post(url,data=data)
            return {"ok":response.json()}
        except Exception as e:
            return {"error":str(e)}
        
def init():
    try:
        global apiTelegram
        apiTelegram = ApiTelegram()
    except Exception as e:
        print("error:",e)
        