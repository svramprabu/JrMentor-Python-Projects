import streamlit as st

def main():
    st.title("DataFrame Generator")

    # Get number of columns
    num_columns = st.number_input("Enter number of columns:", value=2)
    df={}
    # Buttons
    # st.button("Enter", on_click=input_values,args=(df,num_columns))
    # st.button("Convert", on_click=convert,args=df)

# def input_values(df,num_columns):
    """Function to take user input and store it in session state."""
    for i in range(num_columns):
        column_name = st.text_input(f"Enter column name for Column {i + 1}:", key=f"a{i}")
        values = st.text_area(f"Enter values for {column_name} (comma-separated):", key=f"b{i}")

        df[column_name] = values.split()


# def convert(df):
    """Function to generate and display the DataFrame."""
    st.dataframe(df)




main()