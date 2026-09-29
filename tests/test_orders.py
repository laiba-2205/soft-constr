import pytest
from src.orders import calc

def test_calc_order_total():
  
    order = {
        "items": [{"price": 10, "qty": 2}, {"price": 15, "qty": 1}],
        "member": True,
        "country": "US"
    }
    
 
    result = calc(order)
  
    assert result == pytest.approx(50.0)