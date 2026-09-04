import streamlit as st
from matcher import ResumeJobMatcher


st.set_page_config(
    page_title="Resume-to-Job Matching Recommender",
    page_icon="💼",
    layout="wide"
)

st.title("💼 Resume-to-Job Matching Recommender")
st.write(
    "Enter your resume below and find the most relevant jobs "
    "using semantic similarity."
)

resume = st.text_area(
    "Paste your resume",
    height=250,
    placeholder="Example: Python developer with experience in machine learning, SQL..."
)

top_k = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Find Matching Jobs"):
    if not resume.strip():
        st.warning("Please enter your resume before searching.")
    else:
        try:
            with st.spinner("Finding the best matching jobs..."):
                matcher = ResumeJobMatcher()
                results = matcher.match(resume, top_k)

            if results.empty:
                st.warning("No matching jobs were found.")
            else:
                st.subheader("Recommended Jobs")

                for _, row in results.iterrows():
                    score = row["similarity_score"]

                    st.markdown(f"### {row['job_title']}")
                    st.write(row["job_description"])
                    st.write(f"**Similarity Score:** {score:.2%}")
                    st.divider()

        except Exception as error:
            st.error(
                "Something went wrong while processing your resume. "
                "Please check the project setup and try again."
            )
            st.caption(f"Technical error: {error}")
