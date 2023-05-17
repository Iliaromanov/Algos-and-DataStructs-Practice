func bruteForce(haystack string, needle string) int {
    if len(haystack) < len(needle) {
        return -1;
    }

    start, end := 0, len(needle) - 1;

    for end < len(haystack) {
        var i int;
        for i = start; i <= end; i++ {
            if needle[i - start] != haystack[i] {
                start++;
                end = start + len(needle) - 1;
                break; 
            }
        }
        if i > end {
            return start;
        }
    }
    return -1;
}


// beats 100% speed
func BoyerMoore(haystack string, needle string) int {
    if len(needle) > len(haystack) {
        return -1;
    }

    // compute last occurence map
    L := make(map[rune]int);
    for i, char := range needle {
        L[char] = i;
    }

    n, m := len(haystack), len(needle);
    i, j := m - 1, m - 1;
    for i < n && j >= 0 {
        if haystack[i] == needle[j] {
            i--;
            j--;
        } else {
            last, found := L[rune(haystack[i])];
            if !found {
                last = -1;
            }
            // cus Go doesn't have a min function
            if last > j {
                i += m - 1 - (j - 1);
            } else {
                i += m - 1 - last;
            }
            j = m - 1;
        }
    }
    if j == -1 {
        return i + 1;
    }
    return -1;
}
