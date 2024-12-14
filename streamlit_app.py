import requests
import streamlit as st
import pandas as pd

# Set up base URL for API
BASE_URL = "http://localhost:8080"

st.title("Game Analytics Explore UI")

# Sidebar for filters
st.sidebar.header("Build Your Filter")

filters = {}

# Dynamic filter input
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

# Preview filters
st.sidebar.write("### Current Filters:")
st.sidebar.json(filters)

# Button to run the query
st.sidebar.write("---")
run_query = st.sidebar.button("Get Results")

# Main Section
st.subheader("Results")

if run_query:
    try:
        # Make a POST request to the FastAPI /explore endpoint
        response = requests.post(
            f"{BASE_URL}/explore",
            json={"filters": filters},
            headers={"accept": "application/json"},
            timeout=5
        )
        if response.status_code == 200:
            data = response.json()
            st.success("Query successful!")

            # Display data as a table
            if data["data"]:
                # Convert results to a pandas DataFrame
                df = pd.DataFrame(data["data"])

                # Render the table in a "pretty" manner
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
