''' Cabeçalho 
####    Autor: Gabriel Tomé Silveira    ####
####    contato: silveira.tomeg@usp.br  ####
####    github: @DeadSecs32             ####
####    data: 23/08/2020                ####
####    Marrie Currie Vestibulares      ####
####    Título: Refração Simulator      ####

Liscença: Copyright (c) 2021 Gabriel Tomé Silveira
 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:
 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.
 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
'''

import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.widgets import Slider, Button, RadioButtons

fig = plt.figure()
ax = plt.axes(aspect = "equal")

#criando os sliders 
axcolor = 'lightgoldenrodyellow'
axa = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
axne = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axnd = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor = axcolor)
sa = Slider(axa, 'ângulo', 0, 90, valinit=0)
sne = Slider(axne, 'refração esquerdo', 1, 2.42, valinit=1)
snd = Slider(axnd, 'refração direito', 1, 2.42, valinit=1)
#update 
def update(val): 
    ax.cla()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1,1)
    a = sa.val
    ne = sne.val
    nd = snd.val 
    td = 2*np.tan(a*np.pi/180)
    te = (4-2*np.sin(a*np.pi/180))*np.tan(a*np.pi/180)-2*np.cos(a*np.pi/180)
    #criando a fronteira 
    espd = plt.Rectangle((td, -2), 2, 100, fill=1, lw=2, angle=a, alpha=0.8*(nd-1)/1.42)
    espe = plt.Rectangle((te,-4),2,180, fill=1, lw=2, angle=a, alpha=0.8*(ne-1)/1.42, color ='green')
    ax.add_patch(espd)
    ax.add_patch(espe)
    fig.canvas.draw_idle()
    #vetor laser
    vlaser = [0, 1]
    vesp = [-np.cos(a*np.pi/180),np.sin(a*np.pi/180)]
    ai = np.arcsin(np.inner(vlaser,vesp))
    #criando Laser
    if ne*np.sin(ai)/nd < 1:
        ar = np.arcsin(ne*np.sin(ai)/nd)
        x, y = np.array([[-2, 0, 2*np.cos(ar-ai)], [0, 0, -2*np.sin(ar-ai)]])
    else:
        x, y = np.array([[-2, 0, -2*np.cos(ai*2)], [0,0,-2*np.sin(ai*2)]])
    line = plt.Line2D(x, y, lw=2., alpha=1.0, color="red")
    ax.add_line(line)



update(0)
sa.on_changed(update)
snd.on_changed(update)
sne.on_changed(update)

plt.subplots_adjust(bottom = 0.25)
plt.show()
