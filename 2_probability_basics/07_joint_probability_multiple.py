prob_failure = .10

three_fails_prob = 1.0 

for _ in range(0,3):
    three_fails_prob = three_fails_prob * prob_failure

print(f"Probability of 3 consecutive failures: {three_fails_prob}")
