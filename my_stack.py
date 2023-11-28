import os

class ArrayStack:
    def __init__(self, capacity = 10) -> None:
        self.capacity = capacity
        self.list = [None]*capacity
        self.top = -1

    def isEmpty(self) -> bool:
        return self.top == -1
    
    def isFull(self) -> bool:
        return self.top == self.capacity-1
    
    def push(self, item) -> None:
        if self.isFull():
            print("Error: Stack is full")
            return
        
        self.top += 1
        self.list[self.top] = item
    
    def pop(self) -> int:        
        if not self.isEmpty():
            temp = self.list[self.top]
            self.list[self.top] = None
            self.top -= 1
            return temp
        
        print("Error: Stack is empty")
    
    def peek(self) -> int:
        if not self.isEmpty():
            return self.list[self.top]
        
        print("Error: Stack is empty")
        
    def deleteAll(self) -> None:
        while not self.isEmpty():
            self.pop()
    
    def reverse(self):
        self.list[:self.top+1] = self.list[self.top::-1]
        
    def __str__(self) -> str:
        result = ""
        
        for i in reversed(range(self.capacity)):
            result += "| {0} |".format(self.list[i])
            result += " <- top\n" if i == self.top else "\n"

        return result

def init():
    os.system("cls")
    print("""push: 삽입
pop: 삭제 후 반환
peek: 반환
delete: 스택 초기화
reverse: 스택 역순으로 배열
print: 스택 출력
cls: 화면 초기화
exit: 시스템 종료""")

stack = ArrayStack()

init()
print(">>> ", end="")

while True:
    choice = input()
    
    if choice == 'push':
        stack.push(int(input("정수를 입력해주세요: ")))
        init()
    
    elif choice == 'pop':
        print(stack.pop())
    
    elif choice == "peek":
        print(stack.peek())
    
    elif choice == "delete":
        stack.deleteAll()
        init()
    
    elif choice == "reverse":
        stack.reverse()
        init()
    
    elif choice == 'print':
        print(stack)
    
    elif choice == 'exit':
        break

    print(">>> ", end="")