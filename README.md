# HR Employee Attrition Analytics

## 📌 Project Overview

This project analyzes employee attrition using **Excel, SQL, Python, and Power BI**.

The goal is to understand why employees leave an organization, identify high-risk employee groups, and provide data-driven recommendations that can help HR teams improve employee retention.

The project follows an end-to-end data analytics workflow:

**Raw Data → Data Cleaning → SQL Analysis → Python Analysis → Power BI Dashboard → Business Insights**

---

## 🎯 Business Problem

Employee attrition can increase recruitment costs, reduce productivity, and affect team performance.

The HR department needs to understand:

* How many employees are leaving the organization?
* Which departments have the highest attrition?
* Which job roles have higher attrition?
* Does overtime affect employee attrition?
* Does job satisfaction influence attrition?
* Which age groups have higher attrition?
* Does salary or job level relate to employee turnover?
* Which employee segments may require greater retention attention?

This project uses data analysis to answer these business questions.

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Calculate the overall employee attrition rate.
2. Analyze attrition by department.
3. Analyze attrition by job role.
4. Analyze attrition by age group.
5. Analyze attrition by overtime.
6. Analyze attrition by job satisfaction.
7. Analyze attrition by salary and job level.
8. Analyze attrition by years at company.
9. Identify high-risk employee segments.
10. Create an interactive HR analytics dashboard.
11. Provide business recommendations based on the analysis.

---

## 📊 Dataset

The project uses an HR Employee Attrition dataset containing employee-level information.

Important columns include:

| Column                  | Description                                |
| ----------------------- | ------------------------------------------ |
| Age                     | Employee age                               |
| Department              | Employee department                        |
| JobRole                 | Employee job role                          |
| MonthlyIncome           | Monthly employee income                    |
| OverTime                | Whether the employee works overtime        |
| JobSatisfaction         | Employee job satisfaction rating           |
| YearsAtCompany          | Number of years at the company             |
| WorkLifeBalance         | Work-life balance rating                   |
| PerformanceRating       | Employee performance rating                |
| YearsSinceLastPromotion | Years since the last promotion             |
| Attrition               | Whether the employee left the organization |
| JobLevel                | Employee job level                         |
| DistanceFromHome        | Distance between home and workplace        |
| EnvironmentSatisfaction | Workplace environment satisfaction         |
| JobInvolvement          | Employee involvement level                 |
| TotalWorkingYears       | Total years of professional experience     |

---

## 🛠️ Tools & Technologies

### Excel

Used for:

* Initial data inspection
* Data validation
* Data cleaning
* Basic analysis
* Summary tables
* Data dictionary
* Value reference documentation

### SQL

Used for:

* Database creation
* Data cleaning
* Data validation
* Aggregation
* Business analysis
* Attrition calculations
* Department analysis
* Job role analysis
* Overtime analysis
* Job satisfaction analysis

### Python

Used for:

* Exploratory Data Analysis
* Data validation
* Statistical analysis
* Attrition analysis
* Identifying patterns and trends
* Creating analytical visualizations

Libraries used:

* pandas
* numpy
* matplotlib
* seaborn

### Power BI

Used for:

* Interactive dashboard creation
* KPI cards
* Charts
* Filters and slicers
* Business insights
* HR decision support

---

## 🧹 Data Cleaning

The dataset was reviewed and prepared before analysis.

The cleaning process included:

* Checking the dataset structure
* Checking missing values
* Checking duplicate records
* Checking data types
* Checking categorical values
* Validating numerical columns
* Checking the Attrition column
* Creating appropriate analysis groups
* Preparing the cleaned dataset for analysis

The original dataset was preserved separately from the cleaned dataset.

---

## 🗄️ SQL Analysis

SQL was used to answer important HR business questions.

Examples include:

### Overall Attrition

* Total employees
* Employees who left
* Overall attrition rate

### Department Analysis

* Total employees by department
* Employees who left by department
* Attrition rate by department

### Job Role Analysis

* Total employees by job role
* Employees who left by job role
* Attrition rate by job role

### Overtime Analysis

* Attrition among employees working overtime
* Attrition among employees not working overtime

### Job Satisfaction Analysis

* Employee count by satisfaction level
* Employees leaving by satisfaction level
* Attrition rate by satisfaction level

### Age Group Analysis

Employees were grouped into:

* 18–25
* 26–35
* 36–45
* 46–55
* 56+

These groups were analyzed to identify differences in attrition.

---

## 🐍 Python Analysis

Python was used to perform exploratory data analysis and identify patterns in employee attrition.

The analysis included:

* Dataset inspection
* Missing-value analysis
* Duplicate analysis
* Descriptive statistics
* Attrition distribution
* Attrition by department
* Attrition by job role
* Attrition by age group
* Attrition by overtime
* Attrition by job satisfaction
* Attrition by income
* Attrition by years at company

The complete analysis is available in:

`Python/HR_Attrition_Analysis.ipynb`

---

## 📈 Power BI Dashboard

The final Power BI dashboard provides an interactive overview of employee attrition.

### Key KPIs

* Total Employees
* Employees Who Left
* Attrition Rate
* Average Monthly Income
* Average Years at Company

### Main Visualizations

* Attrition by Department
* Attrition by Job Role
* Attrition by Age Group
* Attrition by Overtime
* Attrition by Job Satisfaction
* Attrition by Job Level
* Attrition by Years at Company

### Interactive Filters

Users can filter the dashboard by relevant employee attributes such as:

* Department
* Job Role
* Gender
* Overtime
* Job Level
* Age Group
* Job Satisfaction

---

## 📸 Dashboard Preview

### HR Employee Attrition Dashboard

![HR Attrition Dashboard](Screenshots/dashboard.png)

The complete Power BI file is available here:

`PowerBI/HR_Attrition_Dashboard.pbix`

---

## 🔍 Key Findings

The analysis identified several employee segments with differences in attrition.

Key findings include:

* Employee attrition varies across departments.
* Attrition differs significantly across job roles.
* Employees working overtime show different attrition patterns compared with employees who do not work overtime.
* Job satisfaction is associated with differences in employee attrition.
* Attrition varies across different age groups.
* Employee tenure can be an important factor when analyzing employee turnover.
* Some employee segments may require additional retention attention.

> Note: The exact numerical findings should be updated here using the final results from the SQL, Python, and Power BI analysis.

---

## 💡 Business Recommendations

Based on the analysis, HR teams could consider the following actions:

### 1. Focus on High-Attrition Departments

Identify departments with above-average attrition and investigate the underlying causes.

### 2. Review High-Risk Job Roles

Analyze workload, compensation, career growth, and job satisfaction for roles with higher attrition.

### 3. Monitor Overtime

Employees working frequent overtime may require workload reviews and better work-life balance support.

### 4. Improve Employee Satisfaction

Use employee surveys and feedback programs to identify workplace issues affecting satisfaction.

### 5. Strengthen Career Development

Provide training, promotion opportunities, mentoring, and clear career paths.

### 6. Improve Retention Strategies

Develop targeted retention programs for employee groups with higher attrition risk.

---

## 📁 Project Structure

```text
HR-Employee-Attrition-Analytics
│
├── Dataset
│   └── HR_Employee_Data.csv
│
├── Excel
│   ├── HR_Analysis.xlsx
│   └── Data_Dictionary.xlsx
│
├── SQL
│   ├── database_setup.sql
│   ├── data_cleaning.sql
│   └── business_analysis.sql
│
├── Python
│   ├── HR_Attrition_Analysis.ipynb
│   └── requirements.txt
│
├── PowerBI
│   └── HR_Attrition_Dashboard.pbix
│
├── Screenshots
│   └── dashboard.png
│
└── README.md
```

---

## 🚀 Project Workflow

```text
Raw Dataset
     ↓
Data Cleaning
     ↓
Excel Analysis
     ↓
SQL Analysis
     ↓
Python Exploratory Analysis
     ↓
Power BI Dashboard
     ↓
Business Insights
     ↓
Recommendations
```

---

## 📌 Skills Demonstrated

This project demonstrates practical skills in:

* Data Cleaning
* Data Analysis
* Exploratory Data Analysis
* SQL
* Python
* Excel
* Power BI
* Data Visualization
* KPI Development
* Business Analysis
* HR Analytics
* Dashboard Development
* Data Storytelling

---

## 👩‍💻 Author

**Mekala Sanjana**

Data Analytics Portfolio Project

---

## ⭐ Conclusion

This HR Employee Attrition Analytics project demonstrates an end-to-end approach to solving a real-world business problem using data.

The project combines **Excel, SQL, Python, and Power BI** to transform raw employee data into meaningful HR insights and actionable recommendations.
