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


with open('chandrayaan2.json','r') as json_file:
    c_data = json.load(json_file)

with open('moon11.json','r') as json_file:
    moon_data = json.load(json_file)


slide = len(c_data)

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
    mx.append(data['mx']*149597870.691)
    my.append(data['my']*149597870.691)
    mz.append(data['mz']*149597870.691)
    mvx.append(data['mvx']*149597870.691/86400)
    mvy.append(data['mvy']*149597870.691/86400)
    mvz.append(data['mvz']*149597870.691/86400)
    
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


ind = date.index(k)

chxx = []
chyy = []
chzz = []

ind1 = date1.index(k)


diff = ind1 - ind


mxx = []
myy = []
mzz = []
launch = 1

def time1():
    utc1 = datetime.utcnow().strftime('%Y-%b-%d %H:%M:%S')
    ut1 = utc1[:-4]+'0:00.0000'
    up = date.index(ut1)
    return up


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'marginLeft': 510, 'marginRight': 10, 'marginTop': -110, 'marginBottom': 0,
        'backgroundColor':'#FAD7A0',
        'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'
    }
}


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
	),html.Button('current_position', id='btn-1',n_clicks_timestamp=0),html.Button('End_position', id='btn-2', n_clicks_timestamp=0),

	
dcc.Markdown(d("""
                shows data with 10 min interval\n
            data available from 23.07.2019 to 21.08.2019\n
            """)),
            html.Pre(id='click-data', style=styles['pre'])

])



@app.callback(
    Output('click-data', 'children'),
    [Input('btn-1', 'n_clicks_timestamp'),Input('btn-2', 'n_clicks_timestamp')])
def display_click_data(btn1,btn2):
    #value11 = time1()
    #value = date.index(value11)
    #print(n_clicks)
    value = 0
    value = time1()
    if int(btn1) > int(btn2):
        value = time1()
    elif int(btn2) > int(btn1):
        value = len(date)-1

    dat = date[int(value)]
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.strptime(dat[:-5], '%Y-%b-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    ind = date.index(k)
    ind1 = date1.index(k)
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

    mr = math.sqrt(float(ax)*float(ax) + float(ay)*float(ay) + float(az)*float(az))
    mvl = math.sqrt(float(vxx)*float(vxx) + float(vyy)*float(vyy) + float(vzz)*float(vzz))
    
    
    return str(central)[:-6]+' GMT+05:30'+' IST\n'+'Chandrayaan2 \n'+'Distance btw earth & ch2: '+str(cr)+' km\n'+ 'Distance btw moon & ch2: '+str(mr)+' km\n'+'velocity wrt Earth:'+str(vl)+' km/s\nvelocity wrt to moon:'+str(mvl)+' km/s\n'

@app.callback(Output('graph', 'figure'),[Input('btn-1', 'n_clicks_timestamp'),Input('btn-2', 'n_clicks_timestamp')])
def displayClick(btn1,btn2):


    value = 0
    value = time1()
    if int(btn1) > int(btn2):
        value = time1()
    elif int(btn2) > int (btn1):
        value = len(date)-1
    dat = date[int(value)]
    from_zone = tz.tzutc()
    to_zone = tz.tzlocal()
    utc = datetime.strptime(dat[:-5], '%Y-%b-%d %H:%M:%S')
    utc = utc.replace(tzinfo=from_zone)
    central = utc.astimezone(to_zone)
    ind = date.index(k)
    ind1 = date1.index(k)
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

    mr = math.sqrt(float(ax)*float(ax) + float(ay)*float(ay) + float(az)*float(az))
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
    #burn66 = date.index(burn_66)

    #tlix = []
    #tliy = []

    #for i in range(burn6,burn66):
     #   tlix.append(ch2x[i])
      #  tliy.append(ch2y[i])

    return {'data':[
                go.Scatter3d(
                    x=ch2x[:value],
                    y=ch2y[:value],
                    z=ch2z[:value],
                    mode = 'lines',
                    line=dict(width=3,color='orange'),
                    text='chandrayaan2 orbit',
                    name = 'Chandrayaan2 orbit',
                    hoverinfo='text'
                ),


                    go.Scatter3d(
                    x=[0],
                    y=[0],
                    z=[0],
                    mode = 'markers',
                    marker=dict(size=5,color='green'),
                    text='Earth',
                    name = 'Earth',
                    hoverinfo='text'),


                    go.Scatter3d(
                    x=mx,
                    y=my,
                    z=mz,
                    mode = 'lines',
                    line=dict(width=5,color='grey'),
                    text='Moon orbit',
                    name = 'Moon orbit',
                    hoverinfo='text'),

                    go.Scatter3d(
                    x=[ch2x[value]],
                    y=[ch2y[value]],
                    z=[ch2z[value]],
                    mode = 'markers',
                    marker=dict(size=5,color='red',symbol = 'circle'),
                    text=str(central)[:-6]+' GMT+05:30'+' IST<br>'+'Chandrayaan2<br>'+'Distance btw earth & ch2: '+str(cr)[:-7]+' km<br>'+ 'Distance btw moon & ch2: '+str(mr)[:-7]+' km<br>'+'velocity wrt Earth: '+str(vl)[:-12]+' km/s<br>velocity wrt to moon: '+str(mvl)[:-12]+' km/s<br>',
                    name = 'Chandrayaan2',
                    hoverinfo='text'),

                    go.Scatter3d(
                    x=[mx[value+diff]],
                    y=[my[value+diff]],
                    z=[mz[value+diff]],
                    mode = 'markers',
                    marker=dict(size=7,color='white'),
                    text='moon',
                    name = 'moon',
                    hoverinfo='text'),

                    go.Scatter3d(
                    x=[ch2x[burn1]],
                    y=[ch2y[burn1]],
                    z=[ch2z[burn1]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='burn1',
                    name = 'burn1',
                    hoverinfo='text'),

                    go.Scatter3d(
                    x=[ch2x[burn2]],
                    y=[ch2y[burn2]],
                    z=[ch2z[burn2]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='burn2',
                    name = 'burn2',
                    hoverinfo='text'),


                    go.Scatter3d(
                    x=[ch2x[burn3]],
                    y=[ch2y[burn3]],
                    z=[ch2z[burn3]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='burn3',
                    name = 'burn3',
                    hoverinfo='text'),


                    go.Scatter3d(
                    x=[ch2x[burn4]],
                    y=[ch2y[burn4]],
                    z=[ch2z[burn4]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='burn4',
                    name = 'burn4',
                    hoverinfo='text'),



                    go.Scatter3d(
                    x=[ch2x[burn5]],
                    y=[ch2y[burn5]],
                    z=[ch2z[burn5]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='burn5',
                    name = 'burn5',
                    hoverinfo='text'),


                    go.Scatter3d(
                    x=[ch2x[burn6]],
                    y=[ch2y[burn6]],
                    z=[ch2z[burn6]],
                    mode = 'markers',
                    marker=dict(size=3,color='red'),
                    text='Trans Lunar Insertion',
                    name = 'Trans Lunar Insertion',
                    hoverinfo='text'),


				],'layout': go.Layout(scene = dict(
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
                        zerolinecolor="orange",),),scene_aspectmode='manual',
                  scene_aspectratio=dict(x=1.3, y=1.3, z=1.3),margin=dict(r=0, l=100, b=80, t=11),paper_bgcolor='black',
    plot_bgcolor='black')

				}
		
if __name__ == '__main__':
    app.run_server(debug=True,threaded=True,port=8050)

