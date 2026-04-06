nested = ((1,2,3), (4,5,6), (7,8,9))
print(nested[0])         # (1, 2, 3)
print(nested[1][2])       # 6
print(nested[-1][-2])     # 9

# Real-world: list of coordinate points
points = [(0,0), (3,4), (6,8)]
print(points[1])           # (3, 4)
print(points[1][0])        # 3  (x-coordinate)