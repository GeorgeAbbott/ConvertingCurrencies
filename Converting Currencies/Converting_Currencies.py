# This is to convert between currencies, to 
# get converted currencies for individual entries
# when only the Orig prices for each item, 
# and the Sett Total and Orig Total are known.

# To do so, call the PerformConversion with relevant parameters
# outputted to the console and returns in a list as well

def CalcEquiv(OrigTotal, SettTotal, ItemOrigValue):
    rate = SettTotal / OrigTotal
    return (ItemOrigValue * rate)

def PerformConversion(OrigTotal, SettTotal, *ItemOrigValues):
    print("NOTE: check OrigTotal matches sum of values: ", OrigTotal, "vs.", sum(ItemOrigValues))

    total = 0
    settValues = []
    itemSettValue = 0 # the converted value for each item
    for value in ItemOrigValues:
        itemSettValue = CalcEquiv(OrigTotal, SettTotal, value)
        print("Item of cost", value, "is", itemSettValue, "in sett currency")
        settValues.append(itemSettValue)
        total+=itemSettValue
    # will bug out due to floating point issues, but too minor to add episilon or anything like that
    # other than that, this functions as a check that the total value
    # of all the items actually matches the total, if not
    # there is likely a typo in adding values
    if total==SettTotal: print("ItemSett total matches SettTotal at", SettTotal)
    else: print("ItemSett total at", total, "whereas SettTotal at", SettTotal)

    return settValues

# Test Example
PerformConversion(1500, 11.43, 200, 200, 400, 540, 160)
