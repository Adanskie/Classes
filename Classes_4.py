class Menu:
    data = []

    def __init__(self):

        while True:
            Menu.create_choices(self)
            choices = input("Enter a number : ")

            if choices == "1":
                self.show_all_data()

            elif choices == "2":
                self.added_single_data()

            elif choices == "3":
                self.added_multiple_data()

            elif choices == "4":
                self.Delete_data()

            elif choices == "5":
                self.Delete_all_data()

            elif choices == "6":
                self.update_data()

            elif choices == "7":
                print("EXIT -> THANKYOU")
                break


    def create_choices(self):
        print("==========Menu===========")
        print("Press [1] SHOW ALL DATA")
        print("Press [2] ADDED SINGLE DATA")
        print("Press [3] ADDED MULTIPLE DATA")
        print("Press [4] DELETE")
        print("Press [5] DELETE ALL DATA")
        print("Press [6] UPDATE DATA")
        print("Press [7] EXIT")


    def show_all_data(self):
        if Menu.data:
            print("\n==========================")
            for get_value in Menu.data:
                print(get_value)
            print("==========================\n")
        else:
            print("Something Wrong")


    def added_single_data(self):
        single_data = input("Enter value for single data : ")
        self.data.append(single_data)
        print("\n=========================")
        print("Success added single data")
        print("=========================\n")


    def added_multiple_data(self):
        multiple_data = int(input("How many data (enter number) : "))
        for _ in range(multiple_data):
            user = input("Enter a data : ")
            self.data.append(user)
        print("\n==========================")
        print("Success adding multiple data")
        print("===========================\n")

    def Delete_data(self):
        if self.data:
            print("\n==========choices index number============")
            num = 0
            for get_value in self.data:
                print(num , " -",get_value)
                num += 1
            print("===========================================\n")
            index = int(input("Enter index number for delete : "))
            self.data.pop(index)
            print("\n============================\nSuccess delete account\n============================\n")
        else:
            print("Something Wrong")

    def Delete_all_data(self):
        self.data.clear()
        print("\n============================================================")
        print("Success Delete all data")
        print("=============================================================\n")

    def update_data(self):
        if self.data:
            print("\n==========choices index number============")
            num = 0
            for get_value in self.data:
                print(num , " -",get_value)
            print("===========================================\n")
            index_number = int(input("choice index number for update : "))
            value = input("Enter value for update : ")
            self.data[index_number] = value

            print("\n==============================\nSuccess updating value\n========================================\n")
        else:
            print("Something Wrong")

Menu()
