/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var diameterOfBinaryTree = function (root) {
  // declare var: store diameter; init to 0
  let diameter = 0;
  // call heightOfBT with root
  heightOfBT(root);
  // return diameter
  return diameter;

  function heightOfBT(node) {
    // if: no node; return 0
    if (node == null) return 0;
    // declare var: store result of traversing left node
    const leftTreeHeight = heightOfBT(node.left);
    // declare var: store result of traversing right node
    const rightTreeHeight = heightOfBT(node.right);
    // update diameter: max val between current and new diameter
    diameter = Math.max(diameter, leftTreeHeight + rightTreeHeight);
    // return max height
    return Math.max(leftTreeHeight, rightTreeHeight) + 1;
  }
};

