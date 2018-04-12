
def bulk(self):
    print("%s is yelling..." %self.name)

class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating....%s" %(self.name,food))

d = Dog("xiaobai")
choice = input(">>:").strip()

#getattr 根据字符串去获取obj对象里的对应的方法的内存地址
#hasattr 是判断是有输入的方法 或者变量什么的
if hasattr(d,choice):
    getattr(d,choice)

else:
    setattr(d,choice,None)
    print(d.age)
    # v= getattr(d,choice)
    # print(v)

