import random
from collections import Counter

# Single roll
def roll_dice_once(M, N):
    return sum(random.randint(1, N) for _ in range(M))

# Multiple rolls
def simulate_rolls(M, N, K):
    results = [roll_dice_once(M, N) for _ in range(K)]
    return results

def calculate_probability_distribution(results):
    count = Counter(results)
    total_rolls = sum(count.values())
    probability_distribution = {sum_: count[sum_] / total_rolls for sum_ in count}
    return probability_distribution

def main():
    print("Please enter number of sides on each die (N):")
    N = int(input().strip())
    
    print("Please enter number of dice to roll (M):")
    M = int(input().strip())
    
    print("Please enter number of times to roll dice (K):")
    K = int(input().strip())
    
    results = simulate_rolls(M, N, K)
    probability_distribution = calculate_probability_distribution(results)
    
    print("Probability Distribution:")
    for sum_, probability in sorted(probability_distribution.items()):
        print(f"Sum: {sum_}, Probability: {probability:.4f}")

# Test cases
def test_roll_dice_once():
    assert 1 <= roll_dice_once(1, 6) <= 6
    assert 2 <= roll_dice_once(2, 6) <= 12
    assert 3 <= roll_dice_once(3, 6) <= 18

def test_simulate_rolls():
    results = simulate_rolls(2, 6, 1000)
    assert len(results) == 1000
    assert all(2 <= result <= 12 for result in results)

def test_calculate_probability_distribution():
    results = [2, 3, 3, 4, 4, 4, 5, 5, 6]
    distribution = calculate_probability_distribution(results)
    expected_distribution = {2: 1/9, 3: 2/9, 4: 3/9, 5: 2/9, 6: 1/9}
    assert distribution == expected_distribution

# Edge cases
def test_edge_cases():
    results = simulate_rolls(1, 1, 1000) # 1 die with 1 side (expected 1)
    distribution = calculate_probability_distribution(results)
    assert distribution == {1: 1.0}

    results = simulate_rolls(0, 6, 1000) # 0 dice (expected 0)
    distribution = calculate_probability_distribution(results)
    assert distribution == {0: 1.0}

    results = simulate_rolls(3, 1, 1000) # 3 dice with 1 side (expected 3)
    distribution = calculate_probability_distribution(results)
    assert distribution == {3: 1.0}

def run_tests():
    test_roll_dice_once()
    test_simulate_rolls()
    test_calculate_probability_distribution()
    test_edge_cases()
    print("All tests passed!")

if __name__ == "__main__":
    run_tests()
    main()
