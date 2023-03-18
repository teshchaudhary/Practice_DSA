class Stack:
    
    def __init__(self):
        self.__data = []
        
    def push(self,item):
        return self.__data.append(item)
    
    def pop(self):
        if len(self.__data) == 0:
            return "Stack is Empty"
        return self.__data.pop()
        
    def top(self):
        if len(self.__data) == 0:
            return "Stack is Empty"
        return self.__data[len(self.__data) - 1]
    
    def size(self):
        return len(self.__data)
    
    def isEmpty(self):
        return len(self.__data) == 0
