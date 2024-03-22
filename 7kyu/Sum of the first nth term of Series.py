def series_sum(n):
    summed =0
    for i in range(n):
        summed +=1/(3*i+1)
    return "{:.2f}".format(summed)