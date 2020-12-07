def birthdayCakeCandles(ar):
    highest = 0
    m = max(ar)
    for candle in ar:
        if candle == m:
            highest += 1
    
    return highest
