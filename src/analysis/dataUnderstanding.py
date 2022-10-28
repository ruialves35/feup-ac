import pandas as pd
import scipy.stats as stats

CLEAN_PATH = "../../assets/clean/"

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

# anova f-test
# H0: mean of all groups are equal
# H1: mean of at least one group is different
# df = dataframe
# columns = columns to analyse
def anova_f_test(df, column1, column2):
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
    # p-value is less than 0.05, so we reject H0 and conclude that type and operation are dependent

# spearmant correlation test
# numerical - numerical
# ordinal - numerical
# H0: there is no correlation between the two variables
# H1: there is a correlation between the two variables
# df = dataframe
# columns = columns to analyse
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


#df = pd.read_csv(CLEAN_PATH + "trans_dev.csv")
df = pd.read_csv(CLEAN_PATH + "district.csv")
print("Doing chi-square test...")
#chi_square_test(df)
print("\n-----------------\n")
print("Doing anova f-test...")
#anova_f_test(df)
print("\n-----------------\n")
print("Doing spearman correlation test...")
spearman_correlation(df, "municip499", "municip500_1999")