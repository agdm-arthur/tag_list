class PersonalArray:
    SIZE = 5
    insertPosition = 0
    elements = [None] * SIZE

    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return self.insertPosition

    def isMemoryFull(self):
        return self.insertPosition == len(self.elements)

    def append(self, newElement):
        if self.isMemoryFull():
            self.updateMemory()
        self.elements[self.insertPosition] = newElement
        self.insertPosition += 1

    def updateMemory(self):
        newArray = [None] * (self.size() + self.SIZE)
        for position in range(self.insertPosition):
            newArray[position] = self.elements[position]
        self.elements = newArray
    
    def clear(self):
        self.elements = [None] * self.SIZE
        self.insertPosition = 0
    
    def remove(self):
        if not self.isEmpty():
            self.elements[self.insertPosition - 1] = None
            self.insertPosition -= 1

    def removePosition(self, position):
        if position < 0 or position >= self.insertPosition:
            print("PosiÃ§Ã£o invÃ lida")
            return
        for i in range(position, self.insertPosition - 1):
            self.elements[i] = self.elements[i + 1]
        self.elements[self.insertPosition - 1] = None
        self.insertPosition -=1

    def insertAt(self, position, newElement):
        if position < 0 or position > self.insertPosition:
            print("Posição inválida!")
            return
        if self.isMemoryFull():
            self.updateMemory()
        index = self.insertPosition - 1
        while index >= position:  
            self.elements[index + 1] = self.elements[index]
            index -= 1
        self.elements[position] = newElement
        self.insertPosition += 1   

    def elementAt(self, position):
        if position < 0 or position >= self.insertPosition:
            print("Posição inválida!")
            return None
        return self.elements[position]

class PersonalStack:
    list = PersonalArray()
    
    def listAll(self):
        print(self.list.elements)

    def push(self, newElement):
        self.list.insertAt(0, newElement)
    
    def pop(self):
        return self.list.removePosition(0)
    
tags = PersonalStack()
print("Write a word to add it to the tag list.\nYou can also use one of the following commands:"
"\n\\pop\n   Remove the last added tag."
"\n\\show\n   Shows all the tags.")


while True:
    print("")
    tags.listAll()
    decision = input(str(""))
    if decision == "\\show":
        None
    elif decision == "\\pop":
        tags.pop() 
    else:
        tags.push(decision)