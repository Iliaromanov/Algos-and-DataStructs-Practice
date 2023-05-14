func longestCommonPrefix(strs []string) string {
    count := 0;
    stop := false;
    for !stop {
        if len(strs[0]) <= count {
            break;
        }
        cur_c := []rune(strs[0])[count];
        for _, s := range strs {
            if len(s) <= count || []rune(s)[count] != cur_c {
                count -= 1;
                stop = true;
                break;
            }
        }
        count += 1;
    }
    prefix := strs[0][:count];
    return prefix;
}