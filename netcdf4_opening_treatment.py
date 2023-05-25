"script pour ouvrir et traiter fichier météo netcdf après conversion sous Python"


import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


Fichier_netcdf = 'prevision_operationelle_AROME/netcdf_AROME_file/weather_netcdf_file_test_4.nc'

# ouverture du fichier grib2. methode trouvée ici : https://github.com/ecmwf/cfgrib
ds = xr.open_dataset(Fichier_netcdf,engine='netcdf4')



CAPE_INS_array = ds.CAPE_INS.to_numpy()              # remplacer la grandeur météo par celle que l'on étudie
latitude_array = ds.latitude.to_numpy()
longitude_array = ds.longitude.to_numpy()


# afficher le array sous forme de graphe pour verifier son contenu


X, Y = np.meshgrid(longitude_array, latitude_array)
#plt.imshow(surface_pressure_array, cmap='viridis',  extent = [np.min(X), np.max(X), np.min(Y), np.max(Y)] ) 
plt.text(1.22, 1.05, "forecast deadline", color='black', fontsize=11)
plt.pcolormesh(X, Y, CAPE_INS_array, cmap='viridis') 

plt.title("CAPE_INS forecast \n by AROME-Europe 1.3 km resolution \n forecast deadline")
plt.xlabel("longitude", fontsize=10)
plt.ylabel("latitude", fontsize=10)



# plt.text(1.22, 1.05, "Surface_Pressure (Pa)", style='normal',
#     verticalalignment='top', horizontalalignment='right',
#     color='black', fontsize=11)

# mettre l'heure d'échéance
cbar = plt.colorbar()
cbar.set_label('CAPE_INS (J/kg)')
plt.savefig("C:/Users/Etienne.FELLMAN/Documents/prevision_operationelle_AROME/plot_prevision_fine_AROME/CAPE_INS_forecast_AROME_Europe.png")
plt.show()









 









