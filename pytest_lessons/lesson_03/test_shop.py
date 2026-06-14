from unittest.mock import MagicMock
from shop import ShopService , OrderError 

import pytest
def test_place_order_success():
    mock_gateway = MagicMock()
    mock_gateway.charge.return_value = {"status": "success" , "transaction_id": "txn_123"}

    shop = ShopService(mock_gateway)
    order =  shop.place_order("test@example.com" , "Product A" , 100)


    assert order["product"] == "Product A"
    assert order["amount"] == 100
    assert len(shop.orders) == 1  
    mock_gateway.charge.assert_called_once_with("test@example.com", 100)



def test_place_order_failed():
    mock_gateway = MagicMock()
    mock_gateway.charge.return_value = {"status": "failed" , "transaction_id": "txn_123"}

    shop = ShopService(mock_gateway)
    with pytest.raises(OrderError):
        shop.place_order("test@example.com" , "Product A" , 100)
    mock_gateway.charge.assert_called_once_with("test@example.com", 100)




def test_place_order_handles_connection_error():
    mock_gateway = MagicMock()
    mock_gateway.charge.side_effect = ConnectionError("Connection failed")


    shop = ShopService(mock_gateway)

    with pytest.raises(ConnectionError):
        shop.place_order("test@example.com" , "Product A" , 100)

    assert len(shop.orders) == 0
    mock_gateway.charge.assert_called_once_with("test@example.com", 100)