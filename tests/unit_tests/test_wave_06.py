import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_best_by_category():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Clothing(condition=4.0)
    item_d = Decor(condition=5.0)
    item_e = Clothing(condition=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_category("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_best_by_category_no_matches_is_none():
    item_a = Decor(condition=2.0)
    item_b = Decor(condition=2.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_category("Electronics")

    assert best_item is None

# @pytest.mark.skip
def test_best_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(condition=2.0)
    item_b = Clothing(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_category("Clothing")

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.condition == pytest.approx(4.0)

# @pytest.mark.skip
def test_swap_best_by_category():
    # Arrange
    # me
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert result 
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_a and item_b and item_f in tai.inventory
    assert item_c and item_d and item_e in jesse.inventory 
    assert item_c not in tai.inventory 
    assert item_f not in jesse.inventory 

# @pytest.mark.skip
def test_swap_best_by_category_reordered():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there
    assert result 
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_a and item_b and item_f in tai.inventory
    assert item_c and item_d and item_e in jesse.inventory 
    assert item_c not in tai.inventory
    assert item_f not in jesse.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

# @pytest.mark.skip
def test_swap_best_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories
    assert not result 
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_d and item_e and item_f in jesse.inventory
    assert item_a and item_b and item_c in tai.inventory


# @pytest.mark.skip
def test_swap_best_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(condition=2.0)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_best_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories
    assert not result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_d and item_e and item_f in jesse.inventory
    assert item_a and item_b and item_c in tai.inventory

def test_swap_swap_by_newest_different_ages():
    # Arrange
    item_a = Decor(condition=2.0, age=3.0)
    item_b = Electronics(condition=4.0, age=5.0)
    item_c = Decor(condition=4.0, age=1.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=8.0)
    item_e = Decor(condition=4.0, age=4.0)
    item_f = Clothing(condition=4.0, age=0.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    # Assert
    assert result 
    assert item_c in jesse.inventory
    assert item_f in tai.inventory
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3

def test_swap_by_newest_one_all_same_age():
    # Arrange
    item_a = Decor(condition=2.0, age=3.0)
    item_b = Electronics(condition=4.0, age=3.0)
    item_c = Decor(condition=4.0, age=3.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(condition=2.0, age=8.0)
    item_e = Decor(condition=4.0, age=4.0)
    item_f = Clothing(condition=4.0, age=0.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    # Assert 
    assert result 
    assert item_a or item_b or item_c in jesse.inventory
    assert item_a or item_b or item_c not in tai.inventory
    assert item_f in tai.inventory 
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3


def test_swap_by_newest_both_all_same_age_swaps_first_instances():
    # Arrange
    item_a = Decor(condition=2.0, age=3.0)
    item_b = Electronics(condition=4.0, age=3.0)
    item_c = Decor(condition=4.0, age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=8.0)
    item_e = Decor(condition=4.0, age=8.0)
    item_f = Clothing(condition=4.0, age=8.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    # Assert 
    assert result  
    assert item_a in jesse.inventory
    assert item_a not in tai.inventory
    assert item_d in tai.inventory 
    assert item_d not in jesse.inventory 

    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3    

def test_swap_by_newest_returns_false_if_either_inventory_is_empty():
    # Arrange
    item_a = Decor(condition=2.0, age=3.0)
    item_b = Electronics(condition=4.0, age=3.0)
    item_c = Decor(condition=4.0, age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )

    # Assert
    assert not result 