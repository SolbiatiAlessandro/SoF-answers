def compute_turnover(first_account, second_account):
    turnover = 0

    for stock_name, stock_allocation in first_account.items():
        other_allocation = second_account.get(stock_name) 
        if other_allocation is not None:
            turnover += abs(stock_allocation - second_account[stock_name])
        else:
            turnover += stock_allocation

    for stock_name, stock_allocation in second_account.items():
        other_allocation = first_account.get(stock_name) 
        if other_allocation is None:
            turnover += stock_allocation

    return turnover
