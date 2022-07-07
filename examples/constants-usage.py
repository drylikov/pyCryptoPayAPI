# -*- coding: utf-8 -*-
#
#  pyCryptoPayAPI - Constants example usage.
#  Created by LulzLoL231 at 3/6/22
#
from os import environ
from asyncio import run

from CryptoPayAPI import CryptoPay
from CryptoPayAPI.types import Assets, PaidButtonNames, InvoiceStatus


TOKEN = environ.get('CRYPTOPAY_API_TOKEN', '')
if not TOKEN:
    print('Use shell argument "CRYPTOPAY_API_TOKEN" for your Crypto Pay API token!')
    exit(1)


async def main():
    cp = CryptoPay(TOKEN)

    new_invoice = await cp.create_invoice(
        Assets.USDT, 5.25,
        description='Example page for $5.25!',
        paid_btn_name=PaidButtonNames.VIEW_ITEM,
        paid_btn_url='https://example.com'
    )
    print('Your a new Invoice: ', new_invoice)
    invoices = await cp.get_invoices(
        status=InvoiceStatus.ACTIVE
    )
    print(f'You have {len(invoices)} active invoices!')


run(main())
