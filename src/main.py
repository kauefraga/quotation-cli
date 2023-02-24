import httpx
from rich import print, print_json
from rich.panel import Panel

from settings import settings


def main():
  print('[b green][>-<] HIII!')
  print('[>-<] Searching for the current value of the dolar...')

  data = httpx.get(f'{settings.API_URL}/usd-brl,eur-brl').json()

  print_json(data=data['USDBRL'])
  print_json(data=data['EURBRL'])


if __name__ == '__main__':
  main()
