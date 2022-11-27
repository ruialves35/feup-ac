import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

SHOW_GRAPH = False

SUBMISSION_PATH = "../assets/results/submission.csv"
RESULTS_PATH = "../assets/complete_clean/loan_dev.csv"

submission_pd = pd.read_csv(SUBMISSION_PATH)
results_pd = pd.read_csv(RESULTS_PATH)
mix_pd = pd.merge(submission_pd, results_pd, left_on='Id', right_on='loan_id', how='inner')

submission_scores = mix_pd["Predicted"].values.tolist()
results = mix_pd["paid"].values.tolist()

# calculate confusion matrix
tp = 0
tn = 0
fp = 0
fn = 0
for i in range(len(results)):
    if results[i] == 1:
        if submission_scores[i] < 0.5:
            tn += 1
        else:
            fp += 1
    else:
        if submission_scores[i] < 0.5:
            fn += 1
        else:
            tp += 1

print("True Positive: ", tp)
print("True Negative: ", tn)
print("False Positive: ", fp)
print("False Negative: ", fn)
print("False negative rate", (fn / (fn + tn)) * 100, "%")
print("False positive rate", (fp / (fp + tp)) * 100, "%")

fpr, tpr, thresholds = roc_curve(results, submission_scores, pos_label=0)
auc = auc(fpr, tpr)

print(f"Submission score: {auc}% (~{round(auc, 2)}%)")

if SHOW_GRAPH:
    plt.figure()
    plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.show()
