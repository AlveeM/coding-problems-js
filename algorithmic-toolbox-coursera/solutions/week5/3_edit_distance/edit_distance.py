# Uses python3
def edit_distance(s, t):
    n = len(s)
    m = len(t)
    d = [[x for x in range(n + 1)] for y in range(m + 1)]
    
    for k in range(m + 1):
        d[k][0] = k

    for i in range(1, m+1):
        for j in range(1, n+1):
            insert_op = d[i-1][j] + 1
            delete_op = d[i][j-1] + 1
            match_op = d[i-1][j-1]
            mismatch_op = d[i-1][j-1] + 1
            if s[j-1] == t[i-1]:
                d[i][j] = min(insert_op, delete_op, match_op)
            else:
                d[i][j] = min(insert_op, delete_op, mismatch_op)

    return d[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
