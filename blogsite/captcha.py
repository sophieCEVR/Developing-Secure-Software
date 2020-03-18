#
#

import random


class Captcha:
    # create object
    def __init__(self):
        self.key = self.getkey()
        self.numa = self.randhigh()
        self.numb = self.randlow()
        self.total = self.sum()
        self.op = self.getoperator()

    # return the key used to control the operator
    def getkey(self):
        return random.randrange(0, 3)

    # generate a random number between 1 and 5
    def randlow(self):
        return random.randrange(1, 5)

    # generate a random number between 1 and 20
    def randhigh(self):
        return random.randrange(1,20)

    # return the result of the sum dependent on the operator
    def sum(self):
        if self.key == 0:
            return self.numa*self.numb
        elif self.key == 1:
            return self.numa-self.numb
        elif self.key == 2:
            return self.numa+self.numb

    # return the operator character
    def getoperator(self):
        if self.key == 0:
            return ' x '
        elif self.key == 1:
            return ' - '
        elif self.key == 2:
            return ' + '

    # check the input (a) against the sum
    def checkinput(self, a):
        if self.sum() == int(a):
            return True
        else:
            return False

    # return the sum as a string (for easy printing to a console or webpage
    def sumasstring(self):
        return str(self.numa) + str(self.op) + str(self.numb) + ' = '


#for testing:
# if __name__ == '__main__':
#     object = Captcha()
#     object2 = Captcha()
#     print(object.sumasstring())

#     print(object.sum())

    #input = input()
    #print(object.checkinput(input))