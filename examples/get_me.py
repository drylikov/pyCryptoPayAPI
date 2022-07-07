# -*- coding: utf-8 -*-
#
#  pyCryptoPayAPI - get_me example usage.
#  Created by LulzLoL231 at 3/6/22
#
from os import environ
from asyncio import run

from CryptoPayAPI import CryptoPay


TOKEN = environ.get('CRYPTOPAY_API_TOKEN', '')
if not TOKEN:
    print('Use shell argument "CRYPTOPAY_API_TOKEN" for your Crypto Pay API token!')
    exit(1)


async def main():
    cp = CryptoPay(TOKEN)

    app = await cp.get_me()
    print('Application: ', app)


run(main())
