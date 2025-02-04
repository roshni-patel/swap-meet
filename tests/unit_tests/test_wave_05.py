import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."

# @pytest.mark.skip
def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category == "Decor"
    assert str(decor) == "Something to decorate your space."

# @pytest.mark.skip
def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category == "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."

# @pytest.mark.skip
def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

# @pytest.mark.skip
def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description

    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)

    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

def test_items_returns_error_when_condition_is_not_between_0_and_5_():
    # Arrange
    item = Electronics(condition=6)

    # Act
    result = item.condition_description()

    # Assert
    assert result == "Condition must be a float between 0 and 5."

def test_items_returns_correct_condition_description_for_floats():
    # Arrange
    item_a = Decor(condition=0.4, age=3.0)
    item_b = Electronics(condition=1.2, age=5.0)
    item_c = Decor(condition=2.5, age=2.0)
    item_d = Decor(condition=3.6, age=3.0)
    item_e = Electronics(condition=4.2, age=5.0)
    item_f = Decor(condition=5.0, age=2.0)

    # Act/Assert 
    assert item_a.condition_description() == "Poor"
    assert item_b.condition_description() == "Acceptable"
    assert item_c.condition_description() == "Good"
    assert item_d.condition_description() == "Very Good"
    assert item_e.condition_description() == "Like New"
    assert item_f.condition_description() == "Brand New"
