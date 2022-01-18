import matplotlib as mpl
from svgpath2mpl import parse_path
from svgpathtools import svg2paths

saturn_path, attributes = svg2paths('planet_marker/saturn.svg')
planet = parse_path(attributes[0]['d'])
planet.vertices -= planet.vertices.mean(axis=0)
planet = planet.transformed(mpl.transforms.Affine2D().rotate_deg(180))
planet = planet.transformed(mpl.transforms.Affine2D().scale(-1,1))

hst_path, attributes = svg2paths('hst.svg')
hst = parse_path(attributes[0]['d'])
hst.vertices -= hst.vertices.mean(axis=0)
hst = hst.transformed(mpl.transforms.Affine2D().rotate_deg(180))
hst = hst.transformed(mpl.transforms.Affine2D().scale(-1,1))

saturn2_path, attributes = svg2paths('test2.svg')
saturn = parse_path(attributes[0]['d'])
saturn.vertices -= saturn.vertices.mean(axis=0)
# saturn = saturn.transformed(mpl.transforms.Affine2D().rotate_deg(180))
# saturn = saturn.transformed(mpl.transforms.Affine2D().scale(-1,1))