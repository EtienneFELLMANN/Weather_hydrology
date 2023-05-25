ce répertoire contient : 

_ requete_MF_AROME.py, un programme python permettant de faire fonctionner l'API de
Météo-France pour retirer de la prévision régionale issue du modèle à maille fine
AROME. on obtient de la donnée sous forme de fichier GRIB2 rangé dans le répertoire grib_AROME_file

_ grib_opening_treatment.py, programme python permettant d'ouvrir le contenu du fichier
grib2 d'AROME en entrée. Le contenu météo de ce dernier est ensuite extrait puis enregistré dans un fichier
NetCDF en sortie. 

_ netcdf4_opening_treatment.py, programme python permettant d'ouvrir le contenu du fichier météo 
NetCDF4 en entrée. génère également un plot 2D du paramètre concerné et de la zone cible pour vérifier 
l'information météo. Ce dernier est rangé dans le répertoire plot_prevision_fine_AROME

_ le répertoire grib_AROME_file qui reçoit chaque fichier rapatrié de l'API de Météo-France
sous format Grib2

_ le répertoire netcdf_AROME_file qui reçoit chaque fichier météo grib convertit en format NetCDF

_ le répertoire plot_prevision_fine_AROME qui reçoit chaque plot 2D généré par le script
netcdf4_opening_treatment.py
