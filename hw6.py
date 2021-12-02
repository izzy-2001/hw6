#HW 6 code

def OPT(i, memo, path, m, n, s, c):
    max = 0
    temp = 0

    for k in range (1,m):

        if i + k == n-1:
            max = s[n-1]
        elif i + k > n-1:
            max = 0
        else:
            if memo[i+k] > max:
                temp = memo[i+k]
            else:
                temp = s[i+k] + OPT(i+k, memo, path, m, n, s, c)-c
                memo[i+k] = temp

        if temp > max:
            max = temp
            path[n-i-1]=i+k

    return max


def find_path(n,m,c,s):

    memo = []
    path = []

    for i in range (n):
        memo.append(-1)
        path.append(-1)

    for j in range (n-1, 0, -1):
        memo[j] = OPT(j, memo, path, m, n, s, c)

    print("Maximum caloric surplus: ", memo[0])
    print("path: ", end = "")
    for i in range (n-1, 0, -1):
        if path[i] != -1:
            print(path[i], " ", end = "")
    print()


def main():
    s_1 = [0, 5, 19, 1, 1, 100]
    s_2 = [0, 1, 2, 3, 4, 5]
    s_3 = [0, 16, 5, 22, 1, 14, 30]
    s_4 = [0, 1]
    s_5 = [0, 1, 1, 1, 1, 1, 1, 1]
    all_s = [s_1, s_2, s_3, s_4, s_5]

    m_1 = 0
    m_2 = 2
    m_3 = 2
    m_4 = 1
    m_5 = 3

    all_m = [m_1, m_2, m_3, m_4, m_5]

    c = 5

    for i in range(5):
        find_path(len(all_s[i]), all_m[i], c, all_s[i])

main()
