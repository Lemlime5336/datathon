import streamlit as st

pages = {
    "Form": [
        st.Page("medf.py", title="Migrant Employee Details Form (MEDF)")
    ],
    "Analysis": [
        st.Page("population.py", title="Population"),
        st.Page("nationality.py", title="Nationality")
    ],
}

pg = st.navigation(pages)
pg.run()