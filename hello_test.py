from hello import add, toyou, substract

def setup_function(function):
    print("Running Setup: %s" % {function.__name__})
    function.x = 10

def teardown_function(function):
    print("Running Teardown: %s" % {function.__name__})
    del function.x

def test_hello_substact():
    assert substract(test_hello_substact.x)==9
