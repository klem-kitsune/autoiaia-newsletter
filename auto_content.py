import feedparser
from datetime import datetime

# Fuentes de tendencia en IA y automatización autónoma
TRENDING_FEEDS = [
    "https://news.ycombinator.com/rss",
    "https://www.artificialintelligence-news.com/feed/"
]

def run_autonomous_pipeline():
    print(f"=== AUTOIAIA PIPELINE ACTIVE: {datetime.now().strftime('%Y-%m-%d %H:%M')} ===")
    curated_content = []
    
    for feed_url in TRENDING_FEEDS:
        parsed_feed = feedparser.parse(feed_url)
        for entry in parsed_feed.entries[:2]: # Top 2 por fuente
            curated_content.append({
                "headline": entry.title,
                "url": entry.link
            })
            
    print("\n[ESTADO] Contenido viral extraído con éxito. Listo para distribución.")
    for idx, item in enumerate(curated_content[:4], 1):
        print(f"{idx}. {item['headline']}\n   -> URL: {item['url']}")

if __name__ == "__main__":
    run_autonomous_pipeline()
