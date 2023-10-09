class BubbleSort(object):


    def __init__(self, contents=None):

        if contents is None:
            self.__contents = []

        else:
            self.__contents = contents

    def __str__(self) -> str:
        return f"Contents: {self.__contents}"

    def sort(self):

        flag = True
        while(flag):
            # Iterate through all items
            swaps = 0
            for leftIndex in range(0, len(self.__contents) - 1):

                leftItem = self.__contents[leftIndex]
                
                rightIndex = leftIndex + 1 # Just 1 to the right of the left index
                rightItem = self.__contents[rightIndex]
                
                if rightItem < leftItem:
                    
                    # Make the right item equal to a temp item (it is saved when the right index is changed)
                    tempItem = self.__contents[rightIndex]
                    self.__contents[rightIndex] = leftItem # Make the right index equal the left item (swap pt.1)
                    self.__contents[leftIndex] = tempItem # Make the left index equal the temp item (swap pt.2)
                    swaps += 1 # Keep track of swaps


            # Keep repeating this process until no swaps are made
            if swaps == 0:
                flag = False

test = BubbleSort([4, 6, 1, 9, 6, 5, 6, 3, 2])
print(test)
test.sort()
print(test)