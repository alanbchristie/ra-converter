#!/usr/bin/env python

"""A Right Ascension (RA) adjustment utility.
"""
from datetime import datetime, timedelta
from typing import List

# Length of a day
_ONE_DAY: timedelta = timedelta(hours=24)
# Approximate daily change of RA calibration
_FOUR_MINUTES: timedelta = timedelta(minutes=4)

# Ask the user how old the calibration is (assume 0)...
_RA_AGE_DAYS: int = 0
_RA_AGE = input("Days since RA calibration (days) [0]: ")
if _RA_AGE:
    _RA_AGE_DAYS + int(_RA_AGE)

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

# Add the current time of day (and any daily adjustment) to the user's target.
# That aligns the target with the telescope's midnight calibration
# (remembering to deal with RA coordinates that may be 24h or larger).
_NOW: datetime = datetime.now()
_MIDNIGHT_OFFSET: timedelta = timedelta(hours=_NOW.hour, minutes=_NOW.minute)
_AGE_ADJUSTMENT: timedelta = _RA_AGE_DAYS * _FOUR_MINUTES

_ADJUSTED_RA: timedelta = _RA_TARGET + _MIDNIGHT_OFFSET + _AGE_ADJUSTMENT
if _ADJUSTED_RA >= _ONE_DAY:
    _ADJUSTED_RA -= _ONE_DAY

# Print the current time (for reference), age adjustment
# and the adjusted coordinate.
# The user just needs to rotate their telescope RA axis to this new value.
# The '[:-3]' removes the redundant seconds value from the timedelta object.
_LOCAL_TIME: str = str(_MIDNIGHT_OFFSET)[:-3]
_ADJUSTMENT: str = str(_AGE_ADJUSTMENT)[:-3]
_RA_PARTS: List[str] = str(_ADJUSTED_RA)[:-3].split(':')
_RA: str = f'{_RA_PARTS[0]}h{_RA_PARTS[1]}m'
print('---')
print(f'Local time (hh:mm): {_LOCAL_TIME}')
print(f'Age compensation (hh:mm): {_ADJUSTMENT}')
print(f'Adjusted RA coordinate: {_RA}')
