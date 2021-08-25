# Code to generate the word cloud taken from 
# https://towardsdatascience.com/simple-wordcloud-in-python-2ae54a9f58e5


import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

def plot_cloud(wordcloud):
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud) 
    plt.axis("off")
    plt.show()

def generate_cloud(text): 
    wordcloud = WordCloud(
        width = 500, 
        height = 500,
        random_state=1,
        background_color='salmon', 
        colormap='Pastel1',
        collocations=False, 
        stopwords = STOPWORDS
    ).generate(text)

    return wordcloud