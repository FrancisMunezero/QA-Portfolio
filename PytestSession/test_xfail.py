import pytest


def apply_discount(total, coupon_code):
    #if coupon_code == "SAVE10":          #The discount feature can be implemented by commenting out the two lines of code
        #return total * 0.9
    return total

@pytest.mark.xfail(reason="Discount feature not yet implemented")
def test_apply_discount():
    total = 100
    coupon_code = "SAVE10"
    discount_total = apply_discount(total, coupon_code)

    assert discount_total == 90