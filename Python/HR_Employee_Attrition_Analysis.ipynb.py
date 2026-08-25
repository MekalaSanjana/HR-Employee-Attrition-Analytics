#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.listdir()


# In[2]:


os.listdir('Downloads')


# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[6]:


df = pd.read_excel('Downloads/HR_Employee_Attrition_Analysis.xlsx.xlsx')


# In[7]:


df.head()


# In[8]:


df = pd.read_csv('Downloads/WA_Fn-UseC_-HR-Employee-Attrition.csv')


# In[9]:


df.head()


# In[10]:


df.shape


# In[11]:


df.columns


# In[12]:


df.info()


# In[13]:


df.describe()


# In[14]:


df.isnull().sum()


# In[15]:


df['Attrition'].value_counts()


# In[16]:


attrition_rate = df['Attrition'].value_counts(normalize=True) * 100

attrition_rate


# In[17]:


import matplotlib.pyplot as plt


# In[18]:


df['Attrition'].value_counts().plot(
    kind='bar',
    xlabel='Attrition',
    ylabel='Number of Employees',
    title='Employee Attrition Distribution'
)

plt.show()


# In[19]:


department_attrition = pd.crosstab(
    df['Department'],
    df['Attrition']
)

department_attrition


# In[20]:


department_attrition_rate = pd.crosstab(
    df['Department'],
    df['Attrition'],
    normalize='index'
) * 100

department_attrition_rate


# In[21]:


department_attrition_rate.plot(
    kind='bar',
    figsize=(8, 5),
    xlabel='Department',
    ylabel='Percentage',
    title='Department-wise Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.show()


# In[22]:


gender_attrition = pd.crosstab(
    df['Gender'],
    df['Attrition']
)

gender_attrition


# In[23]:


gender_attrition_rate = pd.crosstab(
    df['Gender'],
    df['Attrition'],
    normalize='index'
) * 100

gender_attrition_rate


# In[24]:


gender_attrition_rate.plot(
    kind='bar',
    figsize=(7, 5),
    xlabel='Gender',
    ylabel='Percentage',
    title='Gender-wise Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.show()


# In[25]:


jobrole_attrition = pd.crosstab(
    df['JobRole'],
    df['Attrition']
)

jobrole_attrition


# In[26]:


jobrole_attrition_rate = pd.crosstab(
    df['JobRole'],
    df['Attrition'],
    normalize='index'
) * 100

jobrole_attrition_rate


# In[27]:


jobrole_attrition_rate.plot(
    kind='bar',
    figsize=(12, 6),
    xlabel='Job Role',
    ylabel='Percentage',
    title='Job Role-wise Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[28]:


df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=[0, 25, 35, 45, 55, 100],
    labels=['18-25', '26-35', '36-45', '46-55', '56+']
)

df[['Age', 'AgeGroup']].head()


# In[29]:


age_attrition = pd.crosstab(
    df['AgeGroup'],
    df['Attrition']
)

age_attrition


# In[30]:


age_attrition_rate = pd.crosstab(
    df['AgeGroup'],
    df['Attrition'],
    normalize='index'
) * 100

age_attrition_rate


# In[31]:


age_attrition_rate.plot(
    kind='bar',
    figsize=(9, 5),
    xlabel='Age Group',
    ylabel='Percentage',
    title='Age Group-wise Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[32]:


income_attrition = df.groupby('Attrition')['MonthlyIncome'].mean()

income_attrition


# In[33]:


df.groupby('Attrition')['MonthlyIncome'].describe()


# In[34]:


income_attrition.plot(
    kind='bar',
    figsize=(7, 5),
    xlabel='Attrition',
    ylabel='Average Monthly Income',
    title='Average Monthly Income by Attrition'
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[35]:


overtime_attrition = pd.crosstab(
    df['OverTime'],
    df['Attrition']
)

overtime_attrition


# In[36]:


overtime_attrition_rate = pd.crosstab(
    df['OverTime'],
    df['Attrition'],
    normalize='index'
) * 100

overtime_attrition_rate


# In[37]:


overtime_attrition_rate.plot(
    kind='bar',
    figsize=(7, 5),
    xlabel='OverTime',
    ylabel='Percentage',
    title='OverTime vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[38]:


years_company_attrition = df.groupby('Attrition')['YearsAtCompany'].mean()

years_company_attrition


# In[39]:


df.groupby('Attrition')['YearsAtCompany'].describe()


# In[40]:


years_company_attrition.plot(
    kind='bar',
    figsize=(7, 5),
    xlabel='Attrition',
    ylabel='Average Years at Company',
    title='Average Years at Company by Attrition'
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[41]:


job_satisfaction_attrition = pd.crosstab(
    df['JobSatisfaction'],
    df['Attrition']
)

job_satisfaction_attrition


# In[42]:


job_satisfaction_attrition_rate = pd.crosstab(
    df['JobSatisfaction'],
    df['Attrition'],
    normalize='index'
) * 100

job_satisfaction_attrition_rate


# In[43]:


job_satisfaction_attrition_rate.plot(
    kind='bar',
    figsize=(8, 5),
    xlabel='Job Satisfaction Level',
    ylabel='Percentage',
    title='Job Satisfaction vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[44]:


worklife_attrition = pd.crosstab(
    df['WorkLifeBalance'],
    df['Attrition']
)

worklife_attrition


# In[45]:


worklife_attrition_rate = pd.crosstab(
    df['WorkLifeBalance'],
    df['Attrition'],
    normalize='index'
) * 100

worklife_attrition_rate


# In[46]:


worklife_attrition_rate.plot(
    kind='bar',
    figsize=(8, 5),
    xlabel='Work-Life Balance Level',
    ylabel='Percentage',
    title='Work-Life Balance vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[47]:


distance_attrition = df.groupby('Attrition')['DistanceFromHome'].mean()

distance_attrition


# In[48]:


df.groupby('Attrition')['DistanceFromHome'].describe()


# In[49]:


distance_attrition.plot(
    kind='bar',
    figsize=(7, 5),
    xlabel='Attrition',
    ylabel='Average Distance From Home',
    title='Average Distance From Home by Attrition'
)

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[50]:


marital_attrition = pd.crosstab(
    df['MaritalStatus'],
    df['Attrition']
)

marital_attrition


# In[51]:


marital_attrition_rate = pd.crosstab(
    df['MaritalStatus'],
    df['Attrition'],
    normalize='index'
) * 100

marital_attrition_rate


# In[52]:


marital_attrition_rate.plot(
    kind='bar',
    figsize=(8, 5),
    xlabel='Marital Status',
    ylabel='Percentage',
    title='Marital Status vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[53]:


business_travel_attrition = pd.crosstab(
    df['BusinessTravel'],
    df['Attrition']
)

business_travel_attrition


# In[54]:


business_travel_attrition_rate = pd.crosstab(
    df['BusinessTravel'],
    df['Attrition'],
    normalize='index'
) * 100

business_travel_attrition_rate


# In[55]:


business_travel_attrition_rate.plot(
    kind='bar',
    figsize=(9, 5),
    xlabel='Business Travel',
    ylabel='Percentage',
    title='Business Travel vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[56]:


education_attrition = pd.crosstab(
    df['EducationField'],
    df['Attrition']
)

education_attrition


# In[57]:


education_attrition_rate = pd.crosstab(
    df['EducationField'],
    df['Attrition'],
    normalize='index'
) * 100

education_attrition_rate


# In[58]:


education_attrition_rate.plot(
    kind='bar',
    figsize=(10, 5),
    xlabel='Education Field',
    ylabel='Percentage',
    title='Education Field vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# In[59]:


joblevel_attrition = pd.crosstab(
    df['JobLevel'],
    df['Attrition']
)

joblevel_attrition


# In[60]:


joblevel_attrition_rate = pd.crosstab(
    df['JobLevel'],
    df['Attrition'],
    normalize='index'
) * 100

joblevel_attrition_rate


# In[61]:


joblevel_attrition_rate.plot(
    kind='bar',
    figsize=(8, 5),
    xlabel='Job Level',
    ylabel='Percentage',
    title='Job Level vs Attrition Rate'
)

plt.legend(title='Attrition')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[62]:


print("===== HR EMPLOYEE ATTRITION ANALYSIS: KEY INSIGHTS =====")

print("\n1. Overall Attrition Rate:")
print(f"{(df['Attrition'] == 'Yes').mean() * 100:.2f}%")

print("\n2. Department with Highest Attrition Rate:")
dept_rate = (
    df.groupby('Department')['Attrition']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)
print(dept_rate)

print("\n3. Job Role Attrition Rate:")
jobrole_rate = (
    df.groupby('JobRole')['Attrition']
    .apply(lambda x: (x == 'Yes').mean() * 100)
    .sort_values(ascending=False)
)
print(jobrole_rate)

print("\n4. Attrition Rate by OverTime:")
overtime_rate = (
    df.groupby('OverTime')['Attrition']
    .apply(lambda x: (x == 'Yes').mean() * 100)
)
print(overtime_rate)

print("\n5. Average Monthly Income by Attrition:")
print(df.groupby('Attrition')['MonthlyIncome'].mean())

print("\n6. Average Years at Company by Attrition:")
print(df.groupby('Attrition')['YearsAtCompany'].mean())

print("\n7. Average Distance From Home by Attrition:")
print(df.groupby('Attrition')['DistanceFromHome'].mean())

print("\n===== ANALYSIS COMPLETED =====")


# In[63]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[64]:


plt.figure(figsize=(6, 4))

sns.countplot(data=df, x='Attrition')

plt.title('Employee Attrition Distribution')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')

plt.show()


# In[65]:


plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x='Age',
    hue='Attrition',
    kde=True,
    bins=20
)

plt.title('Employee Age Distribution by Attrition')
plt.xlabel('Age')
plt.ylabel('Number of Employees')

plt.show()


# In[66]:


# Create age groups
bins = [0, 24, 34, 44, 54, 100]

labels = [
    'Under 25',
    '25-34',
    '35-44',
    '45-54',
    '55+'
]

df['AgeGroup'] = pd.cut(
    df['Age'],
    bins=bins,
    labels=labels
)

# Calculate attrition rate for each age group
age_attrition = (
    df.groupby('AgeGroup', observed=False)['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

print(age_attrition)


# In[67]:


plt.figure(figsize=(8, 5))

sns.barplot(
    data=age_attrition,
    x='AgeGroup',
    y='Attrition Rate'
)

plt.title('Attrition Rate by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Attrition Rate (%)')

plt.ylim(0, age_attrition['Attrition Rate'].max() + 5)

plt.show()


# In[68]:


plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x='Attrition',
    y='MonthlyIncome'
)

plt.title('Monthly Income by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Monthly Income')

plt.show()


# In[69]:


# Create income groups
bins = [0, 3000, 6000, 9000, 12000, float('inf')]

labels = [
    'Under 3K',
    '3K-6K',
    '6K-9K',
    '9K-12K',
    '12K+'
]

df['IncomeGroup'] = pd.cut(
    df['MonthlyIncome'],
    bins=bins,
    labels=labels
)

# Calculate attrition rate for each income group
income_attrition = (
    df.groupby('IncomeGroup', observed=False)['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

print(income_attrition)


# In[70]:


plt.figure(figsize=(8, 5))

sns.barplot(
    data=income_attrition,
    x='IncomeGroup',
    y='Attrition Rate'
)

plt.title('Attrition Rate by Monthly Income Group')
plt.xlabel('Monthly Income Group')
plt.ylabel('Attrition Rate (%)')

plt.ylim(0, income_attrition['Attrition Rate'].max() + 5)

plt.show()


# In[71]:


overtime_attrition = (
    df.groupby('OverTime')['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

print(overtime_attrition)


# In[72]:


plt.figure(figsize=(7, 5))

sns.barplot(
    data=overtime_attrition,
    x='OverTime',
    y='Attrition Rate'
)

plt.title('Attrition Rate by Overtime')
plt.xlabel('Overtime')
plt.ylabel('Attrition Rate (%)')

plt.ylim(0, overtime_attrition['Attrition Rate'].max() + 5)

plt.show()


# In[73]:


job_satisfaction_attrition = (
    df.groupby('JobSatisfaction')['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

print(job_satisfaction_attrition)


# In[74]:


plt.figure(figsize=(8, 5))

sns.barplot(
    data=job_satisfaction_attrition,
    x='JobSatisfaction',
    y='Attrition Rate'
)

plt.title('Attrition Rate by Job Satisfaction')
plt.xlabel('Job Satisfaction Level')
plt.ylabel('Attrition Rate (%)')

plt.ylim(0, job_satisfaction_attrition['Attrition Rate'].max() + 5)

plt.show()


# In[75]:


plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x='Attrition',
    y='YearsAtCompany'
)

plt.title('Years at Company by Attrition')
plt.xlabel('Attrition')
plt.ylabel('Years at Company')

plt.show()


# In[76]:


# Create tenure groups
bins = [-1, 2, 5, 10, float('inf')]

labels = [
    '0-2 Years',
    '3-5 Years',
    '6-10 Years',
    '11+ Years'
]

df['TenureGroup'] = pd.cut(
    df['YearsAtCompany'],
    bins=bins,
    labels=labels
)

# Calculate attrition rate for each tenure group
tenure_attrition = (
    df.groupby('TenureGroup', observed=False)['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

print(tenure_attrition)


# In[77]:


plt.figure(figsize=(8, 5))

sns.barplot(
    data=tenure_attrition,
    x='TenureGroup',
    y='Attrition Rate'
)

plt.title('Attrition Rate by Years at Company')
plt.xlabel('Tenure Group')
plt.ylabel('Attrition Rate (%)')

plt.ylim(0, tenure_attrition['Attrition Rate'].max() + 5)

plt.show()


# In[78]:


# Create required summary data

department_attrition = (
    df.groupby('Department')['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
)

jobrole_attrition = (
    df.groupby('JobRole')['Attrition']
      .apply(lambda x: (x == 'Yes').mean() * 100)
      .reset_index(name='Attrition Rate')
      .sort_values('Attrition Rate', ascending=False)
)

# Create dashboard
fig, axes = plt.subplots(2, 2, figsize=(16, 10))

# 1. Department Attrition
sns.barplot(
    data=department_attrition,
    x='Department',
    y='Attrition Rate',
    ax=axes[0, 0]
)

axes[0, 0].set_title('Attrition Rate by Department')
axes[0, 0].set_xlabel('')
axes[0, 0].set_ylabel('Attrition Rate (%)')

# 2. Job Role Attrition
sns.barplot(
    data=jobrole_attrition,
    x='Attrition Rate',
    y='JobRole',
    ax=axes[0, 1]
)

axes[0, 1].set_title('Attrition Rate by Job Role')
axes[0, 1].set_xlabel('Attrition Rate (%)')
axes[0, 1].set_ylabel('')

# 3. Overtime Attrition
sns.barplot(
    data=overtime_attrition,
    x='OverTime',
    y='Attrition Rate',
    ax=axes[1, 0]
)

axes[1, 0].set_title('Attrition Rate by Overtime')
axes[1, 0].set_xlabel('Overtime')
axes[1, 0].set_ylabel('Attrition Rate (%)')

# 4. Tenure Group Attrition
sns.barplot(
    data=tenure_attrition,
    x='TenureGroup',
    y='Attrition Rate',
    ax=axes[1, 1]
)

axes[1, 1].set_title('Attrition Rate by Tenure Group')
axes[1, 1].set_xlabel('Tenure Group')
axes[1, 1].set_ylabel('Attrition Rate (%)')

plt.tight_layout()
plt.show()


# In[79]:


df.columns.tolist()


# In[81]:


df['TenureGroup'] = pd.cut(
    df['YearsAtCompany'],
    bins=[-1, 2, 5, 10, 100],
    labels=['0-2 Years', '3-5 Years', '6-10 Years', '10+ Years']
)


# In[82]:


df['TenureGroup'].value_counts()


# In[83]:


df['SatisfactionGroup'] = pd.cut(
    df['JobSatisfaction'],
    bins=[0, 2, 3, 4],
    labels=['Low', 'Medium', 'High']
)


# In[84]:


df['SatisfactionGroup'].value_counts()


# In[85]:


risk_segment = df.groupby(
    ['OverTime', 'SatisfactionGroup', 'TenureGroup'],
    observed=False
).agg(
    TotalEmployees=('Attrition', 'count'),
    EmployeesLeft=('Attrition', lambda x: (x == 'Yes').sum())
)


# In[86]:


risk_segment['AttritionRate'] = (
    risk_segment['EmployeesLeft'] /
    risk_segment['TotalEmployees']
) * 100


# In[87]:


risk_segment = risk_segment.reset_index()


# In[88]:


risk_segment.sort_values(
    by='AttritionRate',
    ascending=False
)


# In[89]:


risk_segment_filtered = risk_segment[
    risk_segment['TotalEmployees'] >= 10
]


# In[90]:


high_risk_segments = risk_segment_filtered.sort_values(
    by='AttritionRate',
    ascending=False
)

high_risk_segments


# In[91]:


top_10_risk_segments = high_risk_segments.head(10)

top_10_risk_segments


# In[92]:


top_10_risk_segments = top_10_risk_segments.copy()

top_10_risk_segments['RiskSegment'] = (
    'OverTime: ' + top_10_risk_segments['OverTime'].astype(str)
    + ' | Satisfaction: ' +
    top_10_risk_segments['SatisfactionGroup'].astype(str)
    + ' | Tenure: ' +
    top_10_risk_segments['TenureGroup'].astype(str)
)


# In[93]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

plt.barh(
    top_10_risk_segments['RiskSegment'],
    top_10_risk_segments['AttritionRate']
)

plt.xlabel('Attrition Rate (%)')
plt.ylabel('Employee Segment')

plt.title('Top 10 High-Risk Employee Segments')

plt.gca().invert_yaxis()

plt.show()


# In[94]:


department_risk = df.groupby(
    ['Department', 'OverTime', 'SatisfactionGroup'],
    observed=False
).agg(
    TotalEmployees=('Attrition', 'count'),
    EmployeesLeft=('Attrition', lambda x: (x == 'Yes').sum())
).reset_index()


# In[95]:


department_risk['AttritionRate'] = (
    department_risk['EmployeesLeft'] /
    department_risk['TotalEmployees']
) * 100


# In[96]:


department_risk = department_risk[
    department_risk['TotalEmployees'] >= 10
]


# In[97]:


department_risk = department_risk.sort_values(
    by='AttritionRate',
    ascending=False
)

department_risk.head(10)


# In[98]:


jobrole_risk = df.groupby(
    ['JobRole', 'OverTime', 'TenureGroup'],
    observed=False
).agg(
    TotalEmployees=('Attrition', 'count'),
    EmployeesLeft=('Attrition', lambda x: (x == 'Yes').sum())
).reset_index()


# In[99]:


jobrole_risk['AttritionRate'] = (
    jobrole_risk['EmployeesLeft'] /
    jobrole_risk['TotalEmployees']
) * 100


# In[100]:


jobrole_risk = jobrole_risk[
    jobrole_risk['TotalEmployees'] >= 10
]


# In[101]:


jobrole_risk = jobrole_risk.sort_values(
    by='AttritionRate',
    ascending=False
)

jobrole_risk.head(10)


# In[102]:


print("===== TOP HIGH-RISK EMPLOYEE SEGMENTS =====")

print("\n1. Overtime + Satisfaction + Tenure")
display(high_risk_segments.head(5))

print("\n2. Department + Overtime + Satisfaction")
display(department_risk.head(5))

print("\n3. Job Role + Overtime + Tenure")
display(jobrole_risk.head(5))


# In[ ]:




