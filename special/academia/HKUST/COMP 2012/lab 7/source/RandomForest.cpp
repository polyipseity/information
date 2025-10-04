#include "RandomForest.h"

// TODO 2:
// Take as input the test point x.
// Compute the predictions for every tree in the forest
// Find and return the majority label
int RandomForest::ForestPredict( int *x) {
    // You can change this
    int counts[3]{};
    for (int idx{}; idx < NumberOfTrees; ++idx)
        ++counts[Trees[idx].TreePredict(x)];
    int max{}, label{};
    for (int idx{}; idx < sizeof(counts) / sizeof(*counts); ++idx)
    {
        if (counts[idx] > max)
        {
            max = counts[idx];
            label = idx;
        }
    }
    return label;
}