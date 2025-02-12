import streamlit as st

# Hardcoded users (replace with a database for production)
USER_CREDENTIALS = {"admin": "password123", "researcher": "equity2024"}

def authenticate():
    """
    Simple authentication mechanism.
    """
    st.sidebar.header("🔑 User Login ")
    st.sidebar.header("username - researcher")
    st.sidebar.header("password - equity2024")

    # Initialize session state for authentication
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
        st.session_state["username"] = None

    # Only show login form if not authenticated
    if not st.session_state["authenticated"]:
        username = st.sidebar.text_input("Username", key="username_input")
        password = st.sidebar.text_input("Password", type="password", key="password_input")

        if st.sidebar.button("Login"):
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["authenticated"] = True
                st.session_state["username"] = username  # Store the username
                st.sidebar.success(f"✅ Welcome, {username}!")
            else:
                st.sidebar.error("❌ Invalid Credentials!")

    else:
        st.sidebar.success(f"✅ Logged in as {st.session_state['username']}")
        if st.sidebar.button("Logout"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = None
            st.rerun()  # Refresh the app to apply logout

def check_auth():
    """
    Check if user is authenticated before showing the app content.
    If not authenticated, display the login form.
    """
    authenticate()
    if not st.session_state["authenticated"]:
        st.warning("⚠️ Please log in to access the tool.")
        st.stop()  # Stops execution until user logs in
