
from lab4a import Deque

def wordToDeque(input):
    d = Deque()
    for ch in input:
        d.push(ch)
    return d

def OffByOne(char1, char2):
    d = Deque()
    d.push(char1)
    d.push(char2)

    first = d.pop_front()
    second = d.pop()

    return (abs(ord(first) - ord(second))) == 1

def OffByN(char1, char2, N):
    d = Deque()
    d.push(char1)
    d.push(char2)

    first = d.pop_front()
    second = d.pop()

    return abs(ord(first) - ord(second)) == N

def testWordToDeque(test_string, test_deque):
    temp = test_deque
    for i in range(len(test_string)):
        if temp.front == None or test_string[i] != temp.front.item:
            return False
        else:
            temp.front = temp.front.next
    if temp.front != None:
        return False
    return True



test1_string = "hello"
test1_deque = wordToDeque(test1_string)
print(testWordToDeque(test1_string, test1_deque)) # Should return True

char1 = 'b'
char2 = 'a'
print(OffByOne(char1, char2)) #print True

char1 = 'b'
char2 = 'e'
N = 3
print(OffByN(char1, char2, N)) #Prints True