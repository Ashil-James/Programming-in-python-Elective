t = (1, 2, 2, 3, 2, 4)
t.count(2)    # 3
t.count(9)    # 0  (no error)

coords = (1,2,1,3,1)
coords.count(1)  # 3


t = ("a", "b", "c", "b")
t.index("b")        # 1  (first match)
t.index("b", 2)     # 3  (search from 2)
t.index("c", 0, 3)  # 2  (search [0:3])
# Raises ValueError if not found
