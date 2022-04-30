#!./venv/bin/python3.8
from odoo import OdooApi
from rich import print


def main():
    odoo = OdooApi(
        host='http://localhost:9000',
        database='odoo_db',
        user='dharmendrashah2002@yahoo.com',
        password='6a31ed372040da085a337db597e393f588785f55'
    )

    products = odoo.search_read('product.product')
    print(products)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

