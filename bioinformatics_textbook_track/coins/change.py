from utils.common import int_list


def count_coins(x, coins):
    if len(coins) == 0:
        return 0
    val = coins[-1]
    quotient = x // val
    if quotient > 1 or quotient == 0:
        return count_coins(x - val * quotient, coins[:-1]) + quotient
    elif quotient == 1 and x != val:
        return min(count_coins(x - val, coins[:-1]) + 1, count_coins(x, coins[:-1]))
    else:
        return 1


with open('coins.txt') as file:
    amount, coin_list = file.read().split()
    amount, coin_list = int(amount), int_list(coin_list, sep=',')
    res = count_coins(amount, coin_list)
    print(res)
