def mutate_v2(route: list[int], rng, ctx: dict) -> list[int]:
    n = len(route)
    if n <= 2:
        result = route[:]
        return result
    result = route[:]
    i, j = sorted(rng.choice(n, size=2, replace=False).astype(int).tolist())
    result[i], result[j] = result[j], result[i]
    return result
