#python 기초와 tensorflow
#딥카피

import copy

a = [1,2, [3,4]]
b = copy.deepcopy(a)

a[-1][0] = 1
#print(a)
#print(b)

##############################
a = {
    "apple" : "abc",
    "bbbbb" : "cba"
}

b = {"a":"apple"}

a.update(b)

#print(a)

##############################
# byte 자료형
a = b"abc"
b = "abc"
c = b.encode("ascii")
c = b.encode("latin-1")
d = c.decode("latin-1")
#print(d)

##############################
# set
a = {1, 2, 3}
b = {3, 4, 5}
#print( (a | b) )
#print( (a & b) )
#print( a - b )

##############################
# None
a = None


##############################
# condition

if a == 1:
    pass
else:
    pass

##############################
{1:"a", 2:"b", 3:"c"}.keys()
{1:"a", 2:"b", 3:"c"}.values()
{1:"a", 2:"b", 3:"c"}.items()


##############################
# 예외처리
a = []
try:
    print(a[0])

except ZeroDivisionError:
    pass

except IndexError as e:
    #raise e
    pass

except Exception:
    raise Exception()
    pass

finally:
    # 예외 발생 여부에 상관없이 실행
    pass

##############################
# 함수

def hello():
    pass

def hello2(msg):
    pass

def hello3(msg="hello"):
    pass

def hello4(*msg): #가변인자
    print(msg)

def hello5(**msg): #가변키워드인자
    print(msg)

#hello5(msg="123", msg2="456", msg3="789")
#hello4("agh", "bgf")

#hello2(msg="bag") #키워드 인자 전달방식

lambda : "" #no param
lambda x,y,z : "" #params

##############################
# class

class Abc:
    name = "aa"

    def __init__(self):
        pass

    def print(self):
        print("class Abc")
        print(self.name)
        self.name = "bcd"
        print(self.name)

        pass

    pass


#class_a = Abc()
#class_a.print()

#class 상속
class BCd:
    def abc(self):
        print("abc")
    pass

class BCd2:
    def abc(self):
        print("abc2")
    pass

class CDE(BCd, BCd2):
    pass

class DEF(BCd, CDE):
    pass

d = DEF()
c.abc()

