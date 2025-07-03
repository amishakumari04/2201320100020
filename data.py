from datetime import datetime, timedelta

# In-memory data stores
urls = {}  # key: shortcode, value: dict
clicks = {}  # key: shortcode, value: list of click dicts

def create_short_url(shortcode, original_url, validity_minutes):
    expiry = datetime.utcnow() + timedelta(minutes=validity_minutes)
    urls[shortcode] = {
        "original_url": original_url,
        "created_at": datetime.utcnow(),
        "expiry": expiry,
        "click_count": 0
    }
    clicks[shortcode] = []
    return urls[shortcode]
