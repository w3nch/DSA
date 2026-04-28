import random

target = [4821, 1940, 7722]

for seed in range(100000):
    random.seed(seed)

    ok = True
    for t in target:
        if random.randint(0, 9999) != t:
            ok = False
            break

    if ok:
        print("Seed found:", seed)
        break
