import pytest

from lab_8 import Automat, State_Wait_Money, State_Wait_Choise, State_Get_Product

def test_initial_state():
    context = Automat(State_Wait_Money())
    assert isinstance(context.state, State_Wait_Money)

def test_state_transition_a_to_b():
    context = Automat(State_Wait_Money())
    context.request()
    assert isinstance(context.state, State_Wait_Choise)

def test_state_transition_b_to_C():
    context = Automat(State_Wait_Money())
    context.request()
    context.request()  
    assert isinstance(context.state, State_Get_Product)

def test_multiple_transitions():
    context = Automat(State_Wait_Money())
    states = [State_Wait_Money, State_Wait_Choise, State_Get_Product, State_Wait_Money]
    for state in states:
        assert isinstance(context.state, state)
        context.request()

if __name__ == "__main__":
    pytest.main()
