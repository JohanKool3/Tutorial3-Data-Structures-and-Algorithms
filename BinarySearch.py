class BinarySearch(object):

    def search(self, listIn, item):
        
        itemFound = False

        while len(listIn) > 1 and not itemFound:

            # Set middle index to be the middle of the contents
            listIn.sort()

            midPoint = len(listIn) // 2
            pivotItem = listIn[midPoint]

            # Check the middle index. If it is greater or lower

            if item > pivotItem:
                listIn = listIn[pivotItem:]

            elif item < pivotItem:
                listIn = listIn[:pivotItem]

            else:
                print("Item has been found!")
                itemFound = True
                return


            

        print("Item: {},  isn't in the list ".format(item))


        # If lower, discard all the values greater than the mid point

        # If greater, discard all the values lower than the mid point

        # Repeat until either the list is empty or the item is found


testList = [4, 6, 1, 9, 6, 5, 6, 3, 2]
test = BinarySearch()
test.search(testList, 10000)
# test.search(testList -10000)