class PCException(Exception):
    pass


class PCServerResponseException(Exception):
    pass


class PCInvalidFormatException(Exception):
    pass


__all__ = ("PCException",
           "PCServerResponseException",
           "PCInvalidFormatException")
