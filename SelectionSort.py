class SelectionSort(object):


    def __init__(self, contents=None):

        if contents is None:
            self.__contents = []

        else:
            self.__contents = contents

    def __str__(self) -> str:
        return f"Contents: {self.__contents}"

    def sort(self):

        ## The index that the smallest found item will be placed into
        for startIndex, smallestItem in enumerate(self.__contents):
            
            # Work between bounds so that previously small items are re-evaluated
            for itemIndex in range(startIndex, len(self.__contents)):

                # The item that is going to be compared
                item = self.__contents[itemIndex]

                # If the item is smaller, make it the smallest Item!
                if item < smallestItem:
                    smallestItem = item
                    smallestIndex = itemIndex

            # Swap with the 'startIndex' entry
            tempItem = self.__contents[startIndex]
            self.__contents[startIndex] = smallestItem
            self.__contents[smallestIndex] = tempItem


            
            


test = SelectionSort([4, 6, 1, 9, 6, 5, 6, 3, 2])
print(test)
test.sort()
print(test)