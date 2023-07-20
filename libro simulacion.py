# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 12:32:21 2023

@author: Anderson
"""

##ejemplo 5.8 libro simulacion 
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotly.offline import plot



##Datos
dX=1000
dY=1000
dZ=75
B=1
c=3.5*10**-6
Kx=0.015
Por=0.18
U=10
Binic=1
Qsc=-150
#COnstruccion del Grid
X_gird=[i*dX for i in range(0,6)]
X_cent=[i*dX+dX/2 for i in range(0,6)]
##Operando las constantes para dT =10
dt=10
tiempos=[dt*i for i in range(0,37)]
M=((5.615*Binic*dt)/(dX*dY*dZ*Por*c))
T=((1.127*dY*dZ*Kx)/(U*B*dX))
P=[6000,6000,6000,6000,6000]
grids=["Grid 1","Grid 2","Grid 3","Grid 4", "Grid 5"]
df=pd.DataFrame(columns=grids)
df.loc[0]=P[0:5]
tiem=[]
def itera(a,b,c,d,e):
    return [(1-M*T)*a+M*T*b,
            M*T*a+(1-2*M*T)*b+M*T*c,
            M*T*b+(1-2*M*T)*c+M*T*d,
            M*T*c+(1-2*M*T)*d+M*T*e-150*M,
            (1-M*T)*e+M*T*d]
i=1

while i<=360/dt:
    j,k,l,m,n=P
    Pnu=itera(j,k,l,m,n)
    df.loc[i]=Pnu[0:5]
    P=Pnu
    i=i+1
print(df) 

for z in range(1,6):
    
    plt.plot(tiempos,df[f'{"Grid "}{z}'])
    plt.legend(loc="lower left",labels=grids)
plt.title("P Vs Tiempo")
plt.xlabel("Tiempo(dias)")
plt.ylabel("Presion(psi)")

df2=pd.DataFrame(columns=["Presión","Grid","Tiempo"])
df2["Presión"]=df.to_numpy().flatten(order="F")
df2["Grid"]=sorted(grids*len(tiempos))
df2["Tiempo"]=len(grids)*tiempos                          
print(df2)
fig=px.line(df2,x="Tiempo",y="Presión",color="Grid")


fig=px.scatter(df2,x="Grid",y="Presión",animation_frame="Tiempo",color="Grid",size="Tiempo",size_max=30,range_y=[4000,6100])

from dash import Dash, html, dash_table, dcc
app = Dash(__name__)
app.layout = html.Div([
    html.Div(children='BUM BUM, Mira mi grafico'),
    dcc.Graph(figure=fig)
])
if __name__ == '__main__':
    app.run(debug=False)



