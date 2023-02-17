import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import io
import base64

def generate_wordcloud(text):
    # Generate the word cloud
    word_frequencies = {}
    for word in text.split():
        word_frequencies[word] = word_frequencies.get(word, 0) + 1
    wordcloud = WordCloud(width=800, height=800, background_color='white', min_font_size=10).generate_from_frequencies(word_frequencies)

    # Save the plot to a buffer
    buf = io.BytesIO()
    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.savefig(buf, format='png')
    plt.close()
    
    # Encode the plot to base64
    image_base64 = base64.b64encode(buf.getbuffer()).decode('ascii')
    return image_base64

st.set_page_config(page_title='Word Cloud Example')

st.title('Word Cloud Example')

text = st.text_area('Enter text:')
if text:
    image = generate_wordcloud(text)
    st.image('data:image/png;base64,{}'.format(image))
