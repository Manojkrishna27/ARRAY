def buy_and_sell(arr):
    min_price=arr[0] 
    max_profit=0

    for i in arr:
        if i <min_price:
            min_price=i
        
        profit=i-min_price   # getting profit
        max_profit=max(max_profit,profit)  # comparing profit
    return max_profit         
arr=[7,1,5,3,6,4]
print(buy_and_sell(arr))
