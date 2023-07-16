func canCompleteCircuit(gas []int, cost []int) int {
    total_gas := 0 // total gas will be non-negative if a cycle is possible
    local_gas := 0
    start := 0
    for i := 0; i < len(gas); i++ {
        total_gas += gas[i] - cost[i]
        local_gas += gas[i] - cost[i]
        if local_gas < 0 { // cant finish from `start` without going -ve
            local_gas = 0
            start = i+1
        }
    }

    if total_gas >= 0 {
        return start
    }
    return -1
}