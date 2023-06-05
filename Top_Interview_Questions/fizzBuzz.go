func fizzBuzz(n int) []string {
    result := make([]string, n)
    for idx, _ := range result {
        i := idx + 1
        if i % 3 == 0 && i % 5 == 0 {
            result[idx] = "FizzBuzz"
        } else if i % 3 == 0 {
            result[idx] = "Fizz"
        } else if i % 5 == 0 {
            result[idx] = "Buzz"
        } else {
            result[idx] = fmt.Sprint(i)
        }
    }
    return result
}