import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")
st.title("Modern AI System Analysis Dashboard")
st.write("Analyze LLM responses, prompt engineering outputs, and AI capability metrics interactively!")

# --- Load output data files ---
results = pd.read_csv('ai_analysis_results.csv', index_col=0)
capabilities = pd.read_csv('ai_capabilities_assessment.csv', index_col=0)

# --- Tabs for analysis ---
tab1, tab2, tab3 = st.tabs(['Response Metrics Table', 'AI Capability Comparison', 'Visualizations'])

with tab1:
    st.subheader("LLM Response Analysis Table")
    st.dataframe(results.style.background_gradient(axis=None, cmap='YlGnBu'), use_container_width=True)

with tab2:
    st.subheader("Capabilities Assessment Table")
    st.dataframe(capabilities.style.background_gradient(axis=None, cmap='OrRd'), use_container_width=True)

with tab3:
    st.subheader("Automated Response Visualizations")

    # --- Word Count
    fig1, ax1 = plt.subplots(figsize=(8,4))
    ax1.bar(results.index, results['word_count'], color='deepskyblue')
    ax1.set_title('Word Count Comparison')
    ax1.set_ylabel('Number of Words')
    st.pyplot(fig1)

    # --- Readability
    fig2, ax2 = plt.subplots(figsize=(8,4))
    ax2.bar(results.index, results['readability'], color='coral')
    ax2.set_title('Readability Comparison')
    ax2.set_ylabel('Flesch Score')
    st.pyplot(fig2)

    # --- Vocabulary Richness
    fig3, ax3 = plt.subplots(figsize=(8,4))
    ax3.bar(results.index, results['vocabulary_richness'], color='mediumseagreen')
    ax3.set_title('Vocabulary Richness')
    ax3.set_ylabel('Unique Words / Total Words')
    st.pyplot(fig3)

    # --- Sentiment
    fig4, ax4 = plt.subplots(figsize=(8,4))
    ax4.bar(results.index, results['sentiment'], color='orchid')
    ax4.set_title('Sentiment Score')
    ax4.set_ylabel('Polarity (0: Negative, 1: Positive)')
    st.pyplot(fig4)

    # --- Scatter plot: Vocabulary Richness vs Readability
    fig5, ax5 = plt.subplots(figsize=(8,4))
    sizes = results['word_count'] * 4
    ax5.scatter(results['vocabulary_richness'], results['readability'], s=sizes, c=sizes, cmap='cool', alpha=0.7)
    for i, label in enumerate(results.index):
        ax5.annotate(label, (results['vocabulary_richness'][i], results['readability'][i]), fontsize=9)
    ax5.set_xlabel('Vocabulary Richness')
    ax5.set_ylabel('Readability Score')
    ax5.set_title('Vocabulary vs Readability (Bubble Size = Word Count)')
    st.pyplot(fig5)

    # --- Bar plot: Sentences per response
    fig6, ax6 = plt.subplots(figsize=(8,4))
    ax6.bar(results.index, results['sentence_count'], color='slateblue')
    ax6.set_title('Number of Sentences per Response')
    ax6.set_ylabel('Sentence Count')
    st.pyplot(fig6)

    # --- Capability Assessment (Grouped Bar Chart)
    st.subheader("AI Capability Comparison")
    fig7, ax7 = plt.subplots(figsize=(10,5))
    metrics = capabilities.index
    bar_width = 0.18
    x = np.arange(len(metrics))
    colors = ['#4e79a7','#f28e2c','#e15759','#76b7b2']
    for i, col in enumerate(capabilities.columns):
        ax7.bar(x + i*bar_width, capabilities[col], bar_width, label=col, color=colors[i%len(colors)])
    ax7.set_xlabel('Metrics')
    ax7.set_ylabel('Score (out of 10)')
    ax7.set_title('AI Capabilities Grouped Comparison')
    ax7.set_xticks(x + 1.5*bar_width)
    ax7.set_xticklabels(metrics)
    ax7.legend()
    st.pyplot(fig7)

st.markdown("---")
st.info("Note: First run project3_complete.py to generate the analysis results. All visualizations above are fully interactive and neatly arranged for exploration!")

