import streamlit as st

st.set_page_config(
    page_title="Badminton Tournament Manager",
    layout="wide"
)

st.sidebar.title(" Tournament Manager")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Players",
        "Fixtures",
        "Results"
    ]
)

if page == "Dashboard":

    st.title(" Badminton Tournament Manager")

    c1, c2, c3 = st.columns(3)

    c1.metric("Current Round", 1)

    c2.metric("Players", 0)

    c3.metric("Bracket Size", 0)

    st.divider()

    st.info(
        "Register players to begin the tournament."
    )

elif page == "Players":

    st.title("👥 Player Registration")

    st.text_input("Player Name")

    st.selectbox(
        "Experience",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    st.button("➕ Add Player")

elif page == "Fixtures":

    st.title(" Fixtures")

    st.info("No fixtures generated.")

elif page == "Results":

    st.title(" Results")

    st.info("Tournament has not started.")