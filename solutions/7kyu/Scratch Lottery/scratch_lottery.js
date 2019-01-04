function scratch(lottery){
    let total = 0;
    for(i = 0; i < lottery.length; i++){
      let line = lottery[i];
      let items = line.split(" ");
      if(items[0] === items[1] && items[0] === items[2]){
        total = total + parseInt(items[3])
      }
    }
    return(total);
  }