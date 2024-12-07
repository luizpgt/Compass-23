from core.config import settings
from utils import create_response

from services.dynamo import get_all_news
from services.polly import tts_output_directly_on_s3


def handle_news_intent(event):
    try:

        # take from the input the number of news to be read
        slots = event['interpretations'][0]['intent']['slots']
        num_news = int(slots['numeroNoticias']['value']['interpretedValue'])

        print(num_news, type(num_news))

        # get formatted news msg
        news = get_news_fmt(num_news=num_news)

        return create_response(event, news)
    except Exception as e:
        print(str(e))
        return create_response(event, "Ocorreu um erro!")


def get_news_fmt(num_news=5) -> str:
    """
    get and format news from uffs.edu.br

    :return: msg

    usage example:
    get_news_fmt()
    """

    if num_news <= 0:
        return 'Número de notícias inválido!'

    try:
        # scraping from cc.uffs
        news = get_all_news() 

        # Initialize an empty list to store formatted news
        formatted_news = []

        for i in range(min(num_news, len(news))):
            # Format each news item and add it to the list
            formatted_news.append(format_news(news[i]))

            # Add a newline character after every 5th news item
            if (i + 1) % 5 == 0:
                formatted_news.append('\\n')

        # Join all the formatted news items into a single string
        msg = '\n'.join(formatted_news)

        # Add a final message indicating the number of news items returned
        msg += f'\nForam retornadas {min(num_news, len(news))} notícias.'

        return msg
    except Exception as e:
        return f'Ocorreu um erro: {str(e)}'


def format_news(news_item):
    """Helper function to format a single news item."""

    return (
        f'{news_item["titulo"]}... \n'
        f'Publicada em {news_item["data_post"]} \n'
        f'{news_item["texto"].split("  ler mais...")[0]} \n'
        f'Leia a notícia completa em: {news_item["link"]} \n'
        f'Ouça a notícia completa em: {news_item["audio"]} \n\n'
    )


def get_news_audio_url(news_text: str, news_id: str) -> str:
    """
    get news content (body) and returns a s3 link with the tts

    :param news_text: news body
    :param news_id: news id
    :return: s3 object link

    usage example:
    get_news_audio_url("A Universidade Federal da Fronteira Sul (UFFS) está com inscrições abertas.", 123)
    """

    bucket_name = settings.NEWS_BUCKET_NAME
    key = settings.NEWS_FOLDER_NAME + f'{news_id}'
    # tts with polly
    audio_url = tts_output_directly_on_s3(news_text, bucket_name, key)
    
    return audio_url