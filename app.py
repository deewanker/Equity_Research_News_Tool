import streamlit as st
from authentication import check_auth
from langchain_config import get_summary

# Set page config
st.set_page_config(page_title="Equity Research News Tool", page_icon="📈", layout="wide")

check_auth()

st.title("📊 Equity Research News Tool")
st.write("Welcome to the Equity Research News Tool. Use this tool to fetch and summarize news articles.")

# Custom CSS for background and styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: rgba(252, 231, 200);
            padding: 2rem;
            border-radius: 10px;
        }
        .title-text {
            font-size: 42px;
            font-weight: bold;
            color: #FFD700;
            text-align: center;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        }
        .subtitle-text {
            font-size: 22px;
            color: black;
            text-align: center;
        }
        .centered-img {
            display: flex;
            justify-content: center;
        }
        .centered-img img {
            width: 50%;
            border-radius: 10px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.3);
        }
        .summary-box {
            border: 2px solid #4CAF50;
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 3px 3px 10px rgba(0, 0, 0, 0.1);
            font-size: 18px;
            color: #333;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# UI Layout
st.markdown(
    """
    <div class="centered-img">
        <img src="https://img.freepik.com/free-vector/realistic-news-studio-background_23-2149985600.jpg?t=st=1739389418~exp=1739393018~hmac=e8a95b793f1a45f1aa05ed1e45d2a6361b978209d3e9f25888ae8ba075b223b1&w=996">
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='title-text'>📊 Equity Research News Tool</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-text'>Enter your query to get the latest summarized news articles</p>", unsafe_allow_html=True)

# Input Section
query = st.text_input("Enter your query", "", key="query_input")

# Button with hover effect
st.markdown(
    """
    <style>
        div.stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px 28px;
            border-radius: 8px;
            transition: 0.3s;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        div.stButton > button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Fetch News Summary
if st.button("Get News 📰"):
    if query:
        with st.spinner("Fetching latest news..."):
            summary = get_summary(query)
        
        st.success("✅ Summary Generated!")

        # Display the summary inside a bordered box
        st.markdown(
            f"""
            <div class="summary-box">
                <h3>📝 Summary:</h3>
                <p><b>{summary}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("⚠️ Please enter a query.")
