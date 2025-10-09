#include "DecisionTree.h"

void DecisionTree::AddDecisionNode( int attribute, int split_value, int &position, int &height) {
    height--;
    if (height == -1) {
        root = new Node(split_value,attribute);
    }else{
        if(position < (1<<height)){
            if(root->left == nullptr){
                root->left = new DecisionTree(new Node(split_value, attribute));
            }else{
                root->left->AddDecisionNode( attribute, split_value,position,height);
            }
        }else{
            position -= (1<<height);
            if(root->right == nullptr){
                root->right = new DecisionTree(new Node(split_value, attribute));
            }else{
                root->right->AddDecisionNode( attribute, split_value,position,height);
            }
        }
    }
}

void DecisionTree::AddEndNode( int label, int &position, int &height) {
    height--;
    if (height == -1) {
        root = new Node(label);
    }else{
        if(position < (1<<height)){
            if(root->left == nullptr){
                root->left = new DecisionTree(new Node(label));
            }else{
                root->left->AddEndNode(label,position,height);
            }
        }else{
            position -= (1<<height);
            if(root->right == nullptr){
                root->right = new DecisionTree(new Node(label));
            }else{
                root->right->AddEndNode(label,position,height);
            }
        }
    }
}



// TODO 1 :
// Takes as input the test point x
// Returns the predicted label using the rules as described in the website
int DecisionTree::TreePredict( int *x) {
    // You can change this
    if (is_empty())
        return 0;
    Node &root{*this->root};
    if (root.IsEndNode())
        return root.label;
    return (x[root.split_attribute] <= root.split_value ? root.left : root.right)->TreePredict(x);
}



