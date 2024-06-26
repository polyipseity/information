

class DecisionTree {
private:
    class Node{
    public:
        // split attribute of a (decision) node.
        //You can assume that the attribute is a positive number (>= 0). 
        // If X is a data point of size N, then the i-th attribute will correspond to the i-th entry of X. 
        int split_attribute;
        // split value of a (decision) node.
        int split_value;
        // Label of a (end) node 
        int label;
        // Pointers to the children of the node
        DecisionTree *left = nullptr,*right = nullptr;
        // Constructors
        Node() = default;
        // Used when we want to initialize a decision-node
        Node(int split_value, int split_attribute) : split_attribute(split_attribute),split_value(split_value),label(0) {}
        // Used when we want to initialize an end-node
        Node(int label):split_attribute(0),split_value(0), label(label){} 
        ~Node(){
            delete left;
            delete right;
        }

        // Task 1 (Step 1): Implement Tree prediction
        bool IsEndNode(){
            return !left || left->is_empty() || !right || right->is_empty();
        }
    };
   Node* root = nullptr;
    
public:
    
    // Constrcutors For a decision tree
    DecisionTree() = default;
    DecisionTree(Node *node) 
    {
        root = node; 
    }
    ~DecisionTree() {
        if (root != nullptr) {
            delete root;
        }
    }
    bool is_empty() const { return root == nullptr; }
    
    // Functions used to add decision and end nodes.
    // WARNING : Do not modify these methods 
    // height : corresponds to the height (heigth = 0 is the root)
    // position : corresponds to the relative position of the node (a value between 0 and 2^height)
    // add a decision node with the given split value and split attribute at the position and height 
    void AddDecisionNode( int attribute, int split_value, int &position, int &height);
    // add an end node with the given a label at the position and height 
    void AddEndNode( int label, int &position, int &height);
    
    // Task 1 (Step 2): Implement Tree prediction
    int TreePredict(int *x);
};


