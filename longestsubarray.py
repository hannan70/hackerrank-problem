def longestsubarray(arr):
    n = len(arr)
    ans = 0
    # O(n^2) is okay because of constraints.
    for i in range(n):
        w = []
        cnt = 0
        for j in range(i, n):
            if arr[j] in w:
                cnt += 1
                continue
            if len(w) == 0:
                w.append(arr[j])
            elif len(w) == 1:
                if abs(w[0] - arr[j]) > 1:
                    break
                else:
                    w.append(arr[j])
            else:
                break
            cnt += 1
        ans = max(ans, cnt)
    return ans