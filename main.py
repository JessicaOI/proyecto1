#Jessica Ortiz 20192
#sr5 texturas

from cargar import *

from textures import Texture

#tamaño de lienzo
render = Render(1000, 1000)

#cargar textura
hormiga = Texture('textureF.bmp')
#grass = Texture('green.bmp')
petal = Texture('petal.bmp')
tierra = Texture('dirt2.bmp')
oreo = Texture('Oreo.bmp')
cookie = Texture('cookiet.bmp')
caja = Texture('brown.bmp')
#Objetos Escena

#               eye, center, up
render.lookAt(V3(-0.5,0,20), V3(0,0,0), V3(0,1,0))


#box
render.glObjModel2('Cardboard.obj',translate=(0,0.7,0), scale=(0.4,0.4,0.4), rotate=(2.5,0,0), texture=caja)
#cookie
render.glObjModel2('cookie.obj',translate=(0.6,0.8,0), scale=(0.29,0.29,0.29), rotate=(2,-2,0), texture=cookie)
#oreo
render.glObjModel2('oreo.obj',translate=(1,0,0), scale=(0.009,0.009,0.009), rotate=(1,-4,0), texture=oreo)
#hormiga
render.glObjModel('formica.obj',translate=(0,0,0), scale=(0.2,0.2,0.2), rotate=(1,-4,0), texture=hormiga)
#grama
#render.glObjModel2('g2.obj',translate=(1,-0.5,0), scale=(1,1,1), rotate=(0,0,0), texture=petal)
#tierra
render.glObjModel2('plano.obj',translate=(-1,0,-5), scale=(0.3,0.3,0.3), rotate=(0,0,0), texture=tierra)

#imagen final
render.glFinish('out.bmp')