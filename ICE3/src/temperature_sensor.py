def temperatures_processing(temp_list):

        if not temp_list:
            return "No input provided."

        valid_temperatures = []
        for temp in temp_list:
            if type(temp) not in [int, float]:
                return "Invalid input detected."
            if -50 <= temp <= 150:
                valid_temperatures.append(temp)
            else:
                return "Out-of-bound value detected."


        min_temp = min(valid_temperatures)
        max_temp = max(valid_temperatures)
        avg_temp = round(sum(valid_temperatures) / len(valid_temperatures), 2)

        return f"Min: {min_temp}°C, Max: {max_temp}°C, Avg: {avg_temp}°C"
def run_test_cases():
    test_cases = [
        [-50],  # Minimum boundary
        [150],  # Maximum boundary
        [-49, 149],  # Near-boundary values
        [-60, 20, 160],  # Mixed valid and invalid inputs
        [20, "abc", 30],  # Alphabetic characters in input
        [10, "@", -40],  # Special characters in input
        [2**31 - 1, -2**31],  # Very large input values
        [50, 50, 50],  # All inputs are the same
        []  # Empty list
    ]

    for i, case in enumerate(test_cases, 1):
        result = temperatures_processing(case)
        print(f"Test Case {i}: Input: {case}")
        print(f"Result: {result}")


if __name__ == "__main__":
    run_test_cases()
