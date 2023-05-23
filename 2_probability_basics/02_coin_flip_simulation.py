import random

heads = sum(1 for _ in range(0,100) if random.uniform(0,1) <= .6)
print(f"# HEADS: {heads}/100")
