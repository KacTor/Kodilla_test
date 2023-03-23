def get_fibonacci_number(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        fn = [0, 1,]
        for i in range(2, n+1):
            result = fn[i-1] + fn[i-2]
            fn.append(result)            
        return result
