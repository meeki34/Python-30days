"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

"""

# n = 6 

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# # r = 5
# # for i in range(r, 0, -1):
# #     for j in range(i, 0, -1):
# #         print(j, end=" ")
# #     print()

# start = 1
    
# for i in range(1, n + 1):
#     line = []
#     for j in range(i):
#             line.append(start)
#             start += 1
#     print(*line)

n = 4   # number of rows
num = 1

# Build triangular array
triangle = []
for i in range(1, n+1):
    row = []
    for j in range(i):
        row.append(num)
        num += 1
    triangle.append(row)
    print(*triangle[i-1])