from typing import IO, Union

from pytz.tzinfo import StaticTzInfo, DstTzInfo

def build_tzinfo(zone: str, fp: IO) -> Union[StaticTzInfo, DstTzInfo]: ...
