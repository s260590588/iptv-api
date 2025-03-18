class DataManager:
    _instance = None
    data = []

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DataManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def save_data(self, data):
        self.data = data
