import hello

def test_hello():
    assert hello.hello_world() == "Hello World!"
    
def test_Nhello():
    assert hello.hello_world(3) == "Hello World!Hello World!Hello World!"