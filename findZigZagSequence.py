





def zigZag(arr, n):

    flag = True
    for i in range(n-1):
        # "<" relation expected
        if flag is True:
            # If we have a situation like A > B > C,
            # we get A > C < B
            # by swapping B and C
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
            # ">" relation expected
        else:
            # If we have a situation like A < B < C,
            # we get A < C > B
            # by swapping B and C
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        flag = bool(1 - flag)


    print(arr)


# Driver program
arr = [4, 3, 7, 8, 6, 2, 1]
n = len(arr)
zigZag(arr, n)

# This code is contributed by Pratik Chhajer
# This code was improved by Hardik Jain
