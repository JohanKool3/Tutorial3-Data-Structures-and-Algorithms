class InsertionSort(object):


    def __init__(self, contents=None):

        if contents is None:
            self.__contents = []

        else:
            self.__contents = contents

    def __str__(self) -> str:
        return f"Contents: {self.__contents}"
    
    def sort(self):

        """ NOTE: The way that the algorithm doesn't lose the current item is by keeping it saved in the 'item' variable that is situated in the for loop.
            This means that it can safely remove the initial reference (self.__contents[insertionPoint] from existence because it already has the value saved
            in the variable 'item')"""
        
        # Iterates through all of the items in the list

        # InsertionPoint is the initial place where the element is situated. As you work your way up the list, this will be equal to the index of the item
        for insertionPoint, item in enumerate(self.__contents):

            # If the insertion point is 0, you cannot minus 1 from it. Break out of the loop

            # If the item to the left of the current item - ([...,X, Y,....]), in this example X - is greater than the item (Y), you should shift the item that
            # is smaller down 1.
            previousItem = self.__contents[insertionPoint - 1]
            while insertionPoint > 0 and  previousItem > item:
                
                # the index that holds the current item is set to be the value of Y. 
                self.__contents[insertionPoint] = previousItem
                insertionPoint -= 1 # Shift over by 1 to repeat the process

                # Update previous item
                previousItem = self.__contents[insertionPoint - 1]

            # Now that the correct point has been found, insert the item
            self.__contents[insertionPoint] = item



test = InsertionSort([4, 6, 1, 9, 6, 5, 6, 3, 2])
print(test)
test.sort()
print(test)