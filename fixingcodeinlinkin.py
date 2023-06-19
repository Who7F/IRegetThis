#input is a key word, so I was unable to use it
#4 methods all doing the same thing.
#3rd method is make easyer to under stard the 2nd method
#Input need to be an int space int
#I think 4th method which I copy form the reply

def metA(screenInput):
    ni = screenInput.split(' ')
    x = int(ni[0])
    y = int(ni[1])
    sum = x + y
    diff = x - y
    print(str(sum) + str(diff))

def metB(screenInput):
    x, y = [int(i) for i in screenInput.split()]
    print(f'{x+y}{x-y}')

def metC(screenInput):
    list = []
    for i in screenInput.split():
        list.append(int(i))
    x = list[0]
    y = list[1]
    sum = x + y
    diff = x - y
    print(str(sum) + str(diff))    

def metD(screenInput):
    x,y = list(map(int, screenInput.split()))
    print(f'{x+y}{x-y}')
   
def main():
    #Input is not screened. However the methods are scooped
    screenInput = input(':')
    metA(screenInput)
    metB(screenInput)
    metC(screenInput)
    metD(screenInput)

if __name__=='__main__':
    main()
