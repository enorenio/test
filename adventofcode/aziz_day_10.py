lst = '1113222113'
for i in range(0,40):
    output = ''
    prev_ch = ''
    c = 1
    units = []
    for ch in lst:
        if prev_ch != ch:
            if prev_ch:
                #units.append((c, prev_ch))
                output = output + str(c) + str(prev_ch)
            prev_ch = ch
            c = 1  
        else:
            c+=1
    else:
        #units.append((c, ch))
       output = output + str(c) + str(ch)
    lst = output
    #print(output)
        
print(len(lst))