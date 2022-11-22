import numpy
import pickle
import sys
import vtk
from vtk.util import numpy_support


pickledInput = sys.stdin.buffer.read()
input = pickle.loads(pickledInput)

# polyData = vtk.vtkPolyData()
#polyData.SetPoints(input['vertexArray'])
#idArray = numpy_support.numpy_to_vtk(input['idArray'])
#polydata.GetPolys.SetCells(input['cellCount'], idArray)

# TODO: process the polydata with vtk

print(input['a'])

modified_a = input['a'] + 'Adding from child'
output = {}
output['b'] = modified_a

sys.stdout.buffer.write(pickle.dumps(output))
