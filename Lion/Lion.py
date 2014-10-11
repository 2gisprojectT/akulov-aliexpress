__author__ = 'Djonny'
from fsm_data import fsm_data
class lion(fsm_data):
    def __init__(self):
        self.status=""
        self.last_action=""
        self.__change_status()
    #change status
    def __change_status(self):
        if self.status=="":
            self.status=self._status[0]
        elif self.status==self._status[0]:
            self.status=self._status[1]
        elif self.status==self._status[1]:
            self.status=self._status[0]
    #methods action
    def __action_sleep(self):
        self.last_action=self._action[0]
    def __action_run(self):
        self.last_action=self._action[1]
    def __action_see(self):
        self.last_action=self._action[2]
    def __action_eat(self):
        self.last_action=self._action[3]

    #public method
    def lion_find(self,object):
        if self.status==self._status[0]:
            self.__fed_lion_find(object)
        elif self.status==self._status[1]:
            self.__hungry_lion_find(object)
    #private method
    def __fed_lion_find(self,object):
        if object==self.object[0]:
            self.__action_sleep()
            self.__change_status()
        elif object==self.object[1]:
            self.__action_run()
            self.__change_status()
        elif object==self.object[2]:
            self.__action_see()
            self.__change_status()
    def __hungry_lion_find(self,object):
        if object==self.object[0]:
            self.__action_eat()
            self.__change_status()
        elif object==self.object[1]:
            self.__action_run()
        elif object==self.object[2]:
            self.__action_sleep()

    def get_status(self):
        return self.status;

    def get_last_action(self):
        return self.last_action

    def say_lion_find(self,object):
        self.lion_find(object)
        print("I finded {} , my action is {}, now my status is {}\n".format(object,self.last_action,self.status))


fsmdata=fsm_data()
leo=lion()
leo.say_lion_find(fsmdata.object[0])
leo.say_lion_find(fsmdata.object[1])
leo.say_lion_find(fsmdata.object[2])
leo.say_lion_find(fsmdata.object[0])
leo.say_lion_find(fsmdata.object[1])
leo.say_lion_find(fsmdata.object[2])