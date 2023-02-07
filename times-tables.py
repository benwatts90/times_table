# Iterator times table program
# User enters number to get a looped iterator of the multiplication of the number up to 10
print("Enter a number to get a list of the number's multiplications up to 10")
a = int(input("Enter number to be multiplied, then press 'Enter': "))

class TimesTables:
    def __iter__(self):
        self.multiple = 1
        self.table = a
        return self

    def __next__(self):
        x = self.multiple

        if self.multiple <= 10:
            self.multiple += 1
            y = self.table
            return x * y
        else:
            raise StopIteration

myClass = TimesTables()
myIter = iter(myClass)

for x in myIter:
    print(x)