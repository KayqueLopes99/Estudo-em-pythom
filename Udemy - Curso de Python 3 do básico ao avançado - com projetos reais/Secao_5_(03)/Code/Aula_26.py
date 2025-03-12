class CallMe:

    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self, name):
        print(name, "Chama", self.phone)
        return 2134
    

call1 = CallMe("1234567890")
return_ = call1("Kayque")
print(return_)