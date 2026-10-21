"""Streamlit wrapper for the cold weather concreting guide.

Renders the sibling index.html (a self-contained static page) full width.
Run locally with: streamlit run app.py
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Concreting in Cold Weather: A Small Jobs Guide", layout="wide")

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

components.html(html, height=6000, scrolling=True)
