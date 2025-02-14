class DictToList:
    def __init__(self, input_dict):
        self.input_dict = input_dict

    def convert(self):
        self.keys_list = [key for key in self.input_dict]
        self.values_list = [self.input_dict[key] for key in self.input_dict]

    def display(self):
        print("Keys List:", self.keys_list)
        print("Values List:", self.values_list)


sample_dict = {"name": "Aditi", "age": 22, "city": "Dhanbad"}
obj = DictToList(sample_dict)

obj.convert()
obj.display()
