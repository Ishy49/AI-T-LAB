from functools import reduce

def combine(cf1, cf2):
    if cf1 > 0 and cf2 > 0: return cf1 + cf2 - cf1 * cf2
    if cf1 < 0 and cf2 < 0: return cf1 + cf2 + cf1 * cf2
    return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))

def calc_cf(cfs):
    print(f"Starting CF: {cfs[0]}")
    return reduce(lambda a, b: (print(f"Combine {a:.2f} & {b:.2f} → ", end=""), 
                                combine(a, b))[1], cfs[1:], cfs[0])

# Example 1: Flu Diagnosis
print("="*45)
print("Flu Diagnosis using Certainty Factors")
print("="*45)
cf_values = [0.7, 0.6, 0.5]
final = calc_cf(cf_values)
print(f"\nFinal CF for Flu: {final:.4f} ({final*100:.1f}%)")

# Example 2: Mixed Evidence
print("\n\nMixed Evidence Example")
print("="*45)
cf_mixed = [0.8, -0.3, 0.5]
final_mixed = calc_cf(cf_mixed)
print(f"\nFinal Combined CF: {final_mixed:.4f}")
