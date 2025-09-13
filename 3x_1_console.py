limit = float(input('The limit is: '))
inf  = float('inf')

def gen(x):
    sequence = [x]
    while (x != 1):
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    return sequence
i = 1
with open('3x+1_sequence.txt', 'w') as f:
   while i < limit:
        sequence = gen(i)
        print(f"The 3x+1 sequence for {i}: {sequence}")
        f.write(f"The 3x+1 sequence for {i}: {sequence}\n")
        i += 1
