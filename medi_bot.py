import pandas as pd

# Load drug information dataset
drug_data = pd.read_csv('drug_information.csv')  # Replace with your drug dataset filename

# Load dialog dataset
dialog_data = pd.read_csv('dialog_talk_agent.csv')  # Replace with your dialog dataset filename

# Extract relevant columns
drug_columns = ['name', 'substitute0', 'substitute1', 'sideEffect0', 'sideEffect1', 'use0', 'use1',
                'Chemical Class', 'Habit Forming', 'Therapeutic Class', 'Action Class']
relevant_drug_data = drug_data[drug_columns]
relevant_drug_data.fillna('', inplace=True)
relevant_drug_data = relevant_drug_data.apply(lambda x: x.str.lower() if x.dtype == 'object' else x)

# Example function to retrieve drug information based on user query
def get_drug_information(drug_name):
    drug_info = relevant_drug_data[relevant_drug_data['name'].str.contains(drug_name.lower())]
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

# Example function to retrieve response from dialog dataset based on context
def get_dialog_response(context):
    response = dialog_data[dialog_data['Context'].str.lower() == context.lower()]['Text Response']
    if not response.empty:
        return response.values[0]
    else:
        return "I'm not sure about that."

# Function to handle user queries and provide responses
def chat():
    print("Chatbot: Hi! I'm here to help with drug information. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        drug_name = user_input.split()[-1]  # Assuming the last word is the drug name
        response_drug_info = get_drug_information(drug_name)
        context = "General"  # Default context for dialog responses
        response_dialog = get_dialog_response(context)
        
        print("Drug Information:")
        print(response_drug_info)

        print("\nDialog Response:")
        print(response_dialog)

# Run chat function
chat()
