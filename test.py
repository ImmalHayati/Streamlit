import streamlit as st

def main():
    st.title("Simple Streamlit App")
    
    # Add a header
    st.header("This is a header")

    # Add some text
    st.write("Welcome to my Streamlit app!")

    # Add a sidebar
    st.sidebar.title("Sidebar")
    st.sidebar.write("This is a sidebar.")

    # Add a button
    if st.button("Click Me!"):
        st.write("You clicked the button!")

    # Add a checkbox
    checkbox_state = st.checkbox("Show/Hide Text")
    if checkbox_state:
        st.write("You checked the box!")

    # Add a selectbox
    option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", option)

    # Add a slider
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write("Slider value:", slider_value)

if __name__ == "__main__":
    main()
