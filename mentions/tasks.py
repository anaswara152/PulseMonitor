from .models import Mention
from textblob import TextBlob
import random
from datetime import datetime, timedelta

def fetch_mock_mentions():
    """Simulate fetching mentions from APIs."""
    sample_mentions = [
        {"platform": "Twitter", "text": "Love the new product launch!"},
        {"platform": "Reddit", "text": "The price is too high for this brand."},
        {"platform": "News", "text": "Brand X releases a new marketing campaign."},
        {"platform": "Blog", "text": "Customer service was excellent."},
        {"platform": "Twitter", "text": "Terrible experience with the product."},
    ]

    topics = ["Product Launch", "Pricing", "Campaign", "Customer Service", "General"]

    for item in sample_mentions:
        content = item['text']
        sentiment = get_sentiment(content)
        topic = random.choice(topics)
        Mention.objects.create(
            platform=item['platform'],
            content=content,
            sentiment=sentiment,
            topic=topic,
            created_at=datetime.now() - timedelta(minutes=random.randint(0, 120))
        )

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"
