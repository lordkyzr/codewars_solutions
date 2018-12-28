package kata

func GetCount(str string) (count int) {
  for _, value := range str {
      switch value {
      case 'a', 'e', 'i', 'o', 'u':
          count++
      }
  }
  
  return count
}