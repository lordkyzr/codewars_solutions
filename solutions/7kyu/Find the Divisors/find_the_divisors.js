function divisors(inputInteger) {
    let returnArray = []
    for(i = 2;i <= inputInteger / 2;i++){
      if(inputInteger % i === 0){
        returnArray.push(i);
      }
    }
    
    if(returnArray.length === 0){
      return inputInteger.toString() + ' is prime'
    } else {
      return returnArray;
    }
  };