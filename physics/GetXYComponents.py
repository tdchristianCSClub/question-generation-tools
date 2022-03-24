from math import sin, cos

def getXYComponents(force: float, angle: int) -> tuple[float, float]:
    xComponent = sin(angle) * force
    yComponent = cos(angle) * force
    return (xComponent, yComponent)