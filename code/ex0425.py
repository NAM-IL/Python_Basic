# 점프 투 파이썬 : 클래스로 사칙연산 실습
import os
import psutil

class FourCal:
    
    def setData(self, first, second):
        self.first = first
        self.second = second
    
    def add(self):
        result = self.first  + self.second
        return result
    
    def sub(self):
        result = self.first  - self.second
        return result
    
    def mul(self):
        result = self.first  * self.second
        return result

    def div(self):
        result = self.first  / self.second
        return result

if __name__ == "__main__":
    # Terminal을 clear(macOS, Linux) 또는 cls(Windows) 명령어로 초기화
    # os.name: posix (macOS, Linux), nt (Windows)
    # [How to identify which OS Python is running on](https://stackoverflow.com/questions/1854/how-to-identify-which-os-python-is-running-on)
    if(psutil.WINDOWS):
        os.system("cls")
    else:
        os.system("clear")
    
    a = FourCal()
    b = FourCal()
    
    a.setData(4, 2)
    b.setData(3, 8)
    
    a.mul()
    a.sub()
    a.div()
    a.mul()
    
    b.add()
    b.mul()
    b.sub()
    b.div()