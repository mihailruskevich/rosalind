
def population_model(n, life_span):
    generations = {1: 1}
    amount = generations[1]
    for m in range(1, n + 1):
        generations = {g: c for g, c in generations.items() if m - g < life_span}
        adults = sum([c for g, c in generations.items() if m > g])
        amount = sum(generations.values())
        generations[m + 1] = adults
    return amount


months, life_months = 87, 18
rabbits_amount = population_model(months, life_months)
print(rabbits_amount)
