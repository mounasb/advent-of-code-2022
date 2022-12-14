## PART ONE 

with open("Day06/day06_input.txt") as f:
    buffer = f.read()

for i in range(4, len(buffer)-1):
    segment = buffer[i-4:i+1]
    for letter in segment:
        if segment.count(letter) > 1:
            break
    else:
        print("Start of packet marker :", i)
        break


## PART TWO

for i in range(14, len(buffer)-1):
    segment = buffer[i-14:i]
    for letter in segment:
        if segment.count(letter) > 1:
            break
    else:
        print("Start of message marker :", i)
        break