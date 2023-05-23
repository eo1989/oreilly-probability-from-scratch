population = 100000.0

p_gamer_given_homicidal = .85
p_gamer = .19
p_homicidal = .00005

gamers_ct = population * p_gamer
homicidal_criminals_ct = population * p_homicidal

# gamers_and_homicidal_ct = homicidal_criminals_ct * p_gamer_given_homicidal
gamers_and_homicidal_ct = population * p_homicidal * p_gamer_given_homicidal

# p_homicidal_given_gamer = gamers_and_homicidal_ct / gamers_ct
p_homicidal_given_gamer = (population * p_homicidal * p_gamer_given_homicidal) / (population * p_gamer)

print(f"Probability of homicidal given gamer: {p_homicidal_given_gamer}")
