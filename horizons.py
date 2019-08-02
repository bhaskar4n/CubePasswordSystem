from astroquery.jplhorizons import Horizons
from time import gmtime, strftime
import sys
from datetime import datetime, timedelta
from datetime import datetime
from dateutil import tz

#t = datetime.today() + timedelta(seconds=60)
#print t

#b = str(t)[:-10]
#d = datetime.today() - timedelta(seconds=60)
#a = str(d)[:-10]

#print 'a',a
#print 'b',b


from_zone = tz.tzlocal()
to_zone = tz.tzutc()


utc = datetime.utcnow() + timedelta(seconds=60)

b = str(utc)[:-10]
utcd = datetime.utcnow() - timedelta(seconds=60)
a = str(utcd)[:-10]

print 'current date:',datetime.today()

def stock():
	
	#target_body = raw_input('enter target body id number(integer): ')
	#observer_location = raw_input('enter observer location id number(integer): ')
	#id_type = raw_input('enter id type: ')
	print "please wait..."
	#print '...................................................................................................................'
	obj = Horizons(id='chandrayaan',location='500',epochs={'start':a,'stop':b,'step':'1m'},id_type='majorbody')
	obj1 = Horizons(id='chandrayaan',location='@301',epochs={'start':a,'stop':b,'step':'1m'},id_type='majorbody')
	eph = obj.ephemerides()
	eph1 = obj1.ephemerides()

	s = ['datetime_str','delta','r','lighttime','vel_obs','vel_sun']

	#for i in range(len(eph)):
	#print eph[s][0][0]
	i = 2
	#print eph[s][i][0][5:]
	print 'distance wrt earth:',eph[s][i][1],'A.U / ',eph[s][i][1]*149597870.691,'km \n'  
		#print 'distance wrt observer: ',eph[s][i][1]*1.496e+8,'km'
		#print 'distance wrt moon     :',eph1[s][i][2] ,'A.U / ',eph1[s][i][2] *1.496e+8,'km'  
		#print 'distance wrt sun     :',eph[s][i][2] *1.496e+8,'km' 
	print '1-way lighttime wrt to earth	 : ',eph[s][i][3],'min \n' 
	print 'velocity wrt earth: ',eph[s][i][4],'km/s \n' 
		#print 'velocity wrt moon     : ',eph1[s][i][5],'km/s'
    #print '...................................................................................................................'

	#for i in range(len(eph1)):
		#print eph[s][0][0]
	#print eph1[s][i][0][5:]
	print 'distance wrt moon:',eph1[s][i][1],'A.U / ',eph1[s][i][1]*149597870.691,'km \n'  
		#print 'distance wrt observer: ',eph[s][i][1]*1.496e+8,'km'
		#print 'distance wrt moon     :',eph1[s][i][2] ,'A.U / ',eph1[s][i][2] *1.496e+8,'km'  
		#print 'distance wrt sun     :',eph[s][i][2] *1.496e+8,'km' 
	print '1-way lighttime wrt to moon:',eph1[s][i][3],'min \n' 
	print 'velocity wrt moon:',eph1[s][i][4],'km/s \n' 
		#print 'velocity wrt moon     : ',eph1[s][i][5],'km/s'
	#print '...................................................................................................................'
#

def custom():
	target_body = raw_input('enter target body id number(integer): ')
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
