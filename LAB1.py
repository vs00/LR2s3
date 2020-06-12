from math import *
import plotly.graph_objects as go

# Строки
str1 = "Конец"
str2 = "Начало"

# Кортеж
tup = ('работы', 'программы', ' ')
print (str2 + tup[2] + tup[0] + tup[2] + tup[1])

alpha = 0.2
dX = 0.1
dTAU = 0.005
Xmax = 1
TAUmax = 100

# Функции
def fi(x): return 20 + 10 * x

def f1(tau): return 20 + 5 * sin(tau)

def f2(tau): return 30

# x,tau,T
Xarr = []
xi = 0.0
# Циклы
while xi < Xmax:
    Xarr.append(xi)
    xi += dX
TAUarr = []
ti = 0.0
while ti < TAUmax:
    TAUarr.append(ti)
    ti += dTAU

Tarr = []
i = 0
while i < len(TAUarr):
    j = 0
    tmp = []
    while j < len(Xarr):
        tmp.append(j)
        j += 1
    Tarr.append(tmp)
    i += 1
i = 0
while i < len(Xarr):
    Tarr[0][i] = fi(Xarr[i])
    i += 1
xmaxIndex = len(Xarr) - 1
i = 0
while i < len(TAUarr):
    Tarr[i][0] = f1(TAUarr[i])
    Tarr[i][xmaxIndex] = f2(TAUarr[i])
    i += 1
part = (alpha * dTAU) / pow(dX, 2)
j = 0
while j < len(TAUarr) - 1:
    i = 1
    while i < xmaxIndex:
        temp = Tarr[j][i + 1] - 2 * Tarr[j][i] + Tarr[j][i - 1]
        Tarr[j + 1][i] = part * temp + Tarr[j][i]
        i += 1
    j += 1

# Xarr TAUarr Tarr
i = 0
x = []
y = []
z = []
j = 0
while i < len(TAUarr):
    # Условие
    if j == len(Xarr):
        j = 0
    x.append(Xarr[j])
    y.append(TAUarr[i])
    z.append(Tarr[i][j])
    j += 1
    i += 1

# Словарь
fig = go.Figure(data=[go.Surface(z=Tarr, x=Xarr, y=TAUarr)],layout = {
  "showlegend": True,
  "title": {"text": "Zillow Home Value Index for Top 5 States"},
  "xaxis": {
    "rangeslider": {"visible": True},
    "title": {"text": "Year from 1996 to 2017"},
    "zeroline": False
  },
  "yaxis": {
    "title": {"text": "ZHVI BottomTier"},
    "zeroline": False
  }
})
fig.update_layout(title='5 lab_s', autosize=False,
                  width=1300, height=800,
                  margin=dict(l=65, r=50, b=65, t=90),
                  scene=dict(
                      xaxis_title='x',
                      yaxis_title='tau',
                      zaxis_title='T')
                  )
fig.show()
print (str1 + tup[2] + tup[0] + tup[2] + tup[1])