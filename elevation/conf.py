import xarray as xr
import pkg_resources

data_file = pkg_resources.resource_filename('elevation', 'KG_ELEVATION/elevation_Kyrgyzstan_2023.nc')
data = xr.open_dataset(data_file)
