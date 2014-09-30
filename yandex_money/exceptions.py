from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future.builtins import *

class APIException(Exception):
    pass


class FormatError(APIException):
    def __init__(self):
        super(FormatError, self).__init__()


class ScopeError(APIException):
    def __init__(self):
        super(ScopeError, self).__init__()
        

class TokenError(APIException):
    def __init__(self):
        super(TokenError, self).__init__()
