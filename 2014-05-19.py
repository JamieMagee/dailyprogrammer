from random import randrange


def simulate_rolls(n):
    rolls = [0] * 6
    for i in range(n):
        rolls[randrange(1, 7, 1) - 1] += 1
    print(str(n).ljust(10), ("{0:.2f}".format(rolls[0] / n * 100) + '%').ljust(6)
          , ("{0:.2f}".format(rolls[1] / n * 100) + '%').ljust(6)
          , ("{0:.2f}".format(rolls[2] / n * 100) + '%').ljust(6)
          , ("{0:.2f}".format(rolls[3] / n * 100) + '%').ljust(6)
          , ("{0:.2f}".format(rolls[4] / n * 100) + '%').ljust(6)
          , ("{0:.2f}".format(rolls[5] / n * 100) + '%').ljust(6))


rolls = [0] * 6
print('# of Rolls 1s     2s     3s     4s     5s     6s    ')
print('====================================================')
for i in [10 ** x for x in range(1, 7)]:
    simulate_rolls(i)