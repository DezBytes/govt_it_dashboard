# 🏛️ US Government IT Investment Dashboard

An interactive dashboard built with **Streamlit** and **Pandas** to visualize Federal IT spending for Fiscal Year 2025. This project was born out of a sudden obsession with learning to code and understanding where government billions are actually going.

## 🚀 Features
* **Live Agency Filtering:** Select any government agency to see their specific IT budget.
* **Smart KPI Metrics:** Automatically calculates total spending, including logic to handle Millions vs. Billions.
* **Unclassified Data Focus:** Specifically tracks "Major IT Investments" provided by the official OMB IT Dashboard.

## 📊 The Data
The data is sourced from the public **ITDashboard.gov** 2025 snapshot.

> **Note on Accuracy:** > While most civilian agencies (like the USDA) show nearly 100% of their budget, the **Department of Defense (DOD)** total in this dashboard reflects only **Unclassified Major Investments** (~$29B). The remaining budget (~$35B) is typically classified or operational and not included in public project-level CSVs.

## 🛠️ How to Run Locally
1. Clone this repository.
2. Install dependencies: 
   ```bash
   pip install streamlit pandas
   Run this app: streamlit run dashboard.py
