from django.shortcuts import render

# Create your views here.
from .models import Mention
from .tasks import fetch_mock_mentions
from datetime import datetime, timedelta

def dashboard(request):
    if Mention.objects.count() == 0:
        fetch_mock_mentions()

    mentions = Mention.objects.all().order_by('-created_at')
    sentiment_count = {
        "Positive": Mention.objects.filter(sentiment="Positive").count(),
        "Neutral": Mention.objects.filter(sentiment="Neutral").count(),
        "Negative": Mention.objects.filter(sentiment="Negative").count(),
    }

    time_threshold = datetime.now() - timedelta(minutes=30)
    negative_recent = Mention.objects.filter(sentiment="Negative", created_at__gte=time_threshold).count()
    alert = None
    if negative_recent > 2:
        alert = f"⚠️ Negative mentions spike detected! ({negative_recent} in last 30 min)"

    return render(request, "dashboard.html", {
        "mentions": mentions,
        "sentiment_count": sentiment_count,
        "alert": alert
    })