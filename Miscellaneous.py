import logging as lg


class Miscellaneous:

    def __init__(self, string):
        self.string = string

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

    def getPrime(self, fr, to):
        '''This method returns a list of prime numbers in the range of input numbers both included'''
        li = []
        try:
            for i in range(fr, to + 1):
                if i > 1:
                    for j in range(2, i):
                        if (i % j) == 0:
                            break
                    else:
                        li.append(i)
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return li

    def removeAtPosition(self, l, pos):
        """This method is equivalent to pop.\n This method removes the element at the input position from the input list and returns the result list"""
        count = 0
        try:
            for i in l:
                if count < pos:
                    count += 1
                else:
                    break
            l.remove(l[count])
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return l

    def __str__(self):
        return "this class is for various manipulations on an input string"


mis = Miscellaneous("Number operation class")
print(mis.getPrime(1, 50))
print(mis.removeAtPosition([4, 5, 6], 1))