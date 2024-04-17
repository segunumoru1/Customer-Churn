# Financial Inclusion in Africa

### Objective
The objective of this project is to work with the 'Financial Inclusion in Africa' dataset provided by the Zindi platform. The dataset contains demographic information and details about financial services used by approximately 33,600 individuals across East Africa. The goal of the machine learning model is to predict which individuals are most likely to have or use a bank account.

### Dataset Description
The dataset contains demographic information and usage of financial services by individuals across East Africa. The aim is to utilize this data to promote financial inclusion, ensuring that individuals and businesses have access to affordable financial products and services that meet their needs, including transactions, payments, savings, credit, and insurance, delivered in a responsible and sustainable manner.

#### COLUMN EXPLANATION

1. country - Country the interviewee is in
2. year - Year Survey is done
3. uniqueid - unique identifier for each interviewee
4. location_type - Type of location (Urban/Rural)
5. cellphone_access - if the interviewee has access to a cell phone (Yes/No)
6. household_size - Number of people living in one house
7. age_of_respondent - The age of the interviewee
8. gender_of_respondent - Gender of the interviewee (Male or Female)
9. relationship_with_head - The interviewee’s relationship with the head of the house:Head of Household, Spouse, Child, Parent, Other relative, Other non-relatives, Don't know
10. marital status - The marital status of the interviewee: Married/Living together, Divorced or Separated, Widowed, Single/Never married, Don't know
11. education_level - The highest level of education: No formal education, Primary education, Secondary education, Vocational/Specialised training, tertiary education, Other/Dont know/RTA
12. job_type - The type of job the interviewee has: Farming and Fishing, Self-employed, Formally employed Government, Formally employed Private, Informally employed, Remittance Dependent, Government Dependent, Other Income, No Income, Don't know/Refuse to answer


## Methodology
1. **Install the Necessary Packages**: Install the required Python packages and libraries for data analysis, visualization, and machine learning.

2. **Data Import and Basic Exploration**: Import the dataset and perform basic data exploration to understand its structure and contents.

3. **General Information Display**: Display general information about the dataset, including the number of entries, data types, and non-null values.

4. **Pandas Profiling Report**: Generate a Pandas Profiling report to gain comprehensive insights into the dataset, including statistical summaries and data quality assessments.

5. **Handling Missing and Corrupted Values**: Address any missing or corrupted values in the dataset using appropriate techniques such as imputation or removal.

6. **Duplicate Data Removal**: Check for and remove any duplicate entries in the dataset, if they exist.

7. **Outlier Handling**: Identify and handle any outliers in the dataset through techniques such as trimming or transformation.

8. **Categorical Feature Encoding**: Encode categorical features in the dataset to prepare it for machine learning modeling.

9. **Machine Learning Modeling**: Train and test a machine learning classifier based on the insights gained from the data exploration phase.

10. **Streamlit Application Creation**: Develop a Streamlit application locally, incorporating input fields for features and a validation button at the end of the form.

11. **ML Model Integration**: Import the trained machine learning model into the Streamlit application and enable it to make predictions based on user-provided feature values.

12. **Application Deployment on Streamlit Share**: Create GitHub and Streamlit Share accounts, establish a new Git repository, upload the local code to the repository, and deploy the application on Streamlit Share.

### Libraries and Skillsets
- **Libraries**: The project will utilize popular Python libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit for data manipulation, visualization, machine learning, and application development.
  
- **Skillsets**: The project requires proficiency in data preprocessing, exploratory data analysis, machine learning modeling, and web application development using Streamlit.
