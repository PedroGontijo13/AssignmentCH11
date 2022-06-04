class MyList:
    def __init__(self, items):
        self._myList = items

    def addItem(self, item):
        if item not in self._myList:
            self._myList.append(item)


    def calculateMax(self):
        return max(self._myList)

    def calculateSum(self):
        return sum(self._myList)

    def printList(self):
        print(self._myList)

class TestMyList:
    @staticmethod
    def testList():
        customList = MyList([5,22,45])
        print("INITIAL LIST:")
        customList.printList()
        print("ADD EXISTING ITEM")
        customList.addItem(22)
        print("List after")
        customList.printList()
        print("ADDING 50 and 70")
        customList.addItem(50)
        customList.addItem(70) 
        print("List after")
        customList.printList()

        print("SUM =", customList.calculateSum())
        print("MAX =", customList.calculateMax())

def main():
    TestMyList.testList()

main()
        