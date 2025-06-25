from ambient_property.device.device import Device

MAX_LENGTH = 10


class Locker(Device):
    def __init__(self, id, name):
        super().__init__(id, name)
        self._locked = False
        self._password = None

    def info(self):
        return {
            'device_id': self.id,
            'name': self.name,
            'paired': self.paired,
            'locked': self._locked,
        }

    def modify(self, locked = None, password = None, update_password = False):
        def _maybe_update_password():
            if password is not None and update_password:
                if len(password) > MAX_LENGTH:
                    raise ValueError(f"Password cannot have more than {MAX_LENGTH} characters.")
                self._password = password

        def _check_password():
            if not update_password:
                if self._password == password:
                    self._locked = False
                else:
                    raise ValueError("Wrong password!")

        if locked is None:
            _maybe_update_password()
            return
        elif locked is True:
            self._locked = True
            return
        else:
            if not update_password:
                _check_password()
                return
        raise AttributeError("Invalid attribute!")
