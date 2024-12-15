'''
Game analyser UI
'''
import os
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://game-analyser.onrender.com"

st.title("Game Analytics Explore UI")

st.sidebar.header("Build Your Filter")

filters = {}

field = st.sidebar.text_input("Field Name (e.g., AppID, Release_date)")
value = st.sidebar.text_input("Field Value (e.g., 123)")
operation = st.sidebar.selectbox("Operation", ["Equals", "Greater than", "Less than"])

if field and value and operation:
    if operation == "Equals":
        filters[field] = value
    elif operation == "Greater than":
        filters[f"{field}__gt"] = value
    elif operation == "Less than":
        filters[f"{field}__lt"] = value

st.sidebar.write("### Current Filters:")
st.sidebar.json(filters)

st.sidebar.write("---")
run_query = st.sidebar.button("Get Results")

st.subheader("Results")

if run_query:
    try:
        headers = {
            "accept": "application/json",
            "x-api-key": os.environ.get('API_KEY')

        }
        response = requests.post(
            f"{BASE_URL}/explore",
            json={"filters": filters},
            headers=headers,
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            st.success("Query successful!")

            # Display data as a table
            if data["data"]:
                df = pd.DataFrame(data["data"])
                st.dataframe(
                    df.style.set_table_styles(
                        [
                            {"selector": "th", "props": [("text-align", "center")]},
                            {"selector": "td", "props": [("text-align", "left")]},
                        ]
                    ).set_properties(subset=df.columns, **{"white-space": "nowrap"}),
                    use_container_width=True,
                )
            else:
                st.warning("No results found.")
        else:
            st.error(f"Error: {response.status_code}")
            st.json(response.json())
    except Exception as e:
        st.error("Error occurred while querying the API.")
        st.exception(e)
