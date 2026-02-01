import streamlit as st
import pandas as pd

# Set the page title
st.caption("Federal IT Portfolio Dashboard 2025")
st.title("🏛️ IT Investment Tracker")

# 1. Function to load and clean the data
@st.cache_data
def load_data():
    # Use the relative path to find the file where it is hiding
    file_path = '.venv/IT Portfolio.csv'
    
    # Load the CSV
    data = pd.read_csv(file_path)
    
    # Clean the column names (removes hidden spaces)
    data.columns = data.columns.str.strip()
    
    # Rename columns to make them easier to use in the code
    # We map the REAL spreadsheet names to our code names
    data = data.rename(columns={
        'agencyName': 'Agency_Name',
        'FY2025 Internal Funding': 'IT_Spending'
    })
    
    # Convert 'IT_Spending' to numbers so the chart can read them
    data['IT_Spending'] = pd.to_numeric(data['IT_Spending'], errors='coerce').fillna(0)
    
    # Only keep rows that actually have an Agency
    data = data.dropna(subset=['Agency_Name'])
    
    return data

# 2. Run the function (Must be all the way to the left!)
data = load_data()
# 3. Create the Sidebar for filtering
st.sidebar.header("Filter Options")

# Get a unique list of agencies for the dropdown
agency_list = sorted(data['Agency_Name'].unique())
selected_agency = st.sidebar.selectbox("Select an Agency", agency_list)

# 4. Filter the data based on selection
filtered_data = data[data['Agency_Name'] == selected_agency]

# 5. Display the Dashboard Content
st.subheader(f"Investment Overview: {selected_agency}")

# 1. Calculate the grand total for the selected agency
total_spent = filtered_data['IT_Spending'].sum() * 1000000 #covert to dollars

# 2. Format it to look like real money (with commas and a $ sign)
formatted_total = f"${total_spent/1e9:.2f} Billion"

# 3. Show it in a big, bold metric card
st.metric(label=f"Total 2025 IT Investment for {selected_agency}", value=formatted_total)
# Optional: Show the raw data table below the chart
if st.checkbox("Show Raw Data"):
    st.write(filtered_data)