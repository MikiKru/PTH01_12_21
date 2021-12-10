class PrepaidPhoneError(Exception):
    def __init__(self, msg):
        self.__msg = msg
    def __str__(self):
        return self.__msg

class PrepaidPhone:
    def __init__(self, limit=100):
        self.limit = limit
    def get_limit(self):
        return self.limit
    def add_to_limit(self, add_limit):
        self.limit += add_limit
    def call(self, call_limit):
        try:
            if self.limit == 0:
                raise TypeError("You have empty account. Call is interupted")
            self.limit -= call_limit
            if self.limit < 0:
                raise PrepaidPhoneError("You have reached the limit. Re-charging phone.")
            print("Call finished. Actual account status: " + str(self.get_limit()))
        except TypeError as e:
            print(e)
            print("You have to add money to your account")
        except PrepaidPhoneError as e:
            print(e)
            self.add_to_limit(abs(self.limit))
            print(self.limit)

prepaidphone = PrepaidPhone(100)
prepaidphone.call(60)
prepaidphone.call(60)
prepaidphone.call(10)
