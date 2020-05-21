class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "[" + str(x) + ", " + str(y) + ", " + str(z) + "]"

    def comparator(self, other):
        if self.x == other.x:
            if self.y == other.y:
                if self.z < other.z:
                    return -1
                elif self.z == other.z:
                    return 0
                else:
                    return 1
            elif self.y < other.y:
                return -1
            else: return 0
        else:
            if self.x < other.x:
                return -1
            else: return 1


x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if a + b + c != n]
print(result)