class Computer:
    def config(self):
        print("hpa")


Computer().config()
com1 = Computer()
Computer.config(Computer)
Computer.config(com1)
com1.config()