import logging as lg


class ListManipulation:

    def __init__(self, msg):
        self.msg = msg

    def logMyMessage(self, msg, filenm):
        try:
            lg.basicConfig(filename=filenm, level=lg.DEBUG, format="%(asctime)s %(levelname)s %(message)s")
            console_log = lg.StreamHandler()
            console_log.setLevel(lg.INFO)
            format = lg.Formatter("%(asctime)s %(levelname)s %(message)s")
            console_log.setFormatter(format)
            lg.getLogger('').addHandler(console_log)
            lg.debug("debug message:" + msg)
            lg.info("debug message:" + msg)
        except FileNotFoundError as e:
            # lg.error(e)
            logMyMessage("FilenoFoundError", 'app.log')
        except Exception as ex:
            logMyMessage("Some Other Exception", 'app.log')

    def extract_Entities(self, lis):
        try:
            for i in lis:
                if type(i) == list:
                    print(i)
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

    def filter_oddValues(self, lis):
        oddlist = []
        try:
            for i in lis:
                if type(i) == list:
                    for j in range(len(i)):
                        if type(i[j]) == int and i[j] % 2 != 0:
                            oddlist.append(i[j])
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')
        return oddlist

    def sum_numericValues(self, li):
        sum = 0
        try:
            for i in li:
                if type(i) == list:
                    for j in range(len(i)):
                        if type(i[j]) == int:
                            sum += int(i[j])
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')
        return sum

    def multiply_numericVals(self, li):
        multi = 1
        try:
            for i in li:
                if type(i) == list:
                    for j in range(len(i)):
                        if type(i[j]) == int:
                            multi *= int(i[j])
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return multi

    def create_FlatList(self, li):
        flat = []
        try:
            for i in li:
                if type(i) == list:
                    for j in range(len(i)):
                        if type(i[j]) == int:
                            flat.append(i[j])
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return flat

    def __str__(self):
        return "this class is for various manipulations on the list entities"


myListManipulation = ListManipulation("list manipulation class")
li = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
      {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science"]]
sum = myListManipulation.multiply_numericVals(li)
print(myListManipulation.create_FlatList(li))
print(sum)