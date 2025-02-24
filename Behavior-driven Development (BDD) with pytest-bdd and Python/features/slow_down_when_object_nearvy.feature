Feature: Slow down whe object nervy
If the sensor detectsan object in the near field of the sensor range, reduce the speed by 1 m/s with a zero bound

Background:
    Given the near field sensor detects an object

@factory_floor
Scenario Outline: Robot detects object while in motion
    Given the robot is traveling at <initialSpeed>m/sensor
    When motion evaliation fires
    Then speed should be <finalSpeed>m/s

    Examples: speeds
    |   initialSpeed    |   finalSpeed  |
    |   10              |   9           |
    |   10001           |   10000       |
    |   1               |   0           |
    |   42              |   41          |
    |    0              |   0           |
    |    2              |   2           |


# Scenario: Robot detects object while in motion at any speed
#     Given the robot is movint at a speed > 0
#     When motion evaliation fires
#     Then speed should be decreasted by one meter per second

# Scenario: Robot detects object while in motion at any speed
#     Given the robot is movint at a speed == 0
#     When motion evaliation fires
#     Then the robot should remain at rest