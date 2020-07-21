def intinerary(llist, start):  
    itinerary_list = []
    itinerary_list.append(start)

    while len(llist) >= 1:
        current = None
        directions = {}

        for item in llist:
           
            if item[0] == start:
                directions[item[0]] = item[1]

        if len(directions) >= 1:
            current = min(directions.values())
            remove_tuple = (start, current)

        try:
            llist.remove(remove_tuple)
            itinerary_list.append(current)
            start = current
        except:
            return "not valid intinerary"

    return itinerary_list


print(intinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 
    'YUL'))

print(intinerary([('SFO', 'COM'), ('COM', 'YYZ')], 
    'COM'))

print(intinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 
    'A'))
