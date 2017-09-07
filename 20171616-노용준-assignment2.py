n = int(input("Enter a number : "))

while True :
        if n == -1 :
                break
        elif n<0 :
                print("계산할 수 없습니다. 수를 다시 입력해주세요.")
                n = int(input("Enter a number : "))
                continue
        elif n==0 :
                print( n, "! = 1")
                n = int(input("Enter a number : "))
                continue               
        else :
                while n>0:
                        result = 1
                        for i in range (1,n+1):
                                result *= i
                                if i == n :
                                        print( n, "! = ",result)
                                        continue
                        n = int(input("Enter a number : "))
                continue



                
        
        

                
