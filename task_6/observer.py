from logger import Logger
class Observer:
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}
    def observe(self, event_name, callback = Logger.write_to_file):
        self._observables[event_name] = callback

class Event:
    def __init__(self, name, after_changes, before_changes, par = None, action = True):
        self._name = name
        self._after_changes = after_changes
        self._before_changes = before_changes
        self._par = par

        if action:
            self.do_event()

    def do_event(self):
        for observer in Observer._observers:
            if self._name in observer._observables:
                observer._observables[self._name](self)

    def __str__(self):
        return f"Event({self._name},new list: {self._after_changes} (old list: {self._before_changes})"