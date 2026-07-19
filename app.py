import streamlit as st
from groq import Groq
st.markdown("""
<style>
.stApp {
    background-color: Azure;;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(
    page_title="AI Prompt Generator",
    page_icon="🤖",
    layout="centered"
    )

st.title("🤖 AI Prompt Generator")
st.write("Enter your task and get a professional AI prompt.")

client = Groq(
    api_key="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"
)

task = st.text_area(
    "Enter your task",
    placeholder="Example: I want Python code for a for loop"
)

if st.button("Generate Prompt"):

    if task.strip() == "":
        st.warning("Please enter your task.")

    else:

        instruction = f"""
You are an Expert Prompt Engineer.

Convert the following user request into a professional AI prompt.

Rules:
- Make it detailed.
- Keep it clear.
- Return ONLY the final prompt.
- No explanation.

User Request:
{task}
"""

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                     {
                        "role": "user",
                        "content": instruction
                    }
                ],
                temperature=0.5,
            )

            result = response.choices[0].message.content

            st.subheader("Generated Prompt")

            st.text_area(
                "Generated Prompt",
                value=result,
                height=300
            )


        except Exception as e:
            st.error(f"Error: {e}")