class Solution:
    def frequencySort(self, s: str) -> str:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1

        counts_sorted = sorted(counts.items(), key=lambda c: c[1], reverse=True)
        result = "".join(c[0]*c[1] for c in counts_sorted)

        return result
