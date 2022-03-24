from math import sin, cos, radians

def getXYComponents(force: float, angle: int) -> tuple[float, float]:
    xComponent = sin(angle) * force
    yComponent = cos(angle) * force
    return (sin(radians(xComponent)), sin(radians(yComponent)))