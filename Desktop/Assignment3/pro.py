class Post(dict):
    """
    The Post class is responsible for working
    with individual user posts. It currently
    supports two features: A timestamp property
    that is set upon instantiation and
    when the entry object is set and an entry
    property that stores the post message.
    """

    def __init__(self, entry: str = None, timestamp: float = 0):
        self._timestamp = timestamp
        self.set_entry(entry)

        # Subclass dict to expose Post properties for serialization
        # Don't worry about this!
        dict.__init__(self, entry=self._entry, timestamp=self._timestamp)

    def set_entry(self, entry):
        self._entry = entry
        dict.__setitem__(self, 'entry', entry)

        # If timestamp has not been set, generate a new one using time module
        if self._timestamp == 0:
            self._timestamp = time.time()

    def get_entry(self):
        return self._entry

    def set_time(self, time: float):
        self._timestamp = time
        dict.__setitem__(self, 'timestamp', time)

    def get_time(self):
        return self._timestamp

    """
    The property method is used to support get
    and set capability for entry and
    time values. When the value for entry is
    changed, or set, the timestamp field is
    updated to the current time.
    """
    entry = property(get_entry, set_entry)
    timestamp = property(get_time, set_time)