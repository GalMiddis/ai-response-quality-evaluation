import os
import pandas as pd
import matplotlib.pyplot as plt


# Load evaluation dataset
DATA_FILE = "sample_ai_responses.csv"
OUTPUT_DIR = "images"

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE)


# Evaluation criteria
criteria = [
    "relevance",
    "instruction_following",
    "accuracy",
    "clarity",
    "completeness"
]


# Calculate average score for each criterion
average_scores = df[criteria].mean()


# Calculate overall score if it is not already present
if "overall_score" not in df.columns:
    df["overall_score"] = df[criteria].mean(axis=1)


# --------------------------------------------------
# Visualization 1: Average score by criterion
# --------------------------------------------------

plt.figure(figsize=(8, 5))

average_scores.plot(kind="bar")

plt.title("Average Evaluation Score by Criterion")
plt.xlabel("Evaluation criterion")
plt.ylabel("Average score (1–5)")
plt.ylim(0, 5)

plt.xticks(rotation=25, ha="right")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "average_scores.png"),
    dpi=200
)

plt.close()


# --------------------------------------------------
# Visualization 2: Review labels
# --------------------------------------------------

label_counts = df["issue_label"].value_counts()

plt.figure(figsize=(8, 5))

label_counts.plot(kind="bar")

plt.title("Observed Review Labels")
plt.xlabel("Issue category")
plt.ylabel("Number of responses")

plt.xticks(rotation=20, ha="right")
plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "review_labels.png"),
    dpi=200
)

plt.close()


# --------------------------------------------------
# Visualization 3: Overall score distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.hist(
    df["overall_score"],
    bins=10
)

plt.title("Distribution of Overall AI Response Quality Scores")
plt.xlabel("Overall score (1–5)")
plt.ylabel("Number of responses")

plt.tight_layout()

plt.savefig(
    os.path.join(OUTPUT_DIR, "overall_score_distribution.png"),
    dpi=200
)

plt.close()


# --------------------------------------------------
# Print summary statistics
# --------------------------------------------------

print("AI Response Evaluation Summary")
print("--------------------------------")

print(f"Number of responses: {len(df)}")

print("\nAverage scores:")
for criterion, score in average_scores.items():
    print(f"{criterion}: {score:.2f}")

print(f"\nAverage overall score: {df['overall_score'].mean():.2f}")

print("\nReview labels:")
print(label_counts)

print("\nEvaluation completed successfully.")
