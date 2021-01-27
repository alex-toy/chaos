import streamlit as st
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from transformers import AutoModelWithLMHead, AutoTokenizer
from generate_linkedin_post_from_blog_article.application.main import summarizer
import generate_linkedin_post_from_blog_article.config.config as cf


def main():
    st.title("Yotta Summarizer")
    activity1 = ["Summarize"]
    choice = st.sidebar.selectbox("Select Function",activity1)

    if choice == 'Summarize':
        st.subheader("votre logiciel de résumé automatique de textes")
        raw_text = st.text_area("Entrez votre texte ici")
        summary_choice = st.selectbox("Choisissez votre modèle préféré",["finetuned mbart","finetuned t5", "no finetuned model"])
        #you can choice the no finetuned model in the config.py file(NAME_MODEL). it must be "t5" ou "mbart"
    if st.button("Summarize"):
        if summary_choice == "t5":
            summary_result= summarizer(raw_text, cf.MODEL_NAME_T5)
        elif summary_choice == "mbart":
            summary_result= summarizer(raw_text, cf.MODEL_NAME_MBART)
        elif summary_choice == "no finetuned model":
            summary_result= summarizer(raw_text,"no finetuned model" )
        st.write(summary_result)

if __name__ == '__main__':
    main()
