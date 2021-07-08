import os
import shutil
class Atm(object):
    def __init__(self,atmnumber,pin):
        self.atmnumber=atmnumber,
        self.pin=pin
    def start(self):
        print("Enter Your AtmNumber")
    def stop(self):
        print("Enter Your PIN")
SBI=Atm(70,4434)
print(SBI.atmnumber)
print(SBI.pin)
    
    