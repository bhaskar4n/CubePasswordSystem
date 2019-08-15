# horizons
horizons 
<br>observatory location table codes: https://en.wikipedia.org/wiki/List_of_observatory_codes</br>
500 -> Geocentric </br>
-152 -> chandrayaan2</br>
301 -> moon</br>
for more information refer https://ssd.jpl.nasa.gov/?horizons</br>
for more information about the horizons class refer</br> https://astroquery.readthedocs.io/en/latest/api/astroquery.jplhorizons.HorizonsClass.html#astroquery.jplhorizons.HorizonsClass


requirements: astroquery,dash,plotly</br>
astroquery - collect data from jpl horizons system</br>
dash & plotly - for graphing...</br>
data available from 23.07.2019 to 21.08.2019

moon11.json -> contains moon vectors data(X,Y,Z, VX,VY,VZ)</br>
chandrayaan2.json -> contains chandrayaan2 vectors data(X,Y,Z, VX,VY,VZ)</br>
g.py -> used to collect data from jpl horizons system. 
ch2.py -> main script

<img src = "https://github.com/bhaskar4n/horizons/blob/master/c3d.png"/>

<img src = "https://github.com/bhaskar4n/horizons/blob/master/c3d1.png"/>





