
def fizzbuzz():
    max_num = int(input("Up to which number do you want to count?: "))
    nums = [3, 5]

    for i in range(0, max_num + 1):
        output = ''

        if i % nums[0] == 0:
            output = 'Fizz'

        if i % nums[1] == 0:
            output += "Buzz"

        print(output or i)


fizzbuzz()
