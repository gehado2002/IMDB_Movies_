# Title using Streamlit native elements
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
    st.markdown("# 🎬🍿 IMDB Movies Explorer")
    st.markdown("#### Explore and analyze the top 1000 IMDB movies")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Add some styling
    st.markdown(
        """
        <style>
        div[data-testid="stMarkdownContainer"] h1 {
            color: #ff7e5f;
            text-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        }
        div[data-testid="stMarkdownContainer"] h3 {
            color: #86A8E7;
        }
        </style>
        """, unsafe_allow_html=True
    )
