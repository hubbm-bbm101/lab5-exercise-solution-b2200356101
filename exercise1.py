def main():
    try:
        inpt=int(input("Please enter a number:"))
        print("Sum of odd numbers: {}\nAverage of even numbers: {}".format(sum_of_odds(inpt) , average_of_evens(inpt)))
    except:
        print("Your input is not a number. Please enter a number:")
        main()

def sum_of_odds (number):
    return sum([x for x in range (0,number+1) if x/2 != 0])

def average_of_evens (number):
    even = ([x for x in range (0,number+1) if x%2 == 0])
    return sum(even) / len(even)

main()
