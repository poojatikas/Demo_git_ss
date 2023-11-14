import pytest


class Test_015_markers():

    @pytest.mark.skip
    def test_add(self):
        a = 10
        b = 20
        add = (a + b)
        if (add == 30):
            print('\n ADDITION SUCESSFUL')
            print("Result=", add)
            assert True
        else:
            print('\n ADDITION UNSUCESSFUL')
            assert False

    @pytest.mark.skipif
    def test_sub(self):
                c = 10
                d = 5
                sub = (c - d)
                if (sub == 5):
                    print('\n SUBSTRACTION SUCESSFUL')
                    print("Result=", sub)
                    assert True
                else:
                    print('\n SUBSTRACTION UNSUCESSFUL')
                    assert False

    @pytest.mark.xfail
    def test_Mul(self):
         e = 10
         f = 15
         Mul = e * f
         if (Mul == 150):
             print('\n VALID OPERATION')
             print("Result=", Mul)
             assert True
         else:
             print('\n INVALID OPERATION')
             assert False

    def test_014_01_Div(self):
         g = 15
         h = 5
         div = g / h
         if (div == 3):
             print('VALID OPERATION')
             print("Result=", div)
             assert True
         else:
             print('INVALID OPERATION')
             assert False

