import matplotlib.pyplot as plt
from textblob import TextBlob

# Sample data: list of sentences
sentences = [
    "I love programming!",
    "This is a bad experience.",
    "I feel fantastic.",
    "This is the worst product I have ever seen.",
    "Python is awesome!",
    "I'm so happy with your service.",
    "I am not satisfied with the product.",
]

# Analyze the sentiment of each sentence
sentiments = [TextBlob(sentence).sentiment.polarity for sentence in sentences]


# Classify sentiment as positive, neutral, or negative
def classify_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'


sentiment_labels = [classify_sentiment(polarity) for polarity in sentiments]

# Count the number of each sentiment
sentiment_counts = {'Positive': sentiment_labels.count('Positive'),
                    'Neutral': sentiment_labels.count('Neutral'),
                    'Negative': sentiment_labels.count('Negative')}

# Plot the results
fig, ax = plt.subplots()
ax.bar(sentiment_counts.keys(), sentiment_counts.values(), color=['green', 'blue', 'red'])
ax.set_xlabel('Sentiment')
ax.set_ylabel('Count')
ax.set_title('Sentiment Analysis Results')
plt.show()
