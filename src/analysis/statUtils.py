import pandas as pd
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

# pearson correlation test
def pearson_correlation(df, column1, column2):
    alpha = 0.05

    # print(df.head())
    # make spearman correlation
    correlation, p = stats.pearsonr(df[column1], df[column2])
    print("correlation: ", correlation, "p: ", p)
    if p < alpha:
        print("H0 rejected")
    else:
        print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent


## Chi-square test
# H0: type and operation are independent
# H1: type and operation are dependent
# df = dataframe
# columns = columns to analyse
def chi_square_test(df, column1, column2):
    alpha = 0.05
    # make chi-square test on type and operation columns of df
    #print(df.head())
    # make contingency table
    contingency_table = pd.crosstab(df[column1], df[column2])
    #print(contingency_table)
    # make chi-square test
    chi2, p, dof, expected = stats.chi2_contingency(contingency_table)
    print("chi2: ", chi2)
    print("p: ", p)
    print("dof: ", dof)
    print("expected: ", expected)
    if p < alpha:
      print("H0 rejected")
    else:
      print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent


# anova test
# assess the amount of variability between the group means in the context of the variation
# within groups to determine whether the mean differences are statistically significant
# H0: mean of all groups are equal
# H1: mean of at least one group is different
# df = dataframe
# columns = columns to analyse
def anova_test(df, column1, column2):
    alpha = 0.05
    # make anova f-test on type and operation columns of df
    print(df.head())
    # make anova f-test
    f, p = stats.f_oneway(df[column1], df[column2])
    print("f: ", f)
    print("p: ", p)
    if p < alpha:
      print("H0 rejected")
    else:
      print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that columns are independent

# spearmant correlation test
# numerical - numerical
# ordinal - numerical
# H0: there is no correlation between the two variables
# H1: there is a correlation between the two variables
# df = dataframe
# columns = columns to analyse
# NOTE: Spearman's correlation should not be used when there are ties in the ranking
def spearman_correlation(df, column1, column2):
    alpha = 0.05

    # print(df.head())
    # make spearman correlation
    correlation, p = stats.spearmanr(df[column1], df[column2])
    print("correlation: ", correlation)
    print("p: ", p)
    if p < alpha:
      print("H0 rejected")
    else:
      print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent


def plot_corr(df, features, methodName="spearman", annot=True, figSize=(5.0, 5.0)):
    # Create Correlation matrix
    corr_matrix = df[features].corr(method=methodName, numeric_only=True)   # Only plot numerical attributes

    # mask upper triangle
    mask = np.zeros_like(corr_matrix, dtype=bool)
    mask[np.triu_indices_from(mask)] = True

    # Create heatmap
    plt.figure(figsize=figSize)
    plt.title("Correlation Heatmap")
    sb.heatmap(corr_matrix, mask=mask, annot=annot, fmt=".2",
                   linecolor='black', linewidths=.5, square=True)
    plt.show()