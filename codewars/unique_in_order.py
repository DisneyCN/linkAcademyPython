def unique_in_order(iterable):
    result = []
    for item in range(0, len(iterable)):
        if len(iterable) != 1 :
            if iterable[item] != iterable[item-1]:
                result.append(iterable[item])
       
        elif len(iterable) ==  0:
            result = list('A') 
        else:   
            result = list(iterable)
    return result


    
print(unique_in_order(""))