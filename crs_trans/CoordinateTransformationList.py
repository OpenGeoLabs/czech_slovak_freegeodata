from qgis.core import *
from qgis.gui import *

from .CoordinateTransformation import CoordinateTransformation


class CoordinateTransformationList(list):
    """
    Represents list of Coordnate transformations and allows to preform some usefull queries.
    """
