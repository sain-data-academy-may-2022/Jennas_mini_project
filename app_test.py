import unittest
import loops
import menus 
from unittest.mock import Mock, patch

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
    mock_input.return_value = 'Tom'

    expected = 'Tom'

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









     
