class UnknownTimeZoneError(KeyError): ...
class InvalidTimeError(Exception): ...
class AmbiguousTimeError(InvalidTimeError): ...
class NonExistentTimeError(InvalidTimeError): ...
