def sockMerchant(n, ar):
    pairs = 0
    cache = {}

    for el in ar:
        cache[el] = cache.get(el, 0) + 1
        if cache[el] % 2 == 0:
            pairs += 1
    
    return pairs