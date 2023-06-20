func sortColors(nums []int)  {
    red, white, blue := 0, 0, 0
    for i := 0; i < len(nums); i++ {
        switch nums[i] {
            case 0:
                red++
            case 1:
                white++
            default:
                blue++
        }
    }
    
    for i := 0; i < red; i++ {
        nums[i] = 0
    }
    for i := 0; i < white; i++ {
        nums[i + red] = 1
    }
    for i := 0; i < blue; i++ {
        nums[i + white + red] = 2
    }
}