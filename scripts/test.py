import compas
from compas.datastructures import Mesh
from compas_notebook.app import App
from compas.colors import Color
from random import random

mesh = Mesh.from_obj(compas.get('faces.obj'))

viewer = App()
facecolor = {face: Color.from_i(random()) for face in mesh.faces()}
viewer.add(mesh, facecolor=facecolor, linecolor=Color(0.0, 0.0, 1.0), pointcolor=Color(0.0, 1.0, 0.0), show_points=True, pointsize=0.1)
viewer.show()