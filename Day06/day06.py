with open("Day06/day06_input.txt") as f:
    buffer = f.read()

## PARTS ONE & TWO

parts = { 'Part one': 4,
          'Part two': 14}
            
for part, length in parts.items():
    for i in range(length, len(buffer)-1):
        segment = buffer[i-length:i]
        for letter in segment:
            if segment.count(letter) > 1:
                break
        else:
            print(part, " - Start of marker :", i)
            break