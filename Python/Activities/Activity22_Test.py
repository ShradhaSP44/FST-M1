import pytest
def test_Addition():
    num1 = 10
    num2=15
    sum= num1+num2
    assert sum==25
def test_Substraction():
    num1= 10
    num2 = 5
    Sub = num1-num2
    assert Sub==5
@pytest.mark.calc
def test_Multiplication():
    num1=5
    num2=2
    Multi=num1*num2
    assert Multi==10
@pytest.mark.calc
def test_Division():
    num1=6
    num2=1
    Div=num1/num2
    assert Div==3