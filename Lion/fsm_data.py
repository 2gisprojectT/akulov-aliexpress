__author__ = 'Djonny'

class fsm_data:
    object=["antelope","hunter","tree"]
    def __init__(self):
        {}

    def get_action(self, table,state,symbol):
        if table[state].has_key(symbol):
            return table[state][symbol][1]
        else:
            return False

    def get_state(self,table,state,symbol):
        if table[state].has_key(symbol):
            return table[state][symbol][0]
        else:
            return False