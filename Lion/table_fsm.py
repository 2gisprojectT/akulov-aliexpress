__author__ = 'Djonny'
from fsm_data import fsm_data
class table_fsm(fsm_data):
    def __init__(self):
        self.status=""
        self.action=""
    def find(self,object,status):
        if(status==self._status[0]):
            if(object==self.object[0]):
                self.status=self._status[1]
                self.action=self._action[0]
            elif(object==self.object[1]):
                self.status=self._status[1]
                self.action=self._action[1]
            elif(object==self.object[2]):
                self.status=self._status[1]
                self.action=self._action[2]
        elif(status==self._status[1]):
            if(object==self.object[0]):
                self.status=self._status[0]
                self.action=self._action[3]
            elif(object==self.object[1]):
                self.action=self._action[1]
            elif(object==self.object[2]):
                self.action=self._action[0]

    def get_status(self):
        return self.status
    def get_action(self):
        return  self.action