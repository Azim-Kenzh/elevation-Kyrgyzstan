from elevation.conf import data
from typing import Union


def elevation(latitude: float, longitude: float) -> Union[float, None]:
    # Input Validation
    if not (38 <= latitude <= 44) or not (69 <= longitude <= 81):
        raise ValueError(
            'Invalid coordinates: latitude and longitude must be in the range (latitude[38 - 44], longitude[69 - 81)'
        )

    # Selecting the nearest point from the data
    closest_point = data.sel(lat=latitude, lon=longitude, method='nearest')

    # Returning the height of this point
    return closest_point.elevation.values
