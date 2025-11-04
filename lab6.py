from itertools import product

def implies(p, q): return (not p) or q

variables = ['R', 'W']
entailment = True

print("Truth Table Approach:")
for R, W in product([True, False], repeat=2):
    KB = implies(R, W) and R
    print(f"R={R}, W={W} | KB={KB}, Query={W}")
    if KB and not W:
        entailment = False
        print("--> Counterexample found")
        break

print("KB entails Query" if entailment else "KB does NOT entail Query")

print("\nResolution Method:")
print("KB: (¬R ∨ W), R\nQuery: W → negate to ¬W")
print("1. (~R ∨ W) + (~W) ⇒ ~R")
print("2. R + ~R ⇒ ⊥ (contradiction)")
print("=> KB entails Query ✅")
