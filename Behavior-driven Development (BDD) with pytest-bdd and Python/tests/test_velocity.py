from velocity import velocity
import pytest


pytestmark = pytest.mark.framework

def test_createSimpleVelocity():
    vel  = velocity(90,10)

    assert vel.heading == 90
    assert vel.speed == 10

def test_creteVelocityWithNegativeSpeed():
    with pytest.raises(Exception) as e:
        vel = velocity(90,-20)

    assert str(e.value)== "Speed can not be below 0"

def test_createVelocityWithCompoundingHeading():
    
    vel = velocity(405, 10)

    assert vel.heading == 45
    assert vel.speed == 10