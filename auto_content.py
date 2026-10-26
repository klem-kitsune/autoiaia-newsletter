import os
import 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def fetch_ai_news():
    urls = [
        "https://news.google.com/rss/search?q=Artificial+Intelligence+AI&hl=es&gl=ES&ceid=ES:es"
    ]
    posts = []
    for url in urls:
        feed = feedparser.parse(url)
        for entry in feed.entries[:4]:
            posts.append(f"<h3><a href='{entry.link}'>{entry.title}</a></h3><p>{entry.get('summary', '')}</p><br>")
    return "".join(posts)

def send_to_substack(content):
    sender_email = os.environ.get("SMTP_USER")
    sender_password = os.environ.get("SMTP_PASS")
    substack_email = os.environ.get("SUBSTACK_EMAIL")
    
    if not sender_email or not sender_password or not substack_email:
        print("Aviso: Faltan las variables de entorno de correo configuradas en GitHub Secrets.")
        return

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "AutoIAia: Tendencias de Inteligencia Artificial del Día"
    msg["From"] = sender_email
    msg["To"] = substack_email

    html_content = f"<html><body><h2>Tu boletín automático diario</h2>{content}</body></html>"
    msg.attach(MIMEText(html_content, "html"))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, substack_email, msg.as_string())
        print("¡Boletín enviado y publicado en Substack con éxito!")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")

if __name__ == "__main__":
    content = fetch_ai_news()
    if content:
        send_to_substack(content)
    else:
        print("No se encontraron noticias nuevas.")
