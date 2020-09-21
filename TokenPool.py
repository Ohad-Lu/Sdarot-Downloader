from Token import Token
from queue import Queue


class TokenPool:
    tokens = Queue()

    def __init__(self, size):
        for i in range(size):
            self.put_token()

    def put_token(self):
        self.tokens.put(Token())

    def get_token(self):
        self.put_token()
        return self.tokens.get()
