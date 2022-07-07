# -*- coding: utf-8 -*-
#
#  CryptoPayAPI - types.
#  Created by LulzLoL231 at 2/6/22
#
from enum import Enum
from decimal import Decimal
from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel


class Assets(Enum):
    BTC = 'BTC'
    TON = 'TON'
    ETH = 'ETH'
    USDT = 'USDT'
    USDC = 'USDC'
    BUSD = 'BUSD'

    def __str__(self) -> str:
        return self.value


class PaidButtonNames(Enum):
    VIEW_ITEM = 'viewItem'
    OPEN_CHANNEL = 'openChannel'
    OPEN_BOT = 'openBot'
    CALLBACK = 'callback'

    def __str__(self) -> str:
        return self.value


class InvoiceStatus(Enum):
    ACTIVE = 'active'
    PAID = 'paid'
    EXPIRED = 'expired'

    def __str__(self) -> str:
        return self.value


class Invoice(BaseModel):
    invoice_id: int
    status: InvoiceStatus
    hash: str
    asset: Assets
    amount: Decimal
    pay_url: str
    description: Optional[str]
    created_at: datetime
    allow_comments: bool
    allow_anonymous: bool
    expiration_date: Optional[datetime]
    paid_at: Optional[datetime]
    paid_anonymously: Optional[bool]
    comment: Optional[str]
    hidden_message: Optional[str]
    payload: Optional[str]
    paid_btn_name: Optional[PaidButtonNames]
    paid_btn_url: Optional[str]


class Transfer(BaseModel):
    transfer_id: int
    user_id: int
    asset: Assets
    amount: Decimal
    status: Literal['completed']
    completed_at: datetime
    comment: Optional[str]


class Application(BaseModel):
    app_id: int
    name: str
    payment_processing_bot_username: str


class Balance(BaseModel):
    currency_code: str
    available: Decimal


class ExchangeRate(BaseModel):
    is_valid: bool
    source: str
    target: str
    rate: Decimal


class Currency(BaseModel):
    is_blockchain: bool
    is_stablecoin: bool
    is_fiat: bool
    name: str
    code: str
    url: Optional[str]
    decimals: int
