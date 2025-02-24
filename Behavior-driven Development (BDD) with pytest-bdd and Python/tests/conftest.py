#conftest.py

#hooks

def pytest_bdd_before_scenario(request, feature, scenario):
    print("Before scenario")
    print("Feature:",feature.name)
    print("Scenario:",scenario.name)
    print("---------")

def pytest_bdd_after_step(request, feature, scenario, step, step_func, step_func_args):
    print("whatever is going on")