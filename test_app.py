import pytest
from app import *

def test_find_postcode():
    #WHEN
    mock_coordinates=(40.6976637, -74.1197632)
    #DO
    actual_result=find_postcode(mock_coordinates)
    #THEN
    expected_result="07305"
    assert expected_result==actual_result