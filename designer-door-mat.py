# Take user input
n, m = map(int, input().split(' '))
# n = 7
# m = 21

pattern_str = '.|.'
# '//' is int devision
n_half_int = (n + 1)//2

#Print design
for i in range(1, n_half_int):
    j = int((2*i)-1)
    print((pattern_str*j).center(m, '-'))

print('WELCOME'.center(m, '-'))

#Print design in reverse
for i in range(n_half_int-1, 0, -1):
    j = int((2*i)-1)
    print((pattern_str*j).center(m, '-'))