func isHappy(n int) bool {
    slow, fast := n, n
    for true {
      slow = sumSquareDigs(slow)
      fast = sumSquareDigs(sumSquareDigs(fast))
      if slow == fast {
        break
      }
    }

    return slow == 1
}


func sumSquareDigs(n int) int {
  sum := 0
  for true {
    dig := n % 10
    sum += dig * dig
    n /= 10
    if n < 10 {
      sum += n * n
      break
    }
  }
  return sum
}