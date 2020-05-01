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
 * @param {number[]} arr
 * @return {boolean}
 */
function isValidSequence(root, arr) {
  if (!root) return arr.length == 0;
  return isValid(root, arr, 0);
};

function isValid(root, arr, idx) {
  if(root.val != arr[idx]) return false;
  if(idx == arr.length - 1) {
    return root.left == null && root.right == null;
  }
  return ((root.left != null && isValid(root.left, arr, idx+1))
          || (root.right != null && isValid(root.right, arr, idx+1)));
}