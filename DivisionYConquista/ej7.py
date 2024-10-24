def puntos_mas_cercanos(puntos):
    def distancia(p1, p2):
        return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

    def closest_pair_rec(Px, Py):
        n = len(Px)

        if n <= 3:
            min_pair = None
            min_dist = float('inf')
            for i in range(n):
                for j in range(i + 1, n):
                    d = distancia(Px[i], Px[j])
                    if d < min_dist:
                        min_dist = d
                        min_pair = (Px[i], Px[j])
            return min_pair, min_dist

        mid = n // 2
        Qx = Px[:mid]
        Rx = Px[mid:]
        midpoint = Px[mid][0]

        Qy = list(filter(lambda p: p[0] <= midpoint, Py))
        Ry = list(filter(lambda p: p[0] > midpoint, Py))

        (q0, q1), dist_q = closest_pair_rec(Qx, Qy)
        (r0, r1), dist_r = closest_pair_rec(Rx, Ry)

        delta = min(dist_q, dist_r)

        S = [p for p in Py if abs(p[0] - midpoint) < delta]
        min_dist = delta
        min_pair = None
        for i in range(len(S)):
            for j in range(i + 1, min(i + 16, len(S))):
                d = distancia(S[i], S[j])
                if d < min_dist:
                    min_dist = d
                    min_pair = (S[i], S[j])

        if min_pair:
            return min_pair, min_dist
        elif dist_q < dist_r:
            return (q0, q1), dist_q
        else:
            return (r0, r1), dist_r

    Px = sorted(puntos, key=lambda p: p[0])
    Py = sorted(puntos, key=lambda p: p[1])

    return closest_pair_rec(Px, Py)[0]