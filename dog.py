class Dog():
    def __init__(self, dog_image, dog_name):
        self.dog_image = dog_image
        self.dog_name = dog_name

class Breed(Dog):
    def __init__(self, dog_image, dog_name, breed_size):
        Dog.__init__(self, dog_image, dog_name)
        self.breed_size = breed_size


class DogInfo(Dog):
    def __init__(self, dog_image, dog_name, age, sex, additional_info):
        Dog.__init__(self, dog_image, dog_name)
        self.age = age
        self.sex = sex
        self.additional_info = additional_info


