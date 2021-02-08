# _*_ coding:utf-8 _*_
import random,string

def randomstr():
    "生成4-20位随机字符串"
    return ''.join(random.sample(string.ascii_letters, random.randint(4, 20)))

if __name__ == '__main__':
    print(randomstr())

