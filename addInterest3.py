def addInterest(balances, rates):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rates)


def test():
    amounts = [1000,2200, 800, 360]
    rates = 0.05
    addInterest(amounts, rates)
    print(amounts)

test()
