def fractional_knapsack(weights, values, capacity):
    res = 0
    for pair in sorted(zip(weights, values), key=lambda x: x[1] / x[0], reverse=True):
        if capacity <= 0:  # Capacity completed - Bag fully filled
            break
        if pair[0] > capacity:  # Current's weight with highest value/weight ratio Available Capacity
            res += int(capacity * (pair[1] / pair[0]))  # Completely fill the bag
            capacity = 0
        elif pair[0] <= capacity:  # Take the whole object
            res += pair[1]
            capacity -= pair[0]
    return res

if __name__ == "__main__":
    # User input for weights, values, and knapsack capacity
    weights = list(map(int, input("Enter weights separated by spaces: ").split()))
    values = list(map(int, input("Enter values separated by spaces: ").split()))
    knapsack_capacity = int(input("Enter knapsack capacity: "))

    result = fractional_knapsack(weights, values, knapsack_capacity)
    print("Maximum value that can be obtained:", result)