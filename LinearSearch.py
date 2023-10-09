class LinearSearch(object):

    def __init__(self, contents=None):

        if contents is None:
            self.__contents = []

        else:
            self.__contents = contents

    def search(self, item):
        
        for index, listItem in enumerate(self.__contents):

            if item == listItem:
                print("Found item in list, list index: {}".format(index))
                return 

        print("Item: {} wasn't found in the list".format(item))


test = LinearSearch([4, 6, 1, 9, 6, 5, 6, 3, 2])

test.search(5)
test.search(-10000)