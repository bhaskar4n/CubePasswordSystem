#observatory location table codes: https://en.wikipedia.org/wiki/List_of_observatory_codes
#218 -> Hyderabad Observatory for observer location
#@301 -> center of the Moon for observer location
#-153 -> chandrayaan2 id number
#for more information refer https://ssd.jpl.nasa.gov/?horizons
#for more information about the horizons class refer https://astroquery.readthedocs.io/en/latest/api/astroquery.jplhorizons.HorizonsClass.html#astroquery.jplhorizons.HorizonsClass

#created by b45k4r

from astroquery.jplhorizons import Horizons
from time import gmtime, strftime
import sys
from datetime import datetime, timedelta
t = datetime.today()
b = str(t)[:-10]
d = datetime.today() - timedelta(seconds=60)
a = str(d)[:-10]

def stock():
	
	target_body = raw_input('enter target body name(string) or id number(integer): ')
	observer_location = raw_input('enter observer location id number(integer): ')
	#id_type = raw_input('enter id type: ')
	print "please wait..."
	print '...................................................................................................................'
	obj = Horizons(id=target_body,location=observer_location,epochs={'start':a,'stop':b,'step':'1m'},id_type='majorbody')
	eph = obj.ephemerides()

	s = ['datetime_str','delta','r','lighttime','vel_obs','vel_sun']

	for i in range(len(eph)):
		#print eph[s][0][0]
		print eph[s][i][0][5:]
		print 'distance wrt observer: ',eph[s][i][1],'A.U / ',eph[s][i][1]*1.496e+8,'km'  
		#print 'distance wrt observer: ',eph[s][i][1]*1.496e+8,'km'
		print 'distance wrt sun     :',eph[s][i][2] ,'A.U / ',eph[s][i][2] *1.496e+8,'km'  
		#print 'distance wrt sun     :',eph[s][i][2] *1.496e+8,'km' 
		print '1-way lighttime	     : ',eph[s][i][3],'min' 
		print 'velocity wrt observer: ',eph[s][i][4],'km/s' 
		print 'velocity wrt sun     : ',eph[s][i][5],'km/s'
		print '...................................................................................................................'

	print(eph.columns)

def custom():
	target_body = raw_input('enter target body name(string) or id number(integer): ')
	observer_location = raw_input('enter observer location id number(integer): ')
	id_type = raw_input('enter id type: ')
	a = raw_input('start date:')
	b = raw_input('end date:')
	#t = raw_input('enter table settings: ')
	time = raw_input('enter time span: ')
	print "please wait..."
	s = ['datetime_str']
	for i in range(len(sys.argv)-1):
		s.append(sys.argv[i+1])
	print '...................................................................................................................'
	obj = Horizons(id=target_body,location=observer_location,epochs={'start':a,'stop':b,'step': time},id_type=id_type)
	eph = obj.ephemerides()

	print eph[s]

if len(sys.argv)>1:
	custom()
else:
	stock()

