import pytest


class Test_015_02_userdefined_markers():

    @pytest.mark.customer
    def test_add_cust(self):
        print('\n *******CUSTOMER ADDED SUCESSFULLY*******')

    @pytest.mark.customer
    def test_del_cust(self):
        print('\n ********CUSTOMER DELETED SUCESSFULLY*******')


    @pytest.mark.product
    def test_add_prod(self):
        print('\n*********PRODUCT ADDED SUCESSFULLY*********')

    @pytest.mark.product
    def test_del_prod(self):
        print('\n*********PRODUCT DELETED SUCESSFULLY*******')

    @pytest.mark.Bill
    def test_add_bill(self):
        print('\n************BILL ADDED SUCESSFULLY********')

    @pytest.mark.Bill
    def test_del_bill(self):
        print('\n***********BILL DELETED SUCESSFULLY********')

    @pytest.mark.sanity
    @pytest.mark.patient
    def test_add_patient(self):
        print('\n*********PATIENT ADDED SUCESSFULLY*********')

    @pytest.mark.regression
    @pytest.mark.patient
    def test_del_patient(self):
        print('\n*********PATIENT DELETED SUCESSFULLY*******')