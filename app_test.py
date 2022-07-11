import unittest
import loops
import menus 
from unittest.mock import Mock, patch
from inputs import int_input, stock_check, phone_input, real_product
from database_func import cursor

mock = Mock()



def test_loop_1():
    #assemble
    food_options = 0
    expected = False
    #Act
    actual = loops.food_loop(food_options)
    #Assert
    assert actual == expected

test_loop_1()


def test_loop_2():
    #assemble
    courier_options = 0
    expected = False
    #Act
    actual = loops.courier_loop(courier_options)
    #Assert
    assert actual == expected

test_loop_2()


def test_loop_3():
    #assemble
    order_options = 0
    expected = False
    #Act
    actual = loops.orders_loop(order_options)
    #Assert
    assert actual == expected

test_loop_3()

def test_Colour_red():
    text = 'Hello'
    expected = 'Hello'
    actual = menus.Colour_red(text)
    assert actual == expected

test_Colour_red()


@patch('builtins.print')
def test_print_menu(mock_print):
    text = 'Hello'
    expected = 'Hello'
    menus.print_menu(text)
    mock_print.assert_called_with(expected)

test_print_menu()


@patch('builtins.input')
def test_get_input(mock_input):
    #assemble
    mock_input.return_value = 'Costalot'

    expected = 'Costalot'

    actual = menus.get_input('text')

    assert actual ==expected

test_get_input()


@patch('builtins.input')
def test_get_input_int(mock_input):
    #assemble
    mock_input.return_value = 1

    expected = 1

    actual = menus.get_input_int('text')

    assert actual ==expected

test_get_input_int()



@patch('builtins.input')
def test_int_input_correct(mock_input):
    #assemble
    mock_input.return_value = 3

    expected = 3

    #act
    actual = int_input("")

    #assert

    assert actual == expected


test_int_input_correct()

@patch('builtins.input')
def test_int_input_incorrect(mock_input):
    #assemble
    mock_input.return_value = 'hello'
    mock_input.return_value = 3

    expected = 3

    #act
    actual = int_input("")

    #assert

    assert actual == expected


test_int_input_incorrect()



@patch('builtins.input')
def test_stock_check(mock_input):
    mock_input.return_value = 10
    expected = 10

    actual = stock_check(11)

    assert actual == expected


test_stock_check()


@patch('builtins.input')
def test_stock_check_one_wrong(mock_input):
    mock_input.return_value = 100
    mock_input.return_value = 10
    expected = 10

    actual = stock_check(11)

    assert actual == expected

test_stock_check_one_wrong()


@patch('builtins.input')
def test_phone_input(mock_input):
    #assemble
    mock_input.return_value = 1213
    mock_input.return_value = '07488311272'
    expected = '07488311272'

    #act
    actual = phone_input()

    # 
    assert actual == expected


test_phone_input()

@patch('builtins.input')
def test_real_product(mock_input):
    #assemble
    mock_input = 22
    mock_input = 1
    expected = 1

    #act
    actual = real_product(cursor)

    #assert

    assert actual == expected

test_real_product()


