#!/usr/bin/env python

"""A Right Ascension (RA) adjustment utility.
"""
from datetime import datetime, timedelta, timezone
from typing import List

# Length of a day
_ONE_DAY: timedelta = timedelta(hours=24)

# Ask the user the RA coordinate they want to locate (the 'target')...
_RA_TARGET = input("RA target coordinate (HhMm): ")
assert _RA_TARGET
assert _RA_TARGET.endswith('m')
assert 'h' in _RA_TARGET
# Check the value looks sensible..
# (i.e. represents a clock)
_PARTS: List[str] = _RA_TARGET.split('h')
assert len(_PARTS) == 2
_TARGET_H: int = int(_PARTS[0])
assert 0 <= _TARGET_H < 24
_TARGET_M: int = int(_PARTS[1][:-1])
assert 0 <= _TARGET_M < 60
# Create a timedelta object to represent the target
_RA_TARGET = timedelta(hours=_TARGET_H, minutes=_TARGET_M)

# Add the current time of day (UTC) to the user's target.
# That aligns the target with the telescope's midnight calibration
# (remembering to deal with RA coordinates that may be 24h or larger).
_UTC_NOW: datetime = datetime.now(timezone.utc)
_MIDNIGHT_OFFSET: timedelta = timedelta(hours=_UTC_NOW.hour,
                                        minutes=_UTC_NOW.minute)

_ADJUSTED_RA: timedelta = _RA_TARGET + _MIDNIGHT_OFFSET
if _ADJUSTED_RA >= _ONE_DAY:
    _ADJUSTED_RA -= _ONE_DAY

# Print the current time (for reference) and the adjusted coordinate.
# The user just needs to rotate their telescope RA axis to this value.
# The '[:-3]' removes the redundant seconds value from the timedelta object.
_LOCAL_TIME: str = str(_MIDNIGHT_OFFSET)[:-3]
_RA_PARTS: List[str] = str(_ADJUSTED_RA)[:-3].split(':')
_RA: str = f'{_RA_PARTS[0]}h{_RA_PARTS[1]}m'
print(f'Local time (UTC): {_LOCAL_TIME}')
print(f'Adjusted RA coordinate: {_RA}')
