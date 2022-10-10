class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        Sol = list()
        
        for num in range(1,n+1):
            if(num%3==0 and num%5==0):
                Sol.append("FizzBuzz")
            elif(num%3==0):
                Sol.append("Fizz")
            elif(num%5==0):
                Sol.append("Buzz")
            else:
                Sol.append(str(num))
        return Sol
