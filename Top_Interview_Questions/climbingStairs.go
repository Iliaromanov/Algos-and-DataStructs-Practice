func climbStairs(n int) int {
    if n == 1 {
        return 1;
    }
    if n == 2 {
        return 2;
    }

    two_behind := 1;
    one_behind := 2;
    var ans int;
    for i := 3; i <= n; i++ {
        ans = one_behind + two_behind;
        two_behind = one_behind;
        one_behind = ans;
    }

    return ans;
}