from ambient_property.device.locker import Locker, MAX_LENGTH
import unittest


class TestLocker(unittest.TestCase):
    def setUp(self):
        self.lock = Locker(id=1, name="Front Door")

    def test_initialization(self):
        self.assertEqual(self.lock.id, 1)
        self.assertEqual(self.lock.name, "Front Door")
        self.assertFalse(self.lock.info()['locked'])

    def test_info_method(self):
        self.lock.paired = True
        expected_info = {
            'device_id': 1,
            'name': "Front Door",
            'paired': True,
            'locked': False,
        }
        self.assertEqual(self.lock.info(), expected_info)

    def test_modify_update_password(self):
        # register password, and lock it
        self.assertFalse(self.lock.info()['locked'])
        self.lock.modify(password="new_pass", update_password=True)
        self.lock.modify(True)
        self.assertTrue(self.lock.info()['locked'])

        self.lock.modify(locked=False, password="new_pass")
        self.assertFalse(self.lock.info()['locked'])

    def test_modify_unlock_empty_password(self):
        # register password, and lock it
        self.assertFalse(self.lock.info()['locked'])
        self.lock.modify(True)
        self.assertTrue(self.lock.info()['locked'])

        self.lock.modify(locked=False, password=None)
        self.assertFalse(self.lock.info()['locked'])

    def test_modify_unlock_correct_password(self):
        # register password, and lock it
        self.assertFalse(self.lock.info()['locked'])
        self.lock.modify(None, "my_pass", True)
        self.lock.modify(True)
        self.assertTrue(self.lock.info()['locked'])

        self.lock.modify(locked=False, password="my_pass")
        self.assertFalse(self.lock.info()['locked'])

    def test_modify_unlock_wrong_password(self):
        # register password, and lock it
        self.assertFalse(self.lock.info()['locked'])
        self.lock.modify(None, "my_pass", True)
        self.lock.modify(True)
        self.assertTrue(self.lock.info()['locked'])

        with self.assertRaises(ValueError) as context:
            self.lock.modify(locked=False, password="wrong_pass")
        self.assertEqual(str(context.exception), "Wrong password!")

    def test_modify_update_password_too_long(self):
        with self.assertRaises(ValueError) as context:
            self.lock.modify(password="a" * (MAX_LENGTH + 1), update_password=True)
        self.assertEqual(str(context.exception), f"Password cannot have more than {MAX_LENGTH} characters.")

    def test_modify_locked_when_password_set(self):
        self.lock.modify(locked=True)
        self.assertTrue(self.lock.info()['locked'])

    def test_unlock_with_pass_locker_without_password_set(self):
        self.lock.modify(True)
        with self.assertRaises(ValueError):
            self.lock.modify(locked=False, password="wrong_pass")

    def test_unlock_with_no_password_set(self):
        self.lock.modify(True)
        self.lock.modify(locked=False)
        self.assertFalse(self.lock.info()['locked'])

    def test_modify_locked_with_password_set(self):
        self.lock.modify(password="my_pass", update_password=True)
        self.lock.modify(locked=True)
        self.assertTrue(self.lock.info()['locked'])

