#solution
K = int(input())
room_list = list(map(int, input().split(' ')))
# print(room_list)
room_set = set(room_list)

# print(sum(room_set)*K)
# print(sum(room_list))

# print((sum(room_set)*K - sum(room_list))/(K-1))
cap_room_num = (sum(room_set)*K - sum(room_list))//(K-1)

print(cap_room_num)