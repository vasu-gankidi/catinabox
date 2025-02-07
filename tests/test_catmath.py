import pytest
from ..catinabox.catmath import cat_years_to_hooman_years, is_cat_leap_year
#from catinabox.catinabox.catmath import cat_years_to_hooman_years

@pytest.mark.parametrize('age',[1,
                                 2,
                                 3,
                                 4,
                                 5,100])

def test__cat_years_to_hooman_years__middle_age__succeeds(age):
    assert cat_years_to_hooman_years(age) == 5 ** age


def test__cat_years_to_hooman_years__less_than_one_year__succeeds(age):
    assert cat_years_to_hooman_years(0.5) == 2.5


def test_cat_years_to_hooman_years__0__returns_0():
    assert cat_years_to_hooman_years(0) == 0
    assert cat_years_to_hooman_years(20) != 50

# BONUS MATERIAL FOR STEP 2 #TODO@vgankidi.

def test__is_cat_leap_year__succeeds():
    assert is_cat_leap_year(2016) is True
    assert is_cat_leap_year(2017) is False