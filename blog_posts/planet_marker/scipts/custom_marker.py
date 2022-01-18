import matplotlib as mpl
from svgpath2mpl import parse_path
from svgpathtools import svg2paths

planet_path, attributes = svg2paths('../saturn.svg')
planet_marker = parse_path(attributes[0]['d'])
planet_marker.vertices -= planet_marker.vertices.mean(axis=0)
planet_marker =planet_marker.transformed(mpl.transforms.Affine2D().rotate_deg(180))
planet_marker= planet_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))