"script pour ouvrir et traiter fichier météo grib sous Python"


import pygrib
import xarray as xr


Fichier_grib = 'prevision_operationelle_AROME/grib_AROME_file/weather_file_test_4.grb2'

# ouverture du fichier grib2. methode trouvée ici : https://github.com/ecmwf/cfgrib
ds = xr.open_dataset(Fichier_grib,engine='cfgrib')

# affiche le contenu du tableau ds pour voire l'acronyme de la grandeur météo
print(ds)

print(type(ds.CAPE_INS) )
DataArray = ds.CAPE_INS

# convertir grib en netcdf ici : https://docs.xarray.dev/en/stable/generated/xarray.DataArray.to_netcdf.html
# pour deployer la donnée météo sur le web avec l'application d'estimation d'inondations, il est
# nécéssaire de faire cette conversion car le format Grib ne peut être transposé en format JSON
DataArray.to_netcdf(path='prevision_operationelle_AROME/netcdf_AROME_file/weather_netcdf_file_test_4.nc',mode = 'w', format = "NETCDF4", engine = "netcdf4", compute = True)





 









