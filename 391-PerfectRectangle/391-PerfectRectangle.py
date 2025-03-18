class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        x1 = y1 = 10 ** 5 + 1
        x2 = y2 = -10 ** 5 - 1
        area = 0
        s = set()
        for x, y, a, b in rectangles:
            x1, y1 = min(x1, x), min(y1, y)
            x2, y2 = max(x2, a), max(y2, b)
            area += (a - x) * (b - y)
            
            for i, j in itertools.product([x, a], [y, b]): s ^= {(i, j)}
        if (x1, y1) not in s or \
            (x1, y2) not in s or \
            (x2, y1) not in s or \
            (x2, y2) not in s or \
            len(s) != 4 \
            or (x2 - x1) * (y2 - y1) != area: return False
        return True