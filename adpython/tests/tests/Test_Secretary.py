from adpython.tests import app
import unittest
from unittest.mock import patch


class TestSecretary(unittest.TestCase):
    # def setUp(self):
    #     with patch('app.input', return_value='q'):
    #         app.secretary_program_start()

    def test_add_new_doc(self):
        with patch('adpython.tests.app.input', side_effect = ['1','2','3','4']):
            app.add_new_doc()
            self.assertIn(['1','2','3','4'], app.append_doc_to_shelf(['1','2','3','4']))



        # with patch('adpython.tests.app.input', return_value='11-'):
        #     app.get_doc_owner_name()

