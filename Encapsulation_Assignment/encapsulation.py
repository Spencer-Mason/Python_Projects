#Demonstrating encapsulation, creating protected and private properties
class Protected:
    def __init__(self):
        #Protected is prefixed with a single underscore
        self._protectedVar = 3
        #Private is prefixed with a double underscore
        self.__privateVar = 9
    #Private is harder to modify, requiring a method to access
    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
#Protected can be accessed/modified outside the class, as it is just a naming
#convention and doesn't change the behavior of anything, but it is discouraged
#because it defeats the purpose of it being protected
print(obj._protectedVar)
obj._protectedVar = 9
print(obj._protectedVar)
#As previously stated, a method is necessary to access private attributes/functions
obj.getPrivate()
obj.setPrivate(3)
obj.getPrivate()
