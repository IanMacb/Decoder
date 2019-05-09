import json
import random

file = open("flood.txt", "r")
data = file.read()
file.close()
x = json.loads(data)

file = open("floodOutput.txt", "w")

# for each REGION
for i in range(len(x["regions"])):
    y = x["regions"][i]
    file.write(str(y["regionID"]) + "\n")
    prevflood = 0
    # for each DAY per region
    for j in range(len(y["readings"])):
        z = y["readings"][j]
        prev = 0
        prev2 = 0
        peaks = []
        flooddanger = 0
        # loop through the reading data to identify peaks
        # and store them with their index in new list
        for k in range(len(z["reading"])):
            if prev > z["reading"][k] and prev >= prev2:
                peaks.append(k - 1)
                pool = 0
                # calculates each pool size and adds them together
                if len(peaks) > 1:
                    for l in range(1, peaks[-1] - peaks[-2]):
                        pool += z["reading"][peaks[-2]] - z["reading"][peaks[-2] + l]
                flooddanger += pool
            # remember the previous two for future peak identification
            prev2 = prev
            prev = z["reading"][k]

        delta = abs(flooddanger - prevflood)
        if delta > 1000 and prevflood != 0:
            #file.write(str(y["regionID"]) + "\t")
            file.write("\t" + z["date"] + "\t:\t" + z["readingID"] + "\t:\t" +
                       str(abs(flooddanger)) + "  \t*\t" + str(delta) + "\n")
        else:
            file.write("\t" + str(z["date"]) + "\t:\t" + str(z["readingID"]) + "\t:\t" + str(abs(flooddanger)) + "\n")
        prevflood = flooddanger

    file.write("\n")

file.close()
