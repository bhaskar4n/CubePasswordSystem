from astroquery.jplhorizons import Horizons
import json
#f= open('b.json','a')

obj = Horizons(id='chandrayaan', location='500',epochs={'start':'2019-07-23', 'stop':'2019-08-11',
                       'step':'10m'},id_type='majorbody')

obj1 = Horizons(id='301', location='500',epochs={'start':'2019-07-01', 'stop':'2019-08-20',
                       'step':'10m'},id_type='majorbody')
vec = obj.vectors()
vec1 = obj1.vectors()

chand = []
moon = []
#print vec
s = ['datetime_str','x','y','z','vx','vy','vz']
#s1 = ['datetime_str','x','y','z','vx','vy','vz']

print 'processing....'
for i in range(len(vec)):
    d=dict(date = vec[s][i][0], cx = vec[s][i][1], cy = vec[s][i][2],cz = vec[s][i][3],cvx = vec[s][i][4],cvy = vec[s][i][5],cvz = vec[s][i][6])
    chand.append(d)
     #js = json.dumps(d)

for i in range(len(vec1)):
    d=dict(date = vec1[s][i][0], mx = vec1[s][i][1], my = vec1[s][i][2],mz = vec1[s][i][3],mvx = vec1[s][i][4],mvy = vec1[s][i][5],mvz = vec1[s][i][6])
    moon.append(d)
     #js = json.dumps(d)


print 'creating json...'
with open('ch2.json','a') as json_file:
    json.dump(chand,json_file)



with open('luna.json','a') as json_file:
    json.dump(moon,json_file)

