class Test:
    x = 10 #public
    _y= 20 #protected- within the class, 
    __z= 30 #private
    def  m1(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        
obj = Test()
obj.m1()

        
    