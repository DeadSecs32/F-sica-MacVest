''' Cabeçalho 
####    Autor: Gabriel Tomé Silveira    ####
####    contato: silveira.tomeg@usp.br  ####
####    github: @DeadSecs32             ####
####    data: 09/08/2020                ####
####    Marrie Currie Vestibulares      ####
####    Título: Reflexão Simulator      ####

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
from matplotlib.widgets import Slider



class DraggableRectangle:
    '''draggable rectangle with the animation blit techniques; see
       http://www.scipy.org/Cookbook/Matplotlib/Animations
    '''
    lock = None  # only one can be animated at a time

    def __init__(self, rect):
        self.rect = rect
        self.press = None
        self.background = None

    def connect(self):
        'connect to all the events we need'
        self.cidpress = self.rect.figure.canvas.mpl_connect(
            'button_press_event', self.on_press)
        self.cidrelease = self.rect.figure.canvas.mpl_connect(
            'button_release_event', self.on_release)
        self.cidmotion = self.rect.figure.canvas.mpl_connect(
            'motion_notify_event', self.on_motion)

    def on_press(self, event):
        '''on button press we will see if the
           mouse is over us and store some data'''
        if event.inaxes != self.rect.axes:
            return
        if DraggableRectangle.lock is not None:
            return
        contains, attrd = self.rect.contains(event)
        if not contains:
            return
        print('event contains', self.rect.xy)
        x0, y0 = self.rect.xy
        self.press = x0, y0, event.xdata, event.ydata
        DraggableRectangle.lock = self

        # draw everything but the selected rectangle and store the pixel buffer
        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        self.rect.set_animated(True)
        canvas.draw()
        self.background = canvas.copy_from_bbox(self.rect.axes.bbox)

        # now redraw just the rectangle
        axes.draw_artist(self.rect)

        # and blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_motion(self, event):
        'on motion we will move the rect if the mouse is over us'
        if DraggableRectangle.lock is not self:
            return
        if event.inaxes != self.rect.axes:
            return
        x0, y0, xpress, ypress = self.press
        dx = event.xdata - xpress
        dy = event.ydata - ypress
        self.rect.set_x(x0+dx)
        self.rect.set_y(y0+dy)

        canvas = self.rect.figure.canvas
        axes = self.rect.axes
        # restore the background region
        canvas.restore_region(self.background)

        # redraw just the current rectangle
        axes.draw_artist(self.rect)

        # blit just the redrawn area
        canvas.blit(axes.bbox)

    def on_release(self, event):
        'on release we reset the press data'
        if DraggableRectangle.lock is not self:
            return

        self.press = None
        DraggableRectangle.lock = None

        # turn off the rect animation property and reset the background
        self.rect.set_animated(False)
        self.background = None

        # redraw the full figure
        self.rect.figure.canvas.draw()

        update(0)  # para atualizar o laser depois de mover o retângulo

    def disconnect(self):
        'disconnect all the stored connection ids'
        self.rect.figure.canvas.mpl_disconnect(self.cidpress)
        self.rect.figure.canvas.mpl_disconnect(self.cidrelease)
        self.rect.figure.canvas.mpl_disconnect(self.cidmotion)


fig = plt.figure()
ax = plt.axes(aspect='equal')

# Criando Sliders
axcolor = 'lightgoldenrodyellow'
axae = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axam = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
sae = Slider(axae, 'ângulo', 0, 360, valinit=0)
sam = Slider(axam, 'laser', 0, 360, valinit=0)

Le = 1  # largura do espelho
He = 0.05  # altura do espelho
Lm = 0.2  # largura da máquina
Hm = 0.05  # altura da máquina

xe0 = -0.5  # posição x inicial do espelho
ye0 = -0.5  # posição y inicial do espelho
xm0 = -0.825  # posição x inicial da máquina
ym0 = 0.645  # posição y inicial da máquina

# Criando o espelho
esp = plt.Rectangle((xe0, ye0), Le, He, fill=1, lw=2, angle=0)

# Criando a máquina
maq = plt.Rectangle((xm0, ym0), Lm, Hm, fill=1, angle=0, color="gray")


def update(val):

    global maq, drmaq, esp, dresp  # para poder atualizar os objetos

    ax.cla()
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    ae = sae.val
    am = -sam.val

    # Atualizando o espelho
    xy = esp.get_xy()  # obtém a posição do objeto
    xe0, ye0 = xy  # redefine as variáveis da posição do objeto
    esp = plt.Rectangle(xy, Le, He, fill=1, lw=2, angle=ae)
    ax.add_patch(esp)
    dresp = DraggableRectangle(esp)
    dresp.connect()

    # Atualizando a máquina
    xy = maq.get_xy()  # obtém a posição do objeto
    xm0, ym0 = xy  # redefine as variáveis da posição do objeto
    maq = plt.Rectangle(xy, Lm, Hm, fill=1, angle=am, color="gray")
    ax.add_patch(maq)
    drmaq = DraggableRectangle(maq)
    drmaq.connect()

    x0 = xm0 + Lm * np.cos(am*np.pi/180) - Hm * np.sin(am*np.pi/180)/2  # posição x da saída do laser
    y0 = ym0 + Hm * np.cos(am*np.pi/180)/2 + Lm*np.sin(am*np.pi/180)  # posição y da saída do laser
    x1 = x0 + np.cos(am*np.pi/180)  # coordenada x de um ponto na direção da máquina
    y1 = y0 + np.sin(am*np.pi/180)  # coordenada y de um ponto na direção da máquina
    x2 = xe0 - He * np.sin(ae*np.pi/180)  # coordenada x da extreminade esquerda do espelho
    y2 = ye0 + He * np.cos(ae*np.pi/180)  # coordenada y da extreminade esquerda do espelho
    x3 = x2 + Le * np.cos(ae*np.pi/180)  # coordenada x da extreminade direita do espelho
    y3 = y2 + Le * np.sin(ae*np.pi/180)  # coordenada y da extreminade direita do espelho

    # determinantes (colisão)
    t = np.linalg.det([[x0 - x2, x2-x3], [y0 - y2, y2-y3]])/np.linalg.det([[x0 - x1, x2 - x3], [y0 - y1, y2-y3]])
    u = -np.linalg.det([[x0 - x1, x0 - x2], [y0 - y1, y0 - y2]])/np.linalg.det([[x0 - x1, x2 - x3], [y0 - y1, y2-y3]])

    # se o espelho estiver no caminho do laser
    if t > 0 and 0 <= u <= 1:
        xcol = x2 + u * (x3 - x2)
        ycol = y2 + u * (y3 - y2)
        xf = xcol + 3*np.cos((2*ae - am)*np.pi/180)
        yf = ycol + 3*np.sin((2*ae - am)*np.pi/180)
    # se o laser não acertar o espelho
    else:
        xcol = x1
        ycol = y1
        xf = x1 + 3*np.cos(am*np.pi/180)
        yf = y1 + 3*np.sin(am*np.pi/180)

    # Criando o laser
    x, y = np.array([[x0, xcol, xf], [y0, ycol, yf]])
    line = plt.Line2D(x, y, lw=2., alpha=1.0, color="r")
    ax.add_line(line)

    # atualizando:
    fig.canvas.draw_idle()


sae.on_changed(update)
sam.on_changed(update)

update(0)

plt.subplots_adjust(left=0.25, bottom=0.25)

plt.show()
