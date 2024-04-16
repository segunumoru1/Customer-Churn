import streamlit as st
import joblib
import numpy as np

# Load the trained model
classifier = joblib.load('classifier.pkl')

st.cache_resource
def predict_bank_account(country, year, location_type, cellphone_access,
       household_size, age_of_respondent, gender_of_respondent,
       relationship_with_head, marital_status, education_level,
       job_type):
    
    # Pre-processing User input

    # input values for country
    if country == "Rwanda":
        country = 1
    elif country == "Tanzania":
        country = 2
    elif country == "Kenya":
        country = 3
    else:
        country = 4

    # input values for location type
    if location_type == "Rural":
        location_type = 1
    else:
        location_type = 2

    # input values for cellphone access
    if cellphone_access == "Yes":
        cellphone_access = 1
    else:
        cellphone_access = 0

    # input values for relationship with head
    if marital_status == "Married/Living together":
        marital_status = 1
    elif marital_status == "Single/Never Married":
        marital_status = 2
    elif marital_status == "Widowed":
        marital_status = 3
    elif marital_status == "Divorced/Seperated":
        marital_status = 4
    else:
        marital_status = 5

    # input values for marital status
    if relationship_with_head == "Head of Household":
        relationship_with_head = 1
    elif relationship_with_head == "Spouse":
        relationship_with_head = 2
    elif relationship_with_head == "Child":
        relationship_with_head = 3
    elif relationship_with_head == "Parent":
        relationship_with_head = 4
    else:
        relationship_with_head= 5

     # input values for education_level
    if education_level == "Primary education":
        education_level = 1
    elif education_level == "No formal education":
        education_level = 2
    elif education_level == "Secondary education":
        education_level = 3
    elif education_level == "Tertiary education":
        education_level = 4
    elif education_level == "Vocational/Specialised training":
        education_level = 5
    else:
        education_level = 6

    #input for Gender
    if gender_of_respondent == "Female":
        gender_of_respondent = 0
    else:
        gender_of_respondent = 1
    
    # input value for job type
    if job_type == 'Self employed':
        job_type = 1
    elif job_type == 'Informally employed': 
        job_type = 2
    elif job_type == 'Farming and Fishing':
        job_type = 3
    elif job_type == 'Remittance Dependent':
        job_type = 4
    elif job_type == 'Other Income':
        job_type = 5 
    elif job_type == 'Formally employed Private': 
        job_type = 6
    elif job_type == 'No Income':
        job_type = 7
    elif job_type == 'Formally employed Government':
        job_type = 8
    elif job_type == 'Government Dependent':
        job_type = 9
    else:
        job_type = 10
    

    # Making Predictions
    prediction = classifier.predict([[country, year, location_type, cellphone_access,
       household_size, age_of_respondent, gender_of_respondent,
       relationship_with_head, marital_status, education_level,
       job_type]])

    if prediction == 0:
        pred = "No Interviewee Bank Account"
    else:
        pred = "Interviewee Bank Account"

    return pred

def main():

    # Add a title in blue color
    st.markdown("<h1 style='color: blue;font-size: 34px;'> Interviewee Bank Account Prediction App</h1>", unsafe_allow_html=True)
    
    
    
    country = st.selectbox("Country", ("Rwanda", "Tanzania", "Kenya", "Uganda"))
    year = st.number_input("Year", min_value=2016, max_value=2018, step=1)
    location_type = st.selectbox("Location Type", ("Rural", "Urban"))
    cellphone_access = st.selectbox("Cellphone Access", ("Yes", "No"))
    household_size = st.slider("Household size", min_value=1, max_value=30, step=1)
    age_of_respondent = st.number_input("Age of Respondent", min_value=12, max_value=101, step=1)
    gender_of_respondent = st.selectbox("Gender", ("Female", "Male"))
    relationship_with_head = st.selectbox("Relationship with Head", ("Head of Household", "Spouse", "Child", "Parent", "Other relative", "Other non-relatives"))
    marital_status = st.selectbox("Marital Status", ("Married/Living together", "Single/Never Married", "Widowed", "Divorced/Seperated", "Dont know"))
    education_level = st.selectbox("Education Level", ("primary education", "No formal education", "Secondary education", "Tertiary education", "Vocational/Specialised training", "Other/Dont know/RTA"))
    job_type = st.selectbox("Job Type", ("Self employed", "Informally employed", "Farming and Fishing", "Remittance Dependent", "Other Income", "Formally employed Private", "No Income", "Formally employed Government", "Government Dependent"))
    


    if st.button('Predict'):
        prediction = predict_bank_account(country, year, location_type, cellphone_access, household_size, age_of_respondent, gender_of_respondent, relationship_with_head, marital_status, education_level, job_type)
        st.write('Bank Account Status:', prediction)
        print(prediction)

if __name__ == '__main__':
    main()
