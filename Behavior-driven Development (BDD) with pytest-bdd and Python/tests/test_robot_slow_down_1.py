from pytest_bdd import scenario, given, when, then, parsers
import pytest

from robot import robot
from velocity import velocity

# Background:
#     Given the near field sensor detects an object

@pytest.fixture
def the_robot():
    return robot(velocity(0,0))

@pytest.fixture
def the_near_field_sensor():
    the_near_field_sensor = False
    return the_near_field_sensor

@scenario("../features/slow_down_when_object_nearvy.feature", "Robot detects object while in motion")
def test_slow_down():
    return

@given("the near field sensor detects an object", target_fixture="the_near_field_sensor")
def field_sensor_detects(the_near_field_sensor):
    the_near_field_sensor = True
    return the_near_field_sensor

@given(parsers.cfparse("the robot is traveling at {initial_speed: d}m/sensor"))
def robot_traveling(the_robot, initial_speed):
    the_robot.velocity.speed = initial_speed

@when("motion evaliation fires")
def robot_motion_evaluation(the_near_field_sensor, the_robot):
    the_robot.motion_evaluation(the_near_field_sensor)

@then(parsers.cfparse("speed should be {final_speed: d}m/s"))
def robot_speed_slower(the_robot, final_speed):
    assert(the_robot.velocity.speed == final_speed)