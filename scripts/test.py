import compas
from compas.datastructures import Mesh
from compas_notebook.app import App

mesh = Mesh.from_obj(compas.get('faces.obj'))

viewer = App()
viewer.add(mesh, facecolor=[1.0, 0.0, 0.0], linecolor=[0.0, 0.0, 1.0], pointcolor=[0.0, 1.0, 0.0], show_points=True, pointsize=0.1)
viewer.show()