import json


def convert():
    file = open("ppb.bin.log.txt", "r")
    data = file.read()
    data = data.split()
    decode = ""
    for i in data:
        decode = decode + chr(int(i, 2))
    file.close()
    file = open("ppbOutput.txt", "w")
    file.write(decode)
    file.close()


def read():
    file = open("ppbOutput.txt", "r")
    data = file.read()
    x = json.loads(data)
    dateSum = {}
    # loop through dates
    for i in range(len(x)):
        print(str(x[i]["date"]))
        timeSum = []
        # loop through times
        for j in range(len(x[i]["readings"])):
            print("\t", x[i]["readings"][j]["time"], x[i]["readings"][j]["id"])
            sum = 0
            # loop through contaminants
            for k in x[i]["readings"][j]["contaminants"]:
                print("\t\t", k, "\t", x[i]["readings"][j]["contaminants"][k])
                sum += x[i]["readings"][j]["contaminants"][k]
            dateSum[str(x[i]["date"]) + " " + str(x[i]["readings"][j]["time"]) + " id:" + str(
                x[i]["readings"][j]["id"])] = sum

    print()
    total = 0
    count = 0
    for i in dateSum:
        count += 1
        total += dateSum[i]
        if dateSum[i] > 1.2 * total / count:
            print("CODE:", dateSum[i], i)
    file.close()


read()
