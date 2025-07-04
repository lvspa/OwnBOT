import praw
import logging
import time
import re

# Lista de URLs permitidas
white_list = [
    "https://www.pichau.com.br/",
    "https://www.kabum.com.br/",
    "https://www.aliexpress.com/",
    "https://shopee.com.br/",
    "https://www.casasbahia.com.br/",
    "https://www.pontofrio.com.br/",
    "https://store.steampowered.com/",
    "https://www.magazineluiza.com.br/",
    "https://www.youtube.com/",
    "https://www.terabyteshop.com.br/",
    "https://patoloco.com.br",
    "https://www.americanas.com.br/",
    "https://www.amazon.com.br/",
    "https://www.nuuvem.com/br-pt/",
    "https://meupc.net/",
    "https://www.reddit.com/",
    "https://www.microsoft.com/pt-br"
]

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

reddit = praw.Reddit(
    client_id='',
    client_secret='',
    username='',
    password='',
    user_agent=''
)

subreddit = reddit.subreddit('computadores')

email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')


def coments_user(comment):
    words = comment.body.split()

    for word in words:
        if word.startswith('http') and not any(word.startswith(allowed_url) for allowed_url in white_list):
            comment.reply("uuh uuh ATENÇÃO! [Removido pelo bot de supervisão]")
            logger.info(f"Respondido ao comentário: {comment.id}")
            comment.delete()
            logger.info(f"Comentário excluído: {comment.id} por violação de regras.")
            comment.mod.lock()
            return True

    if re.search(email_pattern, comment.body):
        comment.reply("uuh uuh ATENÇÃO! [Removido pelo bot de supervisão]")
        logger.info(f"Respondido ao comentário: {comment.id}")
        comment.delete()
        logger.info(f"Comentário excluído: {comment.id} por violação de regras.")
        comment.mod.lock()
        return True

    return False


def subs_user(submission):

    if submission.saved:
        return False

    title_words = submission.title.split()
    selftext_words = submission.selftext.split()

    for word in title_words + selftext_words:
        if word.startswith('http') and not any(word.startswith(allowed_url) for allowed_url in white_list):
            submission.reply("uuh uuh ATENÇÃO! [Removido pelo bot de supervisão]")
            logger.info(f"Respondido ao post: {submission.id}")
            submission.save()
            submission.delete()
            logger.info(f"Post excluído: {submission.id} por violação de regras.")
            submission.mod.lock()
            return True

        if re.search(email_pattern, submission.selftext) or re.search(email_pattern, submission.title):
            submission.reply("uuh uuh ATENÇÃO! [Removido pelo bot de supervisão]")
            logger.info(f"Respondido ao post: {submission.id}")
            submission.mod.remove()
            logger.info(f"Post removido: {submission.id} por violação de regras.")
            submission.mod.lock()
            return True
    return False


while True:
    try:
        for comment in subreddit.stream.comments(skip_existing=True):
            if coments_user(comment):
                continue

        for submission in subreddit.stream.submissions(skip_existing=True):
            if subs_user(submission):
               continue

        time.sleep(2)

    except Exception as e:
        logger.error(f"Ocorreu um erro: {e}")
        time.sleep(4)

