# spectroscpy
## A club project of HORIZON IITM
### ESO data
Python code to calculate the temperature of a star. The python file uses fits file of a star's spectran and fit it with blackbody raidaition curve. Fitting is done by least squares mean methon used from scipy module. 
temp.py has the python code and is specific to the stars from ESO library, fits file for different types of stars can be found on https://www.eso.org/sci/facilities/paranal/decommissioned/isaac/tools/lib.html.
Comacluster(1).py is a python file for color color diagram, the csv file used in the code is named as comacluster.csv.
### SDSS data
SDSS uses different format of fits file for a star's spectra. To calsulate temperature of any star in the cluster use sdss_temp.py file. sdss_temp.py file can be used to eso fits file as well but its not true the other way around. To downlaod sdss fits file use https://skyserver.sdss.org/dr10/en/tools/chart/navi.aspx to navigate star and then click on "Explore" tab, and then go to "Interactive spectra" and then "Downlaod fits file". SDSS does not provide spectra for all the stars, it can be chacked by marking "objects with spectra" in the left side of the webpage.
