import pandas as pd

from scipy.stats import chi2_contingency

## Chi-square test
# H0: type and operation are independent
# H1: type and operation are dependent
# df = dataframe
# columns = columns to analyse
def chi_square_test(df, columns):
    # open
    alpha = 0.05
    # make chi-square test on type and operation columns of df
    print(df[columns].head())
    # make contingency table
    contingency_table = pd.crosstab(df["type"], df["operation"])
    print(contingency_table)
    # make chi-square test
    chi2, p, dof, expected = chi2_contingency(contingency_table)
    print("chi2: ", chi2)
    print("p: ", p)
    print("dof: ", dof)
    print("expected: ", expected)
    if p < alpha:
      print("H0 rejected")
    else:
      print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent

# anova f-test
# H0: mean of all groups are equal
# H1: mean of at least one group is different
# df = dataframe
# columns = columns to analyse
def anova_f_test(df, columns):
    # open
    alpha = 0.05
    # make anova f-test on type and operation columns of df
    print(df[columns].head())
    # make anova f-test
    f, p = stats.f_oneway(df["type"], df["operation"])
    print("f: ", f)
    print("p: ", p)
    if p < alpha:
      print("H0 rejected")
    else:
      print("H0 accepted")
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent


chi_square_test()