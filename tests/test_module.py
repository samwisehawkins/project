from package import module

def test_main():
    module.main()
    assert True 

def test_my_func():
    result = module.my_func("a", "b")
    assert result==True
