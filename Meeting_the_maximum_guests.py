#You are given arrival and departure times of the guests, you need to find the time to go to the party so that you can meet maximum people.

def maxguests(arrivals,departures):
    arrivals.sort()
    departures.sort()

    curr = res = 0
    # i is one because the first arrival time will be lesser than or equal to the first departure time
    i, j = 1, 0
    while (i < len(arrivals) and j < len(departures)):
        if arrivals[i] <= departures[j]:
            curr += 1
            i += 1
        
        else:
            curr -= 1
            j += 1

        res = max(res, curr)
    
    return res
