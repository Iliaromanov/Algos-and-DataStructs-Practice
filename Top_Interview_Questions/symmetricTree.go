/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

 // cleaner recursive solution (my second attempt)
 func isSymmetric(root *TreeNode) bool {
    return root == nil || helper(root.Left, root.Right)
}

func helper(left *TreeNode, right *TreeNode) bool {
    if left == nil || right == nil {
        return left == right;
    }
    if left.Val != right.Val {
        return false;
    }

    return helper(left.Left, right.Right) && helper(left.Right, right.Left);
}


// complex BFS solution (my first attempt)
 func isSymmetricBFS(root *TreeNode) bool {
    if root == nil {
        return true;
    }
    if root.Left == nil {
        return root.Right == nil;
    }

    if root.Right == nil {
        return root.Left == nil;
    }

    queue := make([]*TreeNode, 0);
    queue = append(queue, root);
    for len(queue) > 0 {
        // fmt.Println("queue: ", queue);
        level_len := len(queue);
        if level_len == 1 { 
            if queue[0] != nil {
                queue = append(queue, queue[0].Left);
                queue = append(queue, queue[0].Right);
            }
            queue = queue[1:]; // pop
            continue;
        }
        if level_len % 2 != 0 {
            return false;
        }
        // check palindrome
        l, r := 0, level_len - 1;
        for l < r {
            // if only one of the queue values is nil
            if (queue[l] == nil && queue[r] != nil) || 
               (queue[r] == nil && queue[l] != nil) {
                return false;
            }

            if queue[l] == nil && queue[r] == nil {
                l++;
                r--;
                continue;
            }

            // if neither of the queue vals are nil
            //  and they differ in value
            if queue[l].Val != queue[r].Val {
                return false;
            }
            l++;
            r--;
        }
        // add next level
        for level_len > 0 {
            if queue[0] != nil {
                queue = append(queue, queue[0].Left);
                queue = append(queue, queue[0].Right);
            }
            queue = queue[1:]; // pop
            level_len--;
        }
    }
    return true;
}