from elevation.conf import data

def elevation(latitude, longitude):
    closest_point = data.sel(lat=latitude, lon=longitude, method='nearest')
    result_elevation = closest_point.elevation.values
    return result_elevation
