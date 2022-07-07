# -*- coding: utf-8 -*-
#
#  pyCryptoPayAPI - Transfer example usage.
#  Created by LulzLoL231 at 3/6/22
#
from os import environ
from asyncio import run

from CryptoPayAPI import CryptoPay
from CryptoPayAPI.types import Assets


TOKEN = environ.get('CRYPTOPAY_API_TOKEN', '')
if not TOKEN:
    print('Use shell argument "CRYPTOPAY_API_TOKEN" for your Crypto Pay API token!')
    exit(1)


async def main():
    cp = CryptoPay(TOKEN, testnet=True)

    if input('You want to donate me 3 USDT? -> ').lower() in ['n', 'no', '-']:
        print('Okay :(')
        exit()

    transfer = cp.transfer(
        265300852, Assets.USDT, 3.0, 'pCBA226ghd', comment='donate'
    )

    print('Transfer: ', transfer)


run(main())
