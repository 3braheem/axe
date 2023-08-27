import click
from app import application

@click.group()
def cli():
    pass

@cli.command()
@click.option('--api-key', envvar='API_KEY')
@click.option('-q', '--query', type=str, help='The query you want a response for.', default="Explain how you can help me.")
def chatgpt(query, api_key):
    print(application.query_chatgpt(query, api_key))

if __name__ == '__main__':
    chatgpt()
