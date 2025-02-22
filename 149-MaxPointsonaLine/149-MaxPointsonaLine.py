for i, p1 in enumerate(points[:-1]):
    slopes = defaultdict(int)
    for j, p2 in enumerate(points[i+1:]):
        slope = find_slope(p1, p2)
        slopes[slope] += 1
    ans = max(max(slopes.values()), ans)