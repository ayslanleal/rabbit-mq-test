from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class Message:
    body: dict
    time: int

class MessagesCollection:
    def __init__(self) -> None:
        self.messages = list()
    
    def add(self, message):
        save_time = datetime.now()
        message = Message(message, datetime.timestamp(save_time))
        self.messages.append(message)\
    
    def response(self):
        resp = []
        for m in self.messages:
            resp.append(asdict(m))
        return resp




