import streamlit as st
import snowflake.connector

# Function to connect to Snowflake and fetch data
def fetch_data():
    conn = snowflake.connector.connect(
        user='PRIYADHARSHINI',
        password='snowflake1234*',
        account='TJILUEE.ZK66694',
        url='https://cx11847.ap-southeast-1.snowflakecomputing.com',
        database='SNOWFLAKE_SAMPLE_DATA',
        schema='TPCDS_SF100TCL'
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM CUSTOMER LIMIT 10")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

# Streamlit app
st.title('Simple Streamlit App with Snowflake')

st.write('Fetching data from Snowflake...')

data = fetch_data()

if data:
    st.write('Data from Snowflake:')
    for row in data:
        st.write(row)
else:
    st.write('No data found.')
