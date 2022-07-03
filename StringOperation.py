import logging as lg


class StringOperation:

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

    def count_Vowels(self, lis):
        i = 0
        try:
            vowels = ('a', 'e', 'i', 'o', 'u')
            while i < len(string):
                if string[i] in vowels:
                    print(string[i], ":", "it is a vowel")
                i += 1
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return i

    def lengthofString(self, string):
        count = 0
        try:
            while string[count:]:
                count = count + 1
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return count

    def concate(self, li):
        k = 0
        l2 = []
        flat = []
        string = ""
        try:
            while k < len(li):
                if type(li[k]) == list:
                    for j in range(len(li[k])):
                        string = string + str(li[k][j])
                        flat.append(li[k][j])
                else:
                    string = string + str(li[k])
                    flat.append(li[k])
                k += 1
        except IndexError as ie:
            logMyMessage("IndexError", 'app.log')
        except Exception as ex:
            logMyMessage("SomeOther Exception", 'app.log')

        return string

    def __str__(self):
        return "this class is for various manipulations on an input string"


strOps = StringOperation("String operation class")
print(strOps.lengthofString("KISHOR"))
li = [9, 3, [1, 2, 3, 4], ["ineuron", "data science"]]
ct = strOps.concate(li)
print(ct)