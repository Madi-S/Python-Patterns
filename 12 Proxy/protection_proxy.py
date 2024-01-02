

class Car:
    def __init__(self, driver):
        self.driver = driver
    
    def drive(self):
        print(f'Car is being driven {self.driver.name}')


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(driver)
    
    def drive(self):
        if self.driver.age >= 16:
            self._car.drive()
        else:
            print('Alert, driver is too young')
        


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
if __name__ == '__main__':
    driver = Driver('Alex', 14)
    # car = Car(driver)
    # car.drive()
    car = CarProxy(driver)
    car.drive()
    