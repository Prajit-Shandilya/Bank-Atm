class  Atm:
    def __init__(self,cardno,pin):
        self.cardno=cardno
        self.pin=pin
    def checkBalance(self):
        print("Your balance is 200000")
    def debitAmount(self,amount):

        leftAmount=200000-amount
        print("you have withdrawn :"+str(amount)+"Your remaining balance is:"+str(leftAmount))

def main():
    cardNo=input("Enter your card no.:")    
    pinNo=input("Enter your pin:") 
 
    atmCard=Atm(cardNo,pinNo)

    print("Choose your action:")
    print("1.Balance Enquiry  2.Withdrawlat")
    action=int(input("enter your choice:"))

    if(action==1):
        atmCard.checkBalance()
    elif(action==2):
        amount=int(input("enter your anount to be withdrawl:"))
        atmCard.debitAmount(amount)
    else:
        print("enter a valid choice")
        
            
if __name__=="__main__":
    main()
            

    