import random
import time
import datetime
import random

chars = '0123456789'

def localtime():
    time = datetime.datetime.now()
    return f'[{time.strftime("%H:%M:%S")}]'

def generator(number: int):
    num = 0
    for a in range(number):
        num += 1
        CODE = ''
        for a in range(10):
            CODE += random.choice(chars)
        time.sleep(0.4)
        print(f'{localtime()} [{num}] {CODE}')

def main():
    number = int(input('>>> '))
    print('='*53)
    generator(number)
    print('='*53)
    main()

if __name__ == '__main__':        
    print('How many robux promocodes do you need?')
    main()