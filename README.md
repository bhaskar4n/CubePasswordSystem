# horizons
horizons 
<br>#observatory location table codes: https://en.wikipedia.org/wiki/List_of_observatory_codes</br>
#218 -> Hyderabad Observatory for observer location</br>
#@301 -> center of the Moon for observer location</br>
#-153 -> chandrayaan2 id number</br>
#for more information refer https://ssd.jpl.nasa.gov/?horizons</br>
#for more information about the horizons class refer</br> https://astroquery.readthedocs.io/en/latest/api/astroquery.jplhorizons.HorizonsClass.html#astroquery.jplhorizons.HorizonsClass
```enter target body id number(integer): -153
enter observer location id number(integer): 218
please wait...
...................................................................................................................
Jul-22 22:48
distance wrt observer:  0.00015925939332 A.U /  23825.2052407 km
distance wrt sun     : 1.01615487802 A.U /  152016769.752 km
1-way lighttime	     :  0.001325 min
velocity wrt observer:  3.38578 km/s
velocity wrt sun     :  32.75735 km/s
...................................................................................................................
Jul-22 22:49
distance wrt observer:  0.00016024943589 A.U /  23973.3156091 km
distance wrt sun     : 1.01615504865 A.U /  152016795.278 km
1-way lighttime	     :  0.001333 min
velocity wrt observer:  3.36419 km/s
velocity wrt sun     :  32.73906 km/s
...................................................................................................................
<TableColumns names=('targetname','datetime_str','datetime_jd','solar_presence','flags','RA','DEC','RA_app','DEC_app','RA_rate','DEC_rate','AZ','EL','AZ_rate','EL_rate','sat_X','sat_Y','sat_PANG','siderealtime','airmass','magextinct','V','surfbright','illumination','illum_defect','sat_sep','sat_vis','ang_width','PDObsLon','PDObsLat','PDSunLon','PDSunLat','SubSol_ang','SubSol_dist','NPole_ang','NPole_dist','EclLon','EclLat','r','r_rate','delta','delta_rate','lighttime','vel_sun','vel_obs','elong','elongFlag','alpha','lunar_elong','lunar_illum','sat_alpha','sunTargetPA','velocityPA','OrbPlaneAng','constellation','TDB-UT','ObsEclLon','ObsEclLat','NPole_RA','NPole_DEC','GlxLon','GlxLat','solartime','earth_lighttime','RA_3sigma','DEC_3sigma','SMAA_3sigma','SMIA_3sigma','Theta_3sigma','Area_3sigma','RSS_3sigma','r_3sigma','r_rate_3sigma','SBand_3sigma','XBand_3sigma','DoppDelay_3sigma','true_anom','hour_angle','alpha_true','PABLon','PABLat')>

python horizons.py delta delta_rate r r_rate vel_obs vel_sun lighttime
enter target body id number(integer): -153
enter observer location id number(integer): 218
enter id type: majorbody
start date:2019-07-22 22:51
end date:2019-07-22 22:52
enter time span: 1m
please wait...
...................................................................................................................
   datetime_str        delta       delta_rate       r         r_rate  vel_obs vel_sun  lighttime
       ---               AU          km / s         AU        km / s   km / s  km / s     min   
----------------- ---------------- ---------- ------------- --------- ------- -------- ---------
2019-Jul-22 22:51 0.00016221327005  2.4348763 1.01615536334  0.370566 3.32176 32.70281  0.001349
2019-Jul-22 22:52 0.00016318708497  2.4214349 1.01615550767 0.3491803 3.30091 32.68484  0.001357





