import matplotlib.pyplot as plt

limit = int(input('The limit is: ')) + 2

def gen(x):
    sequence = [x]
    while (x != 1):
        if x % 2 == 0:
            x = x // 2
        else:
            x = 3 * x + 1
        sequence.append(x)
    return sequence

fig, ax = plt.subplots(figsize=(12, 6))
for i in range(1, limit):
    sequence = gen(i)
    ax.plot(sequence, 'o-', markersize=3,)

ax.set_title('3x+1 Sequence')
ax.set_xlabel('Iteration')
ax.set_ylabel('Value')
ax.legend(loc='best')
plt.show()
