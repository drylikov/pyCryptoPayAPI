# -*- coding: utf-8 -*-
#
#  CryptoPayAPI - API errors.
#  Created by LulzLoL231 at 2/6/22
#
class BaseError(Exception):
    def __init__(self, raw_response: dict, *args: object) -> None:
        super().__init__(*args)
        self.raw_response = raw_response


class UnauthorizedError(BaseError):
    pass


class MethodNotFoundError(BaseError):
    pass


class UnexpectedError(BaseError):
    pass


class ExpiresInInvalidError(BaseError):
    pass
