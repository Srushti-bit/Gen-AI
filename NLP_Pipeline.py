import streamlit as st
import spacy
import pandas as pd

# -------------------------------
# Load spaCy Model
# -------------------------------
nlp = spacy.load("en_core_web_sm")

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="NLP Pipeline Demo",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Custom CSS
# -------------------------------
st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    color:#1565C0;
    text-align:center;
}

h2,h3{
    color:#0D47A1;
}

.stButton>button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

.block-container{
    padding-top:2rem;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.title("🧠 NLP Pipeline")

st.sidebar.markdown("---")

st.sidebar.info(
"""
This application demonstrates the basic
Natural Language Processing pipeline
using **spaCy**.

### Features

- 🔤 Tokenization
- 🚫 Stopword Removal
- 🏷️ POS Tagging
- 📚 Lemmatization
- 🧑 Named Entity Recognition
- 🔗 Dependency Parsing
- 📄 Sentence Segmentation
- 📊 Word Frequency
- 📈 Text Statistics
"""
)

st.sidebar.markdown("---")

st.sidebar.success("Built with ❤️ using Streamlit & spaCy")

# -------------------------------
# Title
# -------------------------------
st.title("🧠 Natural Language Processing Pipeline")

st.markdown("""
Explore how Natural Language Processing works by entering any paragraph.

This demo performs multiple NLP preprocessing tasks using **spaCy**.
""")

st.markdown("---")

# -------------------------------
# User Input
# -------------------------------
text = st.text_area(
    "✍ Enter your text below",
    height=220,
    placeholder="Example: Apple Inc. was founded by Steve Jobs in California in 1976."
)

# -------------------------------
# Live Statistics
# -------------------------------
col1, col2, col3 = st.columns(3)

col1.metric("Characters", len(text))
col2.metric("Words", len(text.split()))
col3.metric("Lines", len(text.splitlines()))

st.markdown("---")

# -------------------------------
# Process Button
# -------------------------------
if st.button("🚀 Analyze Text", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter some text.")
        st.stop()

    with st.spinner("Analyzing text..."):

        doc = nlp(text)

        # --------------------------
        # Tokenization
        # --------------------------
        tokens = [token.text for token in doc]

        # --------------------------
        # Stopword Removal
        # --------------------------
        filtered = [
            token.text
            for token in doc
            if not token.is_stop and token.is_alpha
        ]

        # --------------------------
        # POS Tagging
        # --------------------------
        pos_data = []

        for token in doc:
            pos_data.append({
                "Word": token.text,
                "POS": token.pos_,
                "Tag": token.tag_
            })

        # --------------------------
        # Lemmatization
        # --------------------------
        lemma_data = []

        for token in doc:
            lemma_data.append({
                "Word": token.text,
                "Lemma": token.lemma_
            })

        # --------------------------
        # Named Entity Recognition
        # --------------------------
        entity_data = []

        for ent in doc.ents:
            entity_data.append({
                "Entity": ent.text,
                "Label": ent.label_
            })

        # --------------------------
        # Dependency Parsing
        # --------------------------
        dep_data = []

        for token in doc:
            dep_data.append({
                "Word": token.text,
                "Dependency": token.dep_,
                "Head": token.head.text
            })

        # --------------------------
        # Token Details
        # --------------------------
        token_data = []

        for token in doc:
            token_data.append({
                "Text": token.text,
                "Lemma": token.lemma_,
                "POS": token.pos_,
                "Shape": token.shape_,
                "Alpha": token.is_alpha,
                "Stop Word": token.is_stop
            })

        # --------------------------
        # Word Frequency
        # --------------------------
        frequency = {}

        for token in filtered:
            word = token.lower()
            frequency[word] = frequency.get(word, 0) + 1

        freq_df = pd.DataFrame(
            frequency.items(),
            columns=["Word", "Frequency"]
        ).sort_values(
            by="Frequency",
            ascending=False
        )

        # --------------------------
        # Statistics
        # --------------------------
        stats = {
            "Characters": len(text),
            "Words": len(tokens),
            "Unique Words": len(set(filtered)),
            "Sentences": len(list(doc.sents)),
            "Named Entities": len(list(doc.ents))
        }

        st.success("✅ NLP Pipeline executed successfully!")

        # --------------------------
        # Tabs
        # --------------------------
        tab1, tab2, tab3, tab4, tab5 = st.tabs(
            [
                "🔤 Tokens",
                "🏷 POS",
                "📚 Lemmas",
                "🧑 NER",
                "📊 Analysis"
            ]
        )
                # ==========================================
        # TAB 1 : TOKENIZATION
        # ==========================================
        with tab1:

            st.subheader("🔤 Tokenization")
            st.write(tokens)

            st.subheader("🚫 Stopword Removal")
            st.write(filtered)

            st.metric("Total Tokens", len(tokens))
            st.metric("Filtered Tokens", len(filtered))

        # ==========================================
        # TAB 2 : POS TAGGING
        # ==========================================
        with tab2:

            st.subheader("🏷️ Part-of-Speech Tagging")

            st.dataframe(
                pd.DataFrame(pos_data),
                use_container_width=True,
                hide_index=True
            )

            pos_count = {}

            for token in doc:
                pos = token.pos_
                pos_count[pos] = pos_count.get(pos, 0) + 1

            st.subheader("POS Distribution")

            st.bar_chart(
                pd.DataFrame.from_dict(
                    pos_count,
                    orient="index",
                    columns=["Count"]
                )
            )

        # ==========================================
        # TAB 3 : LEMMATIZATION
        # ==========================================
        with tab3:

            st.subheader("📚 Lemmatization")

            st.dataframe(
                pd.DataFrame(lemma_data),
                use_container_width=True,
                hide_index=True
            )

            st.info(
                "Lemmatization converts words into their root form."
            )

        # ==========================================
        # TAB 4 : NER
        # ==========================================
        with tab4:

            st.subheader("🧑 Named Entity Recognition")

            if entity_data:

                st.dataframe(
                    pd.DataFrame(entity_data),
                    use_container_width=True,
                    hide_index=True
                )

                st.subheader("Detected Entities")

                cols = st.columns(3)

                for i, ent in enumerate(doc.ents):
                    cols[i % 3].success(
                        f"{ent.text}\n\n({ent.label_})"
                    )

            else:

                st.info("No named entities detected.")

        # ==========================================
        # TAB 5 : ANALYSIS
        # ==========================================
        with tab5:

            st.subheader("🔗 Dependency Parsing")

            st.dataframe(
                pd.DataFrame(dep_data),
                use_container_width=True,
                hide_index=True
            )

            st.subheader("📋 Token Details")

            st.dataframe(
                pd.DataFrame(token_data),
                use_container_width=True,
                hide_index=True
            )

            st.subheader("📊 Word Frequency")

            st.dataframe(
                freq_df,
                use_container_width=True,
                hide_index=True
            )

            if not freq_df.empty:

                chart = (
                    freq_df
                    .set_index("Word")
                    .head(10)
                )

                st.bar_chart(chart)

            st.subheader("📈 Text Statistics")

            c1, c2, c3, c4, c5 = st.columns(5)

            c1.metric(
                "Characters",
                stats["Characters"]
            )

            c2.metric(
                "Words",
                stats["Words"]
            )

            c3.metric(
                "Unique Words",
                stats["Unique Words"]
            )

            c4.metric(
                "Sentences",
                stats["Sentences"]
            )

            c5.metric(
                "Entities",
                stats["Named Entities"]
            )

            with st.expander("📄 View Statistics (JSON)"):

                st.json(stats)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center;'>

<h2>🧠 NLP Pipeline Demo</h2>

Built using <b>Python</b>, <b>Streamlit</b> and <b>spaCy</b>

Explore how Natural Language Processing transforms raw text into structured information.

</div>
""",
    unsafe_allow_html=True
)
