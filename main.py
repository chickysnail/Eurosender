import time, datetime
import balance, mail


def sendCondition(b):
    send = False
    with open("firstTime.txt", "r") as isFirst:
        first = int(isFirst.read(1))

    if b < 600 or (b < 10000 and first):
        with open("firstTime.txt", "w") as f:
            f.write("0")
        send = True
    elif b > 10000 and not first:
        with open("firstTime.txt", "w") as f:
            f.write("1")
    return send


def checkBalance(debug=False):
    creditBalance = balance.getBalance()

    if debug:
        newB = float(input("New balance: "))
        print(f"balance {creditBalance} -> {newB}")
        creditBalance = newB

    print("Balance checked at {}".format(datetime.datetime.now()))

    if sendCondition(creditBalance):
        mail.send(creditBalance)
        print("Condition is met, notification is sent at {}".format(datetime.datetime.now()))
    else:
        print("Condition not met, balance not sent. Time: {}".format(datetime.datetime.now()))


if __name__ == "__main__":
    debug = False
    checkBalance(debug)