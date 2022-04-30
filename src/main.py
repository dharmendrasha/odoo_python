#!./venv/bin/python3.8
from odoo import OdooApi
from rich import print
from dotenv import load_dotenv
from os import getenv,  environ, path
from pathlib import Path


def main():
    odoo = OdooApi(
        host=getenv('HOST', 'http://localhost:9000'),
        database=getenv('DATABASE', 'odoo_db'),
        user=getenv('USERNAME', 'dharmendrashah2002@yahoo.com'),
        password=getenv('PASSWORD', '6a31ed372040da085a337db597e393f588785f55')
    )

    # products = odoo.search_read('product.product')
    # print(products)


def loadEnv():
    dotenv_path = str(Path(__file__).parents[1]) + '/.env'
    load_dotenv(dotenv_path=dotenv_path)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    loadEnv()
    main()

