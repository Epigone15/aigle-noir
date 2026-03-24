import feedparser
from datetime import datetime
import os

# RSS feeds for each category
FEEDS = {
    "monde": ["http://www.lemonde.fr/rss/une.xml"],
    "technologie": ["https://www.numerama.com/feed/"],
    "economie": ["https://www.lesechos.fr/rss.xml"],
    "france": ["https://www.francetvinfo.fr/titres.rss"]
}

# Function to generate a summary from the entry
def generate_summary(entry):
    title = entry.title if hasattr(entry, 'title') else "No title"
    author = entry.author if hasattr(entry, 'author') else "the source"
    return f"D'après {author}, {title.split(',')[0]}..."

# Function to fetch news from RSS feeds
def fetch_news(category):
    articles = []
    for feed_url in FEEDS[category]:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries[:3]:
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.get('published', 'No date'),
                "summary": generate_summary(entry)
            })
    return articles

# Function to update HTML with new articles
def update_html(articles, category):
    html_path = os.path.join(os.getcwd(), f"{category}.html")  # Chemin absolu depuis la racine
    print(f"Updating file at: {html_path}")  # Debug
    with open(html_path, 'r', encoding='utf-8') as file:
        content = file.read()

    articles_html = "\n".join([
        f'<div class="article-card"><h2>{article["title"]}</h2>'
        f'<p>{article["summary"]}</p>'
        f'<p class="article-date">Publié le: {article["published"]}</p>'
        f'<p><a href="{article["link"]}">Lire la suite</a></p></div>'
        for article in articles
    ])

    updated_content = content.replace(
        '<!-- Articles will be inserted here by the Python script -->',
        articles_html
    )

    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

if __name__ == "__main__":
    for category in FEEDS:
        articles = fetch_news(category)
        update_html(articles, category)