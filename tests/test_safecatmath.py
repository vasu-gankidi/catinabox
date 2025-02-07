import pytest

from ..catinabox.safecatmath import cat_years_to_hooman_years, InvalidAge

@pytest.mark.parametrize('age',[
    1001,
    -1,
    'ten',
    'nan',
    [1,2],
    {-1,-2}
    ])

def test__cat_years_to_hooman_years__middle_age__succeeds():
    hooman_age = cat_years_to_hooman_years(7)
    assert hooman_age == 35

def test__cat_years_to_hooman_years__less_than_one_year__succeeds():
    hooman_age = cat_years_to_hooman_years(0.1)
    assert hooman_age == 0.5

def test__cat_years_to_hooman_years__0__returns_0():
    hooman_age = cat_years_to_hooman_years(0)
    assert hooman_age == 0

def test__cat_years_to_hooman_years_AllInvalidParametrizeTest(age):
    with pytest.raises(InvalidAge):
        cat_years_to_hooman_years(age)

# All the below fucntions can paramterizedWith pytest.mark.parametrize('',[])
# as shown in the above test 
# 'test__cat_years_to_hooman_years_AllInvalidParametrizeTest(age)'
def test__cat_years_to_hooman_years__less_0__raises():
    # context manager here. expects the statement inside to raise
    # 'InvalidAge' exception and catches the exception and handles
    # it. If not, it will raise exception and stops execution.
    # setup and clean up activities.
    with pytest.raises(InvalidAge): # this context manager here.
        cat_years_to_hooman_years(-1)

def test__cat_years_to_hooman_years__older_than_1000__raises():
    with pytest.raises(InvalidAge):
        cat_years_to_hooman_years(1001)
    assert cat_years_to_hooman_years(2) == 10

def test__cat_years_to_hooman_years__string__raises():
    with pytest.raises(InvalidAge):
        cat_years_to_hooman_years("Ten")

def test__cat_years_to_hooman_years__nan__raises():
    with pytest.raises(InvalidAge):
        cat_years_to_hooman_years("nan")