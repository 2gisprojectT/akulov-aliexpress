__author__ = 'Djonny'
from fsm_data import fsm_data
from unittest import TestCase
from table_fsm import table_fsm
from Lion import lion
import unittest
import random

class LionTest(TestCase,fsm_data):
    def test_lionfind_monkeytest(self):
        leo=lion()
        table=table_fsm()
        fsm=fsm_data()
        for i in range(100):
            var=random.randint(0,2)
            table.find(fsm.object[var],leo.status)
            leo.lion_find(fsm.object[var])
            self.assertEqual(table.status,leo.status,'Now status not correct')
            self.assertEqual(table.action,leo.last_action,'Action not correct')


if __name__ == '__main__':
    unittest.main()
