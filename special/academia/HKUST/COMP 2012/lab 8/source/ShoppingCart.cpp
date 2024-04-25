#include "ShoppingCart.h"
#include <numeric>

// TODO1: Implement the addProduct method in the ShoppingCart class.
// Objective: Understand how to use std::vector to store and manage a collection of objects.
// Hints: You can directly use STL algorithm for implement.
void ShoppingCart::addProduct(const Product& product) {
    products.emplace_back(product);
}

// TODO2: Implement the getTotalPrice method in the ShoppingCart class.
// Objective: Understand how to use STL algorithms to operate elements from a vector.
double ShoppingCart::getTotalPrice() const {
    return std::accumulate(std::begin(products), std::end(products), 0., [](double left, Product const &right)
                           { return left + right.price; });
}

// TODO3: Implement the removeProduct method in the ShoppingCart class, which removes the product from cart.
// Objective: Understand how to use STL algorithms to search and remove an element from a vector.
// Hints: You can use find_if() & erase() or erase() & remove_if() for implement.
void ShoppingCart::removeProduct(const std::string& productName) {
    products.erase(std::remove_if(std::begin(products), std::end(products), [&productName](Product const &right)
                                  { return right.name == productName; }),
                   std::end(products));
}

// TODO4.1: Implement the sortByPrice method in the ShoppingCart class.
// Objective: Understand how to use STL algorithms to sort a vector of objects based on a specific criteria.
// You can Use the std::sort algorithm to sort the products vector and define a lambda function or a functor to specify the sorting criteria based on the price member of the Product class.
void ShoppingCart::sortByPrice() {
    std::sort(std::begin(products), std::end(products), Product::compareByPrice);
}

// TODO4.2: Implement the sortByName method in the ShoppingCart class.
// Objective: Understand how to use STL algorithms to sort a vector of objects based on a specific criteria.
void ShoppingCart::sortByName() {
    std::sort(std::begin(products), std::end(products), [](Product const &left, Product const &right)
              { return left.name < right.name; });
}

// TODO5: Implement the applyDiscount method in the ShoppingCart class.
// Hints: You can use std::transform.
void ShoppingCart::applyDiscount(double discountRate) {
    std::transform(std::begin(products), std::end(products), std::begin(products), [discountRate](Product const &element)
                   {
        Product ret{element};
        ret.price *= discountRate;
        return ret; });
}

// TODO6: Implement the getProductsInPriceRange method in the ShoppingCart class.
std::vector<Product> ShoppingCart::getProductsInPriceRange(double minPrice, double maxPrice) {
    std::vector<Product> ret{};
    std::copy_if(std::begin(products), std::end(products), std::back_inserter(ret), [minPrice, maxPrice](Product const &element)
                 { return minPrice <= element.price && element.price <= maxPrice; });
    return ret;
}

// GIVEN: Implement the getExpensiveProducts method in the ShoppingCart class.
// You should filter out expensive products (>threshold) and sort them by price;
// Hints: You can use std::copy_if algorithm and std::sort algorithm, you also need compareByPrice() and isExpensive().
std::vector<Product> ShoppingCart::getExpensiveProducts(double threshold) const {
    std::vector<Product> expensiveProducts;

    std::copy_if(products.begin(), products.end(), std::back_inserter(expensiveProducts),
                [&threshold](const Product& p) { return Product::isExpensive(p, threshold); });

    std::sort(expensiveProducts.begin(), expensiveProducts.end(), Product::compareByPrice);
    return expensiveProducts;
}
