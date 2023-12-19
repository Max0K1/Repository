class SingletonCarDealer:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonCarDealer, cls).__new__(cls)
        return cls._instance

  
car_dealer1 = SingletonCarDealer()
car_dealer2 = SingletonCarDealer()

print(car_dealer1 is car_dealer2)