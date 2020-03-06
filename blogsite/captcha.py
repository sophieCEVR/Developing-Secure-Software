#
#

import random


class Captcha:
    def __init__(self):
        self.key = self.getkey()
        self.numa = self.randhigh()
        self.numb = self.randlow()
        self.total = self.sum()
        self.op = self.getoperator()

    def getkey(self):
        return random.randrange(0, 3)

    def randlow(self):
        return random.randrange(1, 5)

    def randhigh(self):
        return random.randrange(1,20,5)

    def sum(self):
        if self.key == 0:
            return self.numa*self.numb
        elif self.key == 1:
            return self.numa-self.numb
        elif self.key == 2:
            return self.numa+self.numb

    def getoperator(self):
        if self.key == 0:
            return ' x '
        elif self.key == 1:
            return ' - '
        elif self.key == 2:
            return ' + '

    def checkinput(self, a):
        if self.sum() == int(a):
            return True
        else:
            return False

    def sumasstring(self):
        return str(self.numa) + str(self.op) + str(self.numb) + ' = '


if __name__ == '__main__':
    object = Captcha()
    object2 = Captcha()
    print(object.sumasstring())

    print(object.sum())

    input = input()
    print(object.checkinput(input))