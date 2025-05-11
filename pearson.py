# Data Exploration
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the datasets
mat_data = pd.read_csv('student-mat.csv', sep=';')
por_data = pd.read_csv('student-por.csv', sep=';')

# Displaying the first few rows of each dataset for an initial overview
mat_data.head()

por_data.head()

mat_data.info()
por_data.info()


mat_data.describe()
por_data.describe()


#Data Visualization
# Setting the aesthetic style of the plots
sns.set_style("whitegrid")

# Defining a function to create histograms and boxplots for specified columns
def plot_histograms_boxplots(data, columns, dataset_name):
    fig, axes = plt.subplots(len(columns), 2, figsize=(12, 4 * len(columns)))
    for i, col in enumerate(columns):
        # Histogram
        sns.histplot(data[col], kde=True, ax=axes[i, 0])
        axes[i, 0].set_title(f'Histogram of {col} in {dataset_name}')
        # Boxplot
        sns.boxplot(x=data[col], ax=axes[i, 1])
        axes[i, 1].set_title(f'Boxplot of {col} in {dataset_name}')
    plt.tight_layout()

# Columns of interest for both datasets
columns_of_interest = ['age', 'studytime', 'failures', 'G1', 'G2', 'G3']

# Plotting for Mathematics dataset
plot_histograms_boxplots(mat_data, columns_of_interest, 'Mathematics')

#Mathematics Dataset Visualizations
# Plotting for Portuguese dataset
plot_histograms_boxplots(por_data, columns_of_interest, 'Portuguese')

#Chi-Square Test for the Portuguese Language Dataset

from scipy.stats import chi2_contingency

# Defining a function to perform the Chi-Square Test and interpret results
def perform_chi_square_test(data, col1, col2):
    # Creating a contingency table
    contingency_table = pd.crosstab(data[col1], data[col2])

    # Performing the Chi-Square Test
    chi2, p, dof, expected = chi2_contingency(contingency_table)

    # Interpreting the result
    significant = p < 0.05  # 5% significance level
    return chi2, p, significant

# Aspects to test
aspects_to_test = {
    'Gender and Academic Performance': ('sex', 'G3'),
    'Internet Access and Grades': ('internet', 'G3'),
    'Family Educational Background and Performance': ('Medu', 'G3')
}

# Performing the tests for Mathematics dataset

por_chi_square_results = {aspect: perform_chi_square_test(por_data, *columns) for aspect, columns in aspects_to_test.items()}

por_chi_square_results

#Chi-Square Test for the Math Language

# Additional aspects to test in the Mathematics dataset
additional_aspects_to_test = {
    'School Support and Academic Performance': ('schoolsup', 'G3'),
    'Family Support and Grades': ('famsup', 'G3'),
    'Extra-Curricular Activities and Performance': ('activities', 'G3'),
    'Romantic Relationships and Academic Performance': ('romantic', 'G3'),
    'Health Status and Grades': ('health', 'G3')
}

# Performing the additional tests for Mathematics dataset
additional_mat_chi_square_results = {aspect: perform_chi_square_test(mat_data, *columns) for aspect, columns in additional_aspects_to_test.items()}

additional_mat_chi_square_results

'''
Final Insights
Actionable Insights
School Support: Significant positive impact on Mathematics grades suggests that strengthening school support services could enhance student performance.
Romantic Relationships The significant association with grades in Mathematics implies the need for guidance and counseling services that help students balance personal life with academic demands.
Statistical Significance:
The Chi-Square Tests revealed significant relationships in specific areas, notably in the influence of school support and romantic relationships on Mathematics grades, and the impact of family educational background on Portuguese language grades.
Recommendations
Enhance School Support: Schools should consider expanding their support services, focusing on academic counseling and tutoring, especially for Mathematics.
Counseling Services: Implement programs that offer guidance on managing personal relationships alongside academic responsibilities.
Parental Involvement: Encourage parental involvement, especially in households with a lower educational background, to positively influence students’ performance in Portuguese language.
Future Research
Longitudinal Studies: To better understand the long-term effects of these factors on academic performance.
Qualitative Research: Interviews and focus groups with students could provide deeper insights into the impact of personal and social factors on their academic life.
Comparative Studies Comparing these findings with other educational systems or age groups could offer a broader perspective on the influence of these factors on student achievement.
These insights and recommendations aim to contribute to the development of more effective educational strategies and support systems, ultimately enhancing student performance and well-being.
'''