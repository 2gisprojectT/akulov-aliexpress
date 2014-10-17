#-*-coding:utf8-*-
__author__ = 'Djonny'
from fsm_data import fsm_data
class lion(fsm_data):
    def __init__(self):
        self.status= ""
        self.last_action= ""
        self.table= {
            "fed": {
                "antelope": ["hungry", "sleep"],
                "hunter": ["hungry", "run"],
                "tree": ["hungry", "see"]
            },
            "hungry": {
                "antelope": ["fed", "eat"],
                "hunter": ["hungry", "run"],
                "tree": ["hungry", "sleep"]
            }
        }

    def start(self):
        self.status="fed"
        self.last_action= ""

    def lion_find(self,object):
        state=self.get_state(self.table,self.status,object)
        action=self.get_action(self.table,self.status,object)

        if ((type(state)!=bool) & (type(action)!=bool)):
            self.status=state
            self.last_action=action
            return True;
        else:
            return False;


    def get_status(self):
        return self.status;

    def get_last_action(self):
        return self.last_action

#Тестировать не имеет смысла, т.к. работает так же как и lion_find(arg), только выводит информацию на экран
    def say_lion_find(self,object):
        if self.lion_find(object):
            print("I finded {} , my action is {}, now my status is {}\n".format(object, self.last_action, self.status))
            return True
        else:
            return False


fsmdata=fsm_data()
leo=lion()
leo.start()
leo.say_lion_find(fsmdata.object[0])
leo.say_lion_find(fsmdata.object[1])
leo.say_lion_find(fsmdata.object[2])
leo.say_lion_find(fsmdata.object[0])
leo.say_lion_find(fsmdata.object[1])
leo.say_lion_find(fsmdata.object[2])