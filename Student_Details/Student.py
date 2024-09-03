class Students:
    type = "bio"

    def __init__(self,name,roll_no,section):
        self.name = name
        self.roll_no = roll_no
        self.section = section

    def fun(self):
        print("the details are name=={} roll_no=={} and section=={}".format(self.name,self.roll_no,self.section))