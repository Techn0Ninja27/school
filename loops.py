def loopMessage(message, count):
    for n in range(1, count, 1):
        print(message)



def userLoop():
    loopFinish = False
    while loopFinish == False:
        try:
            loopMessage(input("message to loop"), int(input("number of times to loop")))
        except:
            print("input error")
            continue
        else:
            loopFinish = True

def timestable():
    loopFinish = False
    while loopFinish == False:
        try:
            times = int(input("enter times table you want"))
            limit = int(input("enter upper limit"))
        except:
            print("input error")
            continue
        else:
            loopFinish = True
    for i in range(1, limit+1, 1):
        print(times, "*", i, "=", (times*i))
