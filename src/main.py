import httpx
from enum import Enum
from rich import print, print_json
from rich.panel import Panel

from settings import settings


class Icon(Enum):
  PLUS = '[green][[/green]+[green]][/green]'
  MINUS = '[red][[/red]-[red]][/red]'
  INTERROGATIVE = '[yellow][[/yellow]?[yellow]][/yellow]'


def main():
  print(f'[b green]{Icon.PLUS.value} Welcome!')
  print(f'{Icon.INTERROGATIVE.value} Searching for the current value of the dolar...')

  data = httpx.get(f'{settings.API_URL}/usd-brl,eur-brl').json()

  print_json(data=data['USDBRL'])
  print_json(data=data['EURBRL'])


if __name__ == '__main__':
  main()
