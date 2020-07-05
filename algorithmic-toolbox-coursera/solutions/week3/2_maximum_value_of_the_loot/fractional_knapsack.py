# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    sorted_weights_by_val_per_weight = sorted([(x[0] / x[1], x[1]) for x in zip(values, weights)], reverse=True)
    sorted_val_per_weight = [x[0] for x in sorted_weights_by_val_per_weight]
    sorted_weights = [x[1] for x in sorted_weights_by_val_per_weight]
    
    val = 0
    selected_weight = 0
    for i in range(len(weights)):
        if capacity == 0:
            return val
        selected_weight = min(sorted_weights[i], capacity)
        val = val + (selected_weight * sorted_val_per_weight[i])
        # sorted_weights[i] = sorted_weights[i] - selected_weight
        capacity = capacity - selected_weight

    return val

# n = 3
# capacity = 50
# weights = [20, 50, 30]
# values = [60, 100, 120]
# wv = sorted([(x[0] / x[1], x[1]) for x in zip(values, weights)], reverse=True)
# wv -> [(4.0, 120), (3.0, 20), (2.0, 50)]
# sv = [x[0] for x in wv]
# sv -> [4.0, 3.0, 2.0]
# sw = [x[1] for x in wv]
# sw -> [120, 20, 50]

# result = get_optimal_value(capacity, weights, values)

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
