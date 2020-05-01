/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxPathSum = function (root) {
  // var: track global max sum
  var globalMaxSum = -Infinity;
  // make recursive call
  maxPathSumRec(root);
  // return global max sum
  return globalMaxSum;


  function maxPathSumRec(curNode) {
    // base: node is null
    if (curNode == null) return 0;

    // var: sum of left nodes; traverse left
    var leftMaxPathSum = maxPathSumRec(curNode.left);
    // var: sum of right nodes; traverse right
    var rightMaxPathSum = maxPathSumRec(curNode.right);

    // update left sum; ignore negative sums
    leftMaxPathSum = Math.max(leftMaxPathSum, 0);
    // update right sum; ignore negative sums
    rightMaxPathSum = Math.max(rightMaxPathSum, 0);

    // var: sum at current node (L subtree + R subtree + node val)
    var localMaxSum = leftMaxPathSum + rightMaxPathSum + curNode.val;
    // update global max sum; max between local max and current global
    globalMaxSum = Math.max(globalMaxSum, localMaxSum);

    // return: (max between current left and right sum) + current val
    return Math.max(leftMaxPathSum, rightMaxPathSum) + curNode.val;
  }
};