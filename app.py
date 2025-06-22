import streamlit as st
from algorithm import rabin_karp
from utils import highlight_text

st.title("🔍 Rabin-Karp String Matching Visualizer")

text = st.text_area("Text:", "ABABDABACDABABCABAB")
pattern = st.text_input("Pattern:", "ABABC")

if st.button("Show Matches"):
    if pattern and text:
        matches, steps = rabin_karp(text, pattern)

        st.subheader("🧮 Step-by-Step Execution")
        for step in steps:
            st.code(
                f"Index {step['index']}: '{step['window']}' | Hash: {step['current_hash']} | {'✔ Match' if step['match'] else '❌'}"
            )

        st.subheader("✅ Match Results")
        if matches:
            for idx in matches:
                st.markdown(highlight_text(text, idx, len(pattern)))
        else:
            st.warning("No matches found.")
