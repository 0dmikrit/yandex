num = [int(i) for i in input().split(' ')]
m_a, m_b = [], []
n, m = num
n1, m1 = n, m
while n > 0:
    m_a += [int(i) for i in input().split(' ')]
    n -= 1
while n1 > 0:
    m_b += [int(i) for i in input().split(' ')]
    n1 -= 1
m_sum = list(map(sum, [i for i in zip(m_a, m_b)]))
while len(m_sum) != 0:
    print(*[m_sum[i] for i in range(m)])
    m_sum = m_sum[m:]