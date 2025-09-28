def perform_operation(num1, num2, operation):

  match operation:

    case "add" :
      return num1 + num2 
    
    case "subtract":
      return num1 - num2
    
    case "multiply":
      return num1*num2
    
    case "divide":
      if num2 != 0:
        result = num1 / num2
        print(f"The result is {result}")
      else:
        print("cnat divide by 0")


        

