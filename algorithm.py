def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    result = []
    pattern_hash = 0
    current_hash = 0
    h = pow(base, m - 1, mod)
    step_data = []

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % mod
        current_hash = (base * current_hash + ord(text[i])) % mod

    for i in range(n - m + 1):
        match = False
        if pattern_hash == current_hash:
            if text[i:i + m] == pattern:
                result.append(i)
                match = True
        step_data.append({
            'index': i,
            'current_hash': current_hash,
            'match': match,
            'window': text[i:i + m]
        })
        if i < n - m:
            current_hash = (
                base * (current_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % mod
            if current_hash < 0:
                current_hash += mod

    return result, step_data
