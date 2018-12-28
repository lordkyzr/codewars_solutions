function calculate(num1, operation, num2) {
    if(operation == "/" && num2 == 0){
      return null
    }
    let result = 0;
    if(operation == "+"){
      result = num1 + num2
    } else if (operation == "-"){
      result = num1 - num2
    } else if(operation == "*"){
      result = num1 * num2
    } else if(operation == "/"){
      result = num1 / num2
    } else {
      return null
    }
    
    if(result === -0){
      return 0;
    } else {
      return result
    }
    
}