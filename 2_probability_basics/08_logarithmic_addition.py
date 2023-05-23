from math import log, exp 

prob_failure = .10
three_fails_prob = 0.0

for _ in range(0,3):
    # Perform logarithmic addition instead of multiplication
    three_fails_prob = three_fails_prob + log(prob_failure)

# Use exp() to convert back!
three_fails_prob = exp(three_fails_prob)

print(f"Probability of 3 consecutive failures: {three_fails_prob}")
