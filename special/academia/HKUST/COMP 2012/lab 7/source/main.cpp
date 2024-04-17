#include "RandomForest.h"
#include <iostream>
using namespace std;

// Warning: Do not change anything
int main(int argc, char *argv[]){
    const char *label_names[3] = {"Versicolor","Setosa","Virginica"};
    RandomForest Forest;
    DecisionTree Tree;
    
    int NumberOfTrees,position,height,split_value,attribute,label;
    cout << "Enter Number of Trees: \n";
    // Input the number of trees. If NumberOfTrees = 1, then we treat the RandomForest as a Desicion tree 
    cin >> NumberOfTrees;
    if(NumberOfTrees > 1)Forest.InitializeForest(NumberOfTrees);
    // Read trees
    for(int i = 0; i < NumberOfTrees; i++){
        cout << "Inserting Tree : " << i << endl;
        // Read all decision nodes
        // To stop inserting new decision nodes, set height = -1. Note that to add a node, its parent must exist
        // Decision nodes are inserted in the following order : height -> position -> split_value -> attribute
        while(true){
            cin >> height;
            if(height == -1)break;
            cin >> position;
            cin >> split_value;
            cin >> attribute;
            if(NumberOfTrees > 1)Forest.Trees[i].AddDecisionNode(attribute,split_value,position,height);
            else Tree.AddDecisionNode(attribute,split_value,position,height);
        }
        // Similarly, read all end nodes of the i-th tree. Note that there should be no decision node without children
        // End nodes are inserted in the following order :  height -> position -> label
        while(true){
            cin >> height;
            if(height == -1)break;
            cin >> position;
            cin >> label;
            if(NumberOfTrees > 1)Forest.Trees[i].AddEndNode(label,position,height);    
            else Tree.AddEndNode(label,position,height);
        }
    }
    if(NumberOfTrees > 1) cout << "Forest Initialized!" << endl;
    else cout << "Tree Initialized!" << endl;
    //for(int i = 0; i < NumberOfTrees; i++)Forest.Trees[i].PrintLabels();
    
    int x[4];
    // Read test points. This is the easiest part to modify in the given file
    while(true){
        cout << "Enter Test Point: \n";
        cin >> x[0];
        if(x[0] == -1)break;
        cin >> x[1];
        cin >> x[2];
        cin >> x[3];
        cout << "Predicted Label : ";
        if(NumberOfTrees > 1)cout << label_names[Forest.ForestPredict(x)] << endl;
        else cout << label_names[Tree.TreePredict(x)] << endl;
    }

    return 0;
}