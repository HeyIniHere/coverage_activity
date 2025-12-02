from app import usd_to_eur

def test_normal_conversion():
    assert usd_to_eur(100) == 90.0
    # assert usd_to_eur(1.234) == 1.11

def test_rounding():
    assert usd_to_eur(1.234) == 1.11