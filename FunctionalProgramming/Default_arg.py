def total_cost(items,currency="inr"): #default arg
    total=sum(items.values())
    print(f'the sum is {total} in the {currency} currency')

cart={"apple":0.41,"banana":0.53,"orange":0.38}
total_cost(cart)