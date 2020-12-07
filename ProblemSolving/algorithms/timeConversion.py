def timeConversion(s):
    hh = s[0:2]
    XM = s[-2] + s[-1]

    if XM == 'PM':
        if hh != '12':
            hh = str(int(hh) + 12)
    
    if XM == 'AM':
        if hh == '12':
            hh = '00'

    return hh + s[2:8]
