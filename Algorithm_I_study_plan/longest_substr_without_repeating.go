package main

import "math"

func lengthOfLongestSubstring(s string) int {
    start := 0;
    maxlen := 0;
    
    seen := make(map[rune]int);
    
    for i, c := range s {
        if _, exists := seen[c]; exists && start <= seen[c] {
            start = seen[c] + 1;
        } else {
            maxlen = int(math.Max(float64(maxlen), float64(i - start + 1)));
        }
        seen[c] = i;
    }
    return maxlen;
}