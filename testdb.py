from operator import add
from unittest.mock import patch , Mock
from dotenv import load_dotenv
from database_func import add_to_db, update_table, delete_from_db

# @patch("builtins.input")
# @patch("database_func.execute_db")

# def test_add_product(mock_execute, mock_input):
#     #assemble
#     mock_input.side_effect = ["pop", "orange", 10]
#     expected = (f' INSERT INTO food (food_name, description, food_price) VALUES ("pop", "orange", 10)')

#     #act
#     add_to_db('food', "food_name, description, food_price", "'pop', 'orange', 10") 

#     #Asset
#     mock_execute.assert_called_with(expected)



# test_add_product()

@patch('builtins.input')
def test_add_product(mock_input):
    mock_input.side_effect = ["pop", "orange", 10]
    mock_input_db = 'food'
    expected_products = ["pop", "orange", 10]
    mock_read_products = Mock(return_value = expected_products)
    mock_insert_product_into_db = Mock()

    actual = add_to_db(mock_input_db,mock_insert_product_into_db, mock_read_products)

    assert actual == expected_products
    mock_insert_product_into_db.assert_called_with("pop", "orange", 10)
 

test_add_product()