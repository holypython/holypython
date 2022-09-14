from viktor.core import ViktorController
from viktor.parametrization import ViktorParametrization, NumberField
from viktor.geometry import Point, Line, CircularExtrusion, Cone, Sphere, Material, Color
from viktor.views import GeometryResult, GeometryView

WHITE = Material("White", color=Color.white())
RED = Material("Red", color=Color.red())


class Parametrization(ViktorParametrization):

    base_height = NumberField("Height base", default=50, min=1)
    base_diameter = NumberField("Diameter base", default=3, min=1)
    sphere_radius = NumberField("Radius sphere", default=4, min=1)
    mast_height = NumberField("Height mast", default=30, min=1)


class Controller(ViktorController):
    label = 'VIKTOR Tutorial'
    parametrization = Parametrization

    @GeometryView("3D", duration_guess=1)
    def visualize_tower(self, params, **kwargs):
        """Creates the 3D view and visualizes the Radio Tower"""

        print("Params:", params)

        # Reference points

        base_start = Point(0, 0, 0)
        base_end = Point(0, 0, params.base_height)

        # Create tower base

        line = Line(base_start, base_end)
        base = CircularExtrusion(diameter=params.base_diameter, line=line)

        # Create tower cabin

        cabin = Sphere(base_end, params.sphere_radius)

        # Tower top

        top = Cone(diameter=params.base_diameter, height=params.mast_height, origin=base_end)

        return GeometryResult([base, cabin, top])