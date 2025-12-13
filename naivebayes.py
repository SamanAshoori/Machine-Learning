# --- THE TRAINING DATA ---
# Format: [Color, Size, Taste, Label]
# Size Key: 1=Small, 2=Medium, 3=Big

training_data = [
    ['Green', 3, 'Sour', 'Apple'],
    ['Yellow', 3, 'Sweet', 'Apple'],
    ['Red', 1, 'Sweet', 'Grape'],
    ['Red', 1, 'Sweet', 'Grape'],
    ['Yellow', 3, 'Sour', 'Lemon'],
    ['Red', 3, 'Sweet', 'Apple'],
    ['Green', 2, 'Sour', 'Lime'],
    ['Orange', 3, 'Sweet', 'Orange'],
    ['Purple', 1, 'Sweet', 'Grape'],
]

header = ["Color", "Size", "Taste", "Label"]

# --- THE TEST DATA ---
# These are the "Unknown" fruits you need to classify.
# Format: [Color, Size, Taste] (Label is hidden/unknown)

testing_data = [
    ['Green', 3, 'Sweet'],    # A big, sweet, green fruit
    ['Purple', 1, 'Sour'],    # A small, sour, purple fruit
    ['Red', 3, 'Sour'],       # A big, sour, red fruit
]

print("Data loaded successfully!")
print(f"Training Instances: {len(training_data)}")
print(f"Testing Instances: {len(testing_data)}")

# --- YOUR MISSION ---
# Implement Naive Bayes from scratch.
#
# Steps:
# 1. Calculate Priors: P(Class) = count(Class) / total
# 2. Calculate Likelihoods: P(Feature|Class)
#    * Don't forget Laplace Smoothing: (count + 1) / (total_class + unique_values)
# 3. For each test row, calculate the Posterior Probability for every class.
#    * Posterior is proportional to: Prior * Likelihood1 * Likelihood2 ...
