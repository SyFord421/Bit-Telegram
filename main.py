import requests


HHTP_API_BOT = "<Masukan token>"
ID_CHAT = "<Masukan ID chat>"

class BaseBot:
    def __init__(self, bot_token, id_chat):
        self.bot_token = bot_token
        self.id_chat = id_chat
    def send_message(self, text):
        try:
            url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
            msg = requests.post(url, data={"chat_id": self.id_chat, "text": text
            })
            if msg:
                print("[!]Pesan Telah Terkirim")
        except Exception as e:
            print(f"[!] Error {e}" 
if __name__ == "__main__":
    BB = BaseBot(HHTP_API_BOT, ID_CHAT)
    BB.send_message("Testing woi")
