#include "DecisionTree.h"

class RandomForest {
public:
    // Number of trees a forest has
    int NumberOfTrees;
    // An array of decision trees
    DecisionTree *Trees = nullptr;    
    RandomForest() = default;
    RandomForest(int NumberOfTrees): NumberOfTrees(NumberOfTrees){
        Trees = new DecisionTree[NumberOfTrees];
    }
    ~RandomForest(){
        if(Trees != nullptr){
            delete[] Trees;
        }
    }
    void InitializeForest(int NumberOfTrees){
        this->NumberOfTrees = NumberOfTrees;
        Trees = new DecisionTree[NumberOfTrees];
    }
    // TODO 2: Implement Forest Prediction
    int ForestPredict(int *x);
};