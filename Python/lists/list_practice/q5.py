import random, time

number_steaks = 0

for exp_num in range(5):
    coin_list = []

    # generate 100 flips
    for i in range(100):
        coin_flip = random.randint(1, 2)
        if coin_flip == 1:
            coin_list.append('H')
        else:
            coin_list.append('T')

    print(coin_list)
    time.sleep(0.5)

    # check for streak
    for j in range(len(coin_list) - 5):
        if coin_list[j:j+6] == ['H']*6 or coin_list[j:j+6] == ['T']*6:
            number_steaks += 1
            break

print("Total streaks:", number_steaks)