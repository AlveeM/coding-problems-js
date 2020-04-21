function TreeNode(val) {
    this.val = val;
    this.left = this.right = null;
}

/**
 * @param {number[]} preorder
 * @return {TreeNode}
 */
var bstFromPreorder = function (preorder) {
  // var: track index in preorder
  let i = 0;
  // var: root; call constructBST function with
  let root = constructBST(Number.MAX_SAFE_INTEGER);
  // return root
  return root;

  /**
   * @param {number} upperBound
   * @return {TreeNode}
  */
  function constructBST(upperBound) {
    // var: current value
    const val = preorder[i]

    // edge: index out of bound or current value > upperBound
    if (i == preorder.length || val > upperBound) {
      return null;
    }

    // var: new node
    const node = new TreeNode(val);
    i++;

    // construct left
    node.left = constructBST(node.val);
    // construct right
    node.right = constructBST(upperBound);

    return node;
  }
};

console.log(bstFromPreorder([8,5,1,7,10,12]));