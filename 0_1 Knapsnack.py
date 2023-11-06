def knapsack(weight, value, capacity):
    n = len(value)

    def knapsack_recursive(remaining_weight, items_checked):
        if items_checked < 0 or remaining_weight <= 0:
            return 0

        if weight[items_checked] > remaining_weight:
            return knapsack_recursive(remaining_weight, items_checked - 1)
        else:
            return max(value[items_checked] + knapsack_recursive(remaining_weight - weight[items_checked], items_checked - 1),
                       knapsack_recursive(remaining_weight, items_checked - 1))

    return knapsack_recursive(capacity, n - 1)

if __name__ == "__main__":
    # User input for values, weights, and knapsack capacity
    values = list(map(int, input("Enter values separated by spaces: ").split()))
    weights = list(map(int, input("Enter weights separated by spaces: ").split()))
    knapsack_capacity = int(input("Enter knapsack capacity: "))

    result = knapsack(weights, values, knapsack_capacity)
    print("Maximum value that can be obtained:", result)
