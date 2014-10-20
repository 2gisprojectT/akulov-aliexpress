#-*-coding:utf8-*-
__author__ = 'Djonny'
from fsm_data import fsm_data
from unittest import TestCase
from Lion import lion
import unittest

#Тест на класс fsm_data
class fsm_dataTest(TestCase,fsm_data):
    def test_gets(self):
        fsm=fsm_data()
        table={0: {"a": [1, "1"], "b": [0, "2"]},
               1: {"a": [0, "3"], "b": [0, "2"]}}
        self.assertEqual(1,fsm.get_state(table,0,"a"),'Now status not correct')
        self.assertEqual("1",fsm.get_action(table,0,"a"),'Action not correct')

        self.assertEqual(0,fsm.get_state(table,0,"b"),'Now status not correct')
        self.assertEqual("2",fsm.get_action(table,0,"b"),'Action not correct')

        self.assertEqual(0,fsm.get_state(table,1,"a"),'Now status not correct')
        self.assertEqual("3",fsm.get_action(table,1,"a"),'Action not correct')

        self.assertEqual(0,fsm.get_state(table,1,"b"),'Now status not correct')
        self.assertEqual("2",fsm.get_action(table,1,"b"),'Action not correct')

        self.assertEqual(False,fsm.get_state(table,1,"3"),'Now status not correct')
        self.assertEqual(False,fsm.get_action(table,1,"3"),'Action not correct')
#Тесты на класс Lion
class LionTest(TestCase):
    def test_lion_init(self):
        leo=lion()
        table={
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
        self.assertEqual(table,leo.table,'Table not correct')
        self.assertEqual("",leo.get_status(),'State not correct')
        self.assertEqual("",leo.get_last_action(),'Action not correct')

    def test_lion_start(self):
        leo=lion()
        leo.start()
        self.assertEqual("fed",leo.get_status(),'State not correct')
        self.assertEqual("",leo.get_last_action(),'Action not correct')

    def test_lion_find_antelope(self):
        leo=lion()
        fsm=fsm_data()
        leo.start()

        self.assertEqual(True,leo.lion_find(fsm.object[0]),'Not true result')
        self.assertEqual("hungry",leo.get_status(),'State not correct')
        self.assertEqual("sleep",leo.get_last_action(),'Action not correct')

        self.assertEqual(True,leo.lion_find(fsm.object[0]),'Not true result')
        self.assertEqual("fed",leo.get_status(),'State not correct')
        self.assertEqual("eat",leo.get_last_action(),'Action not correct')

    def test_lion_find_hunter(self):
        leo=lion()
        fsm=fsm_data()
        leo.start()

        self.assertEqual(True,leo.lion_find(fsm.object[1]),'Not true result')
        self.assertEqual("hungry",leo.get_status(),'State not correct')
        self.assertEqual("run",leo.get_last_action(),'Action not correct')

        self.assertEqual(True,leo.lion_find(fsm.object[1]),'Not true result')
        self.assertEqual("hungry",leo.get_status(),'State not correct')
        self.assertEqual("run",leo.get_last_action(),'Action not correct')

    def test_lion_find_tree(self):
        leo=lion()
        fsm=fsm_data()
        leo.start()

        self.assertEqual(True,leo.lion_find(fsm.object[2]),'Not true result')
        self.assertEqual("hungry",leo.get_status(),'State not correct')
        self.assertEqual("see",leo.get_last_action(),'Action not correct')

        self.assertEqual(True,leo.lion_find(fsm.object[2]),'Not true result')
        self.assertEqual("hungry",leo.get_status(),'State not correct')
        self.assertEqual("sleep",leo.get_last_action(),'Action not correct')

    def test_lion_find_unknown(self):
        leo=lion()
        fsm=fsm_data()
        leo.start()

        self.assertEqual(False,leo.lion_find("car"),'Not true result')
        self.assertEqual("fed",leo.get_status(),'State not correct')
        self.assertEqual("",leo.get_last_action(),'Action not correct')

if __name__ == '__main__':
    unittest.main()
