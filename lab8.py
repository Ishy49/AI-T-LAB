def bayes_theorem(prior_h, likelihood_e_given_h, likelihood_e_given_not_h):
    """
    Calculate posterior probability using Bayes Theorem
    
    Args:
        prior_h: P(H) - Prior probability of hypothesis
        likelihood_e_given_h: P(E|H) - Likelihood of evidence given hypothesis
        likelihood_e_given_not_h: P(E|¬H) - Likelihood of evidence given not hypothesis
    
    Returns:
        posterior_h_given_e: P(H|E) - Posterior probability
    """
    # Calculate total probability of evidence P(E)
    p_e = (likelihood_e_given_h * prior_h) + (likelihood_e_given_not_h * (1 - prior_h))
    
    # Apply Bayes Theorem
    posterior = (likelihood_e_given_h * prior_h) / p_e
    
    return posterior, p_e

def display_result(hypothesis, prior, likelihood_yes, likelihood_no, posterior):
    """
    Display results in a readable format
    """
    print("\n" + "=" * 60)
    print(f"Bayes Theorem Calculation: {hypothesis}")
    print("=" * 60)
    print(f"Prior Probability P(H):                  {prior:.4f}")
    print(f"Likelihood P(E|H):                       {likelihood_yes:.4f}")
    print(f"Likelihood P(E|¬H):                      {likelihood_no:.4f}")
    print(f"Prior Probability P(¬H):                 {1 - prior:.4f}")
    print("-" * 60)
    print(f"Posterior Probability P(H|E):            {posterior:.4f}")
    print(f"Confidence Level:                        {posterior * 100:.2f}%")
    print("=" * 60)
 # Example 1: Medical Diagnosis
print("\n" + "#" * 60)
print("EXAMPLE 1: Medical Diagnosis - Disease Detection")
print("#" * 60)

hypothesis_1 = "Patient has the disease"
prior_1 = 0.01  # 1% of population has disease
sensitivity = 0.95  # P(Test+|Disease) - True Positive Rate
specificity = 0.90  # P(Test-|¬Disease) - True Negative Rate
false_positive_rate = 1 - specificity  # P(Test+|¬Disease)

posterior_1, p_evidence_1 = bayes_theorem(prior_1, sensitivity, false_positive_rate)
display_result(hypothesis_1, prior_1, sensitivity, false_positive_rate, posterior_1)

print(f"\nInterpretation:")
print(f"Even though the test is positive, the actual probability the patient")
print(f"has the disease is only {posterior_1 * 100:.2f}% (not 95%!)")
print(f"This is due to the low prior probability of disease in the population.")


