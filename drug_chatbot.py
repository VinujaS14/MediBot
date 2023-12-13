import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report

# Load dataset
data = pd.read_csv('drug_information.csv')  # Replace 'drug_information.csv' with your dataset filename

# Extract relevant columns
relevant_columns = ['name', 'substitute0', 'substitute1', 'sideEffect0', 'sideEffect1', 'use0', 'use1',
                    'Chemical Class', 'Habit Forming', 'Therapeutic Class', 'Action Class']
relevant_data = data[relevant_columns]

# Clean the data as needed (handle missing values, data type conversions, etc.)
relevant_data.fillna('', inplace=True)  # Replace NaN values with empty string
relevant_data = relevant_data.apply(lambda x: x.str.lower() if x.dtype == 'object' else x)

# Example function to retrieve drug information based on user query
def get_drug_information(drug_name):
    drug_info = relevant_data[relevant_data['name'].str.contains(drug_name.lower())]
    if not drug_info.empty:
        substitutes = drug_info.iloc[0]['substitute0':'substitute1'].tolist()
        side_effects = drug_info.iloc[0]['sideEffect0':'sideEffect1'].tolist()
        uses = drug_info.iloc[0]['use0':'use1'].tolist()
        chemical_class = drug_info.iloc[0]['Chemical Class']
        habit_forming = drug_info.iloc[0]['Habit Forming']
        therapeutic_class = drug_info.iloc[0]['Therapeutic Class']
        action_class = drug_info.iloc[0]['Action Class']
        
        response = f"Substitutes: {', '.join(substitutes)}\n"
        response += f"Side Effects: {', '.join(side_effects)}\n"
        response += f"Uses: {', '.join(uses)}\n"
        response += f"Chemical Class: {chemical_class}\n"
        response += f"Habit Forming: {habit_forming}\n"
        response += f"Therapeutic Class: {therapeutic_class}\n"
        response += f"Action Class: {action_class}\n"
        
        return response
    else:
        return "Sorry, information about this drug is not available."

# Example usage:
user_input = "Tell me about aspirin"
drug_name = user_input.split()[-1]  # Assuming the last word is the drug name
response = get_drug_information(drug_name)
print(response)
