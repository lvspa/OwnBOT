import praw
import logging
import time

# Lista de URLs permitidas
white_list = [
    "https://www.pichau.com.br/",
    "https://www.kabum.com.br/",
    "https://www.mercadolivre.com.br/",
    "https://www.aliexpress.com/",
    "https://shopee.com.br/",
    "https://www.casasbahia.com.br/",
    "https://www.pontofrio.com.br/",
    "https://store.steampowered.com/",
    "https://www.magazineluiza.com.br/",
    "https://www.youtube.com/"
]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

reddit = praw.Reddit(
    client_id='ViNUpkeiRAn_4t6vgS6Dpw',
    client_secret='wLfqSclEib0Nmp2_ty-GdycbJWoVow',
    username='The_Own_Supervision',
    password='di60ztpud3',
    user_agent='OwnSupervision'
)

subreddit = reddit.subreddit('computadores')

while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            words = comment.body.split()
            found = False

            for word in words:
                if word.startswith('http') and not any(word.startswith(allowed_url) for allowed_url in white_list):
                    bot_comment = comment.reply("uuh uuh ATENÇÃO! [Removido pelo bot de supervisão]")
                    logger.info(f"Respondido ao comentário: {comment.id}")
                    comment.delete()
                    logger.info(f"Comentário excluído: {comment.id} por violação de regras.")
                    comment.mod.lock()
                    found = True
                    break

            if found:
                break

            time.sleep(1)

    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")

    time.sleep(4)
