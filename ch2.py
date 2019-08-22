import dash
#from astroquery.jplhorizons import Horizons
from datetime import datetime, timedelta
from datetime import datetime
from dateutil import tz
import plotly
from plotly.graph_objs import Scatter, Layout
import plotly.graph_objs as go
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import math
from textwrap import dedent as d
import json
import plotly.tools as tls
from numpy import *
#t = datetime.today().strftime('%Y-%b-%d %H:%M:%S')
#from_zone = tz.tzlocal()
#to_zone = tz.tzutc()
utc = datetime.utcnow().strftime('%Y-%b-%d %H:%M:%S')
ut = utc[:-4]+'0:00.0000'
k = ut

ch2x = []
ch2y = []
ch2z = []
chvx = []
chvy = []
chvz = []
date = []

mx = []
my = []
mz = []
mvx = []
mvy = []
mvz = []
date1 = []


with open('chandrayaan_2_geo_3.json','r') as json_file:
    c_data = json.load(json_file)

with open('moon15.json','r') as json_file:
    moon_data = json.load(json_file)

with open('lunar5.json','r') as json_file:
    l_data = json.load(json_file)



#slide = len(c_data)

for data in c_data:
    date.append(data['date'][5:])
    ch2x.append(data['cx']*149597870.691)    
    ch2y.append(data['cy']*149597870.691)
    ch2z.append(data['cz']*149597870.691)
    chvx.append(data['cvx']*149597870.691/86400)
    chvy.append(data['cvy']*149597870.691/86400)
    chvz.append(data['cvz']*149597870.691/86400)

for data in moon_data:
    date1.append(data['date'][5:])
    mx.append(data['cx']*149597870.691)
    my.append(data['cy']*149597870.691)
    mz.append(data['cz']*149597870.691)
    mvx.append(data['cvx']*149597870.691/86400)
    mvy.append(data['cvy']*149597870.691/86400)
    mvz.append(data['cvz']*149597870.691/86400)

date2 = []
lux = []
luy = []
luz = []
lvx = []
lvy = []
lvz = []
for i in range(0,len(l_data)):
    date2.append(l_data[i]['date'][5:])
    lux.append(l_data[i]['cx']*149597870.691)
    luy.append(l_data[i]['cy']*149597870.691)
    luz.append(l_data[i]['cz']*149597870.691)
    lvx.append(l_data[i]['cvx']*149597870.691/86400)
    lvy.append(l_data[i]['cvy']*149597870.691/86400)
    lvz.append(l_data[i]['cvz']*149597870.691/86400)


#xx = 1737*outer(cos(theta),sin(phi))
#yy = 1737*outer(sin(theta),sin(phi))
#zz = 1737*outer(ones(100),cos(phi))

    
#utc times
#2019-Jul-24 00:00:00.0000
burn_1 = '2019-Jul-24 09:20:00.0000'
burn_2 = '2019-Jul-25 19:30:00.0000'
burn_3 = '2019-Jul-29 09:40:00.0000'
burn_4 = '2019-Aug-02 09:50:00.0000'
burn_5 = '2019-Aug-06 09:30:00.0000'
burn_6 = '2019-Aug-13 20:50:00.0000'

burn1 = date.index(burn_1)
burn2 = date.index(burn_2)
burn3 = date.index(burn_3)
burn4 = date.index(burn_4)
burn5 = date.index(burn_5)
burn6 = date.index(burn_6)

try:
    ind = date.index(k)
    ind1 = date1.index(k)
    diff = ind1 - ind
except ValueError as err:
    print('data available upto 30.08.2019')
    print(err)
    ind = len(date)-1
    ind1 = len(date)-1
    diff = ind1 - ind

def time1():
    try:
        utc1 = datetime.utcnow().strftime('%Y-%b-%d %H:%M:%S')
        ut1 = utc1[:-4]+'0:00.0000'
        up = date.index(ut1)
        #moon_location(up)
        #up = 3800
    except ValueError as err:
        print(err)
        print('data available upto 30.08.2019')
        up = len(date)-1
    return up

def time2():
    try:
        utc1 = datetime.utcnow().strftime('%Y-%b-%d %H:%M:%S')
        ut1 = utc1[:-4]+'0:00.0000'
        up = date2.index(ut1)
    except ValueError as err:
        print(err)
        print('data available upto 30.08.2019')
        up = len(date2)-1
    #up = 500
    return up



theta = linspace(0,2*pi,100)
phi = linspace(0,pi,100)
r1 = 6371 #earth - Center radii    : 6371 x 6371 x 6371 km     {Equator, meridian, pole}
#earth shape  
x = r1*outer(cos(theta),sin(phi))
y = r1*outer(sin(theta),sin(phi))
z = r1*outer(ones(100),cos(phi)) 
r2 = 1737.4 #moon - Center radii    : 1737.4 x 1737.4 x 1737.4 km     {Equator, meridian, pole} 
#moon shape
xxx = r2*outer(cos(theta),sin(phi))
yyy = r2*outer(sin(theta),sin(phi))
zzz = r2*outer(ones(100),cos(phi))


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    dcc.Graph(id='graph',style={'height':'110vh','color':'black'},figure={
            'data': [
                go.Scatter3d(
                )],'layout': go.Layout(
                xaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                yaxis={'showgrid':False,'zeroline': False,'showticklabels':False},
                hovermode='closest' )
				 }
	),html.Button('Geocentric view', id='btn-1',n_clicks_timestamp=0),html.Button('Moon(body center) view', id='btn-2', n_clicks_timestamp=0),html.Button('current_position', id='btn-4', n_clicks_timestamp=0),html.Button('end_position', id='btn-5', n_clicks_timestamp=0),
	
dcc.Markdown(d("""
              
            Last updated on 22.08.2019 | data collected from jpl horizons system| For Geocentric view, data available from 22.07.2019 to 30.08.2019 | For moon(body-center)view, data available upto 30.08.2019 | To view the information, keep the mouse pointer on the satellite.
             
            """))
          
])

@app.callback(Output('graph', 'figure'),[Input('btn-1', 'n_clicks_timestamp'),Input('btn-2', 'n_clicks_timestamp'),Input('btn-4', 'n_clicks_timestamp'),Input('btn-5', 'n_clicks_timestamp')])
def displayClick(btn1,btn2,btn4,btn5):

    value = time1()
    value1 = time2()
    if int(btn4) > int(btn2) and int(btn4) > int(btn1) and int(btn4) > int(btn5):
        print('btn4')
        value = time1()
        value1 = time2()

    elif int(btn5) > int(btn4) and int(btn5) > int(btn2) and int(btn5) > int(btn1):
        print('btn5')
        value = len(date)-1
        value1 = len(date2)-1
        
    #moon current location
    x2 = mx[value+diff]
    y2 = my[value+diff]
    z2 = mz[value+diff]
    xx = x2 + r2*outer(cos(theta),sin(phi))
    yy = y2 + r2*outer(sin(theta),sin(phi))
    zz = z2 + r2*outer(ones(100),cos(phi))


    dat = date[int(value)]
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.strptime(dat[:-5], '%Y-%b-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    #ind = date.index(k)
    #ind1 = date1.index(k)
    cx = ch2x[value]
    cy = ch2y[value]
    cz = ch2z[value]
    
    cvx = chvx[value]
    cvy = chvy[value]
    cvz = chvz[value]
   
    cr = math.sqrt(float(cx)*float(cx) + float(cy)*float(cy)+ float(cz)*float(cz))
    vl = math.sqrt(float(cvx)*float(cvx) + float(cvy)*float(cvy)+ float(cvz)*float(cvz))
    
    lx = mx[int(value)+diff]
    ly = my[int(value)+diff]
    lz = mz[int(value)+diff]

    mvxx = mvx[int(value)+diff]
    mvyy = mvy[int(value)+diff]
    mvzz = mvz[int(value)+diff]
    
    ax = cx - lx
    ay = cy - ly
    az = cz - lz

    vxx = cvx - mvxx
    vyy = cvy - mvyy
    vzz = cvz - mvzz

    ux = lux[value1]
    uy = luy[value1]
    uz = luz[value1]
    print (ux)
    print (uy)
    print (uz)
    ur = math.sqrt(float(ux)*float(ux) + float(uy)*float(uy) + float(uz)*float(uz))

    ualti = ur - 1731 # moon 

    vvx = lvx[value1]
    vvy = lvy[value1]
    vvz = lvz[value1]
    
    print ("vx",vvx)
    print ("vy",vvy)
    print ("vz",vvz)
    
    vv = math.sqrt(float(vvx)*float(vvx) + float(vvy)*float(vvy) + float(vvz)*float(vvz))

    mr = math.sqrt(float(ax)*float(ax) + float(ay)*float(ay) + float(az)*float(az))
    malti = mr - 1731 #moon
    mvl = math.sqrt(float(vxx)*float(vxx) + float(vyy)*float(vyy) + float(vzz)*float(vzz))
    
    #value11 = time1()
    #value = date.index(value11)
    burn_1 = '2019-Jul-24 09:20:00.0000'
    burn_2 = '2019-Jul-25 19:30:00.0000'    
    burn_3 = '2019-Jul-29 09:40:00.0000'
    burn_4 = '2019-Aug-02 09:50:00.0000'
    burn_5 = '2019-Aug-06 09:30:00.0000'
    burn_6 = '2019-Aug-13 20:50:00.0000'
    #burn_66 ='2019-Aug-13 20:51:00.0000'
   
    burn1 = date.index(burn_1)  
    burn2 = date.index(burn_2)
    burn3 = date.index(burn_3)
    burn4 = date.index(burn_4)
    burn5 = date.index(burn_5)
    burn6 = date.index(burn_6)
    
    #trace for chandrayaan2 orbit
    trace1 = go.Scatter3d(x=ch2x[:value],
                    y=ch2y[:value],
                    z=ch2z[:value],
                    mode = 'lines',
                    line=dict(width=1,color='orange'),
                    text='chandrayaan2 orbit',
                    name = 'Chandrayaan2 orbit',
                    hoverinfo='text')
    #trace for chandryaan2 current location
    trace2 = go.Scatter3d(x=[ch2x[value]],
                    y=[ch2y[value]],
                    z=[ch2z[value]],
                    mode = 'markers',
                    marker=dict(size=1,color='red'),
                    #line=dict(width=3,color='orange'),
                    text = str(central)[:-6]+' GMT+05:30'+' IST<br>'+'Chandrayaan2 <br>'+'Distance btw earth & ch2: '+str(cr)+' km<br>'+ 'Distance btw moon & ch2: '+str(mr)+' km<br>'+'Altitude wrt to moon: '+str(malti)+'km<br>'+'velocity wrt Earth:'+str(vl)+' km/s<br>velocity wrt to moon:'+str(mvl)+' km/s<br>',
                    name = 'Chandrayaan2',
                    hoverinfo='text')
    #trace for moon orbit
    trace3 = go.Scatter3d(x=mx[1600:len(date)],
                    y=my[1600:len(date)],
                    z=mz[1600:len(date)],
                    mode = 'lines',
                    line=dict(width=1,color='white'),
                    text='Moon orbit',
                    name = 'Moon orbit',
                    hoverinfo='text')
    #trace for burn1
    trace_b1 = go.Scatter3d(x=[ch2x[burn1]],
                    y=[ch2y[burn1]],
                    z=[ch2z[burn1]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn1',
                    name = 'burn1',
                    hoverinfo='text')
    #trace for burn2
    trace_b2 = go.Scatter3d(x=[ch2x[burn2]],
                    y=[ch2y[burn2]],
                    z=[ch2z[burn2]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn2',
                    name = 'burn2',
                    hoverinfo='text')
    #trace for burn3
    trace_b3 = go.Scatter3d(x=[ch2x[burn3]],
                    y=[ch2y[burn3]],
                    z=[ch2z[burn3]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn3',
                    name = 'burn3',
                    hoverinfo='text')
    #trace for burn4
    trace_b4 = go.Scatter3d(x=[ch2x[burn4]],
                    y=[ch2y[burn4]],
                    z=[ch2z[burn4]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn4',
                    name = 'burn4',
                    hoverinfo='text')
    #trace for burn5
    trace_b5 = go.Scatter3d(x=[ch2x[burn5]],
                    y=[ch2y[burn5]],
                    z=[ch2z[burn5]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn5',
                    name = 'burn5',
                    hoverinfo='text')
    #trace for burn6
    trace_b6 = go.Scatter3d(x=[ch2x[burn6]],
                    y=[ch2y[burn6]],
                    z=[ch2z[burn6]],
                    mode = 'markers',
                    marker=dict(size=2,color='red'),
                    text='burn6[TRANS LUNAR INSERTION]',
                    name = 'burn6[TLI]',
                    hoverinfo='text')

    
    #trace for earth 3d shape
    trace33 = go.Surface(x=x, y=y, z=z,showscale=False,colorscale = 'blugrn',text='earth',hoverinfo='text')
    
    #trace for moon current location
    trace4 = go.Scatter3d(x=[mx[value+diff]],
                    y=[my[value+diff]],
                    z=[mz[value+diff]],
                    mode = 'markers',
                    marker=dict(size=5,color='white'),
                    text='Moon',
                    name = 'Moon',
                    hoverinfo='text')
    #trace for moon 3d shape
    trace_hidden = go.Surface(x=xx, y=yy, z=zz,showscale=False,text='moon',colorscale = 'gray',hoverinfo='text')
    #trace for chandrayaan2 current location in lunar view
    trace5 = go.Scatter3d(x=lux[1000:value1],
                    y=luy[1000:value1],
                    z=luz[1000:value1],
                    mode = 'lines',
                    line=dict(width=3,color='orange'),
                    text='chandrayaan2 orbit',
                    name = 'Chandrayaan2 orbit',
                    hoverinfo='text')
    #trace for moon 3d shape
    trace6 = go.Surface(x=xxx, y=yyy, z=zzz,showscale=False,colorscale = 'gray',text='moon',hoverinfo='text')
    #trace for chandrayaan2 current location in lunar view
    trace7 = go.Scatter3d(x= [lux[value1]],
                    y=[luy[value1]],
                    z=[luz[value1]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text= str(central)[:-6]+' GMT+05:30'+' IST<br>'+'Chandrayaan2 <br>'+ 'Distance btw moon & ch2: '+str(ur)+' km<br>'+'velocity wrt to moon:'+str(vv)+' km/s<br>'+'Altitude wrt to moon: '+str(ualti)+'km<br>',
                    name = 'Chandrayaan2 ',
                    hoverinfo='text')

    layout = go.Layout(scene = dict(
                    camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=2.5, y=0.1, z=0.1)
),
                    xaxis = dict(
                         backgroundcolor="black",
                         gridcolor="black",
                         color = 'black',
                         showbackground=True,showticklabels=False,
                         zerolinecolor="orange"),
                    yaxis = dict(
                        backgroundcolor="black",
                        gridcolor="black", color = 'black',
                        showbackground=True,showticklabels=False,
                        zerolinecolor="orange"),
                    zaxis = dict(
                        backgroundcolor="black",
                        gridcolor="black", color = 'black',
                        showbackground=True,showticklabels=False,
                        zerolinecolor="orange",),),scene_aspectmode='data',
                        margin=dict(r=0, l=100, b=80, t=11),paper_bgcolor='black',
    plot_bgcolor='black')    

    if int(btn1) > int(btn2) and int(btn1) > int(btn4) and int(btn1) > int(btn5):
        data = [trace1,trace2,trace3,trace33,trace_b1,trace_b2,trace_b3,trace_b4,trace_b5,trace_b6,trace_hidden]
        print('btn1')
    elif int(btn2) > int(btn1) :
        data = [trace5,trace6,trace7]
        print('btn2')
   
    else:
       data = [trace1,trace2,trace3,trace33,trace_b1,trace_b2,trace_b3,trace_b4,trace_b5,trace_b6,trace_hidden]
        
    fig = go.Figure(data=data,layout = layout)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

