# Dice Roll Probability Distribution

This Python program calculates probability distribution when rolling M number of N-sided dice K times.

## Tasks

1. **Implementing the Dice Roll Function**: Simulates rolling M number of N-sided dice once and returns the sums. 
2. **Simulating Multiple Rolls**: Simulates rolling M number of N-sided dice K times and records results. 
3. **Calculating Probability Distribution**: Calculates probability of each possible sum when M number of N-sided dice are rolled. 
4. **User Interface**: Allows user to input values of N, M, and K, and displays probability distribution.

## Usage

Run the script and follow prompts to input number of sides on die (N), number of dice to roll (M), and number of times to roll the dice (K). 
The probability distribution of the sums will be displayed.

```bash
python3 prob-calculator.py
```

## Example

- Please enter the number of sides on each die (N): 6 
- Please enter the number of dice to roll (M): 2 
- Please enter the number of times to roll the dice (K): 1000
  
Probability Distribution:

- Sum: 2, Probability: 0.0270 
- Sum: 3, Probability: 0.0540 
- Sum: 4, Probability: 0.0810 
- Sum: 5, Probability: 0.1080 
- Sum: 6, Probability: 0.1350 
- Sum: 7, Probability: 0.1620 
- Sum: 8, Probability: 0.1350 
- Sum: 9, Probability: 0.1080 
- Sum: 10, Probability: 0.0810 
- Sum: 11, Probability: 0.0540 
- Sum: 12, Probability: 0.0270

## Test Cases

Test cases ensure functionality works correctly. Tests cover normal and edge cases, such as a die with one side, rolling zero dice, and rolling multiple dice with one side.

## Running Tests

To run the tests, execute the script. Tests will run first, then user will be prompted for input.



