#include <iostream>
#include <vector>
#include <algorithm>

class Product {
private:
    std::string name;
    double price;
    
public:
    Product(const std::string& n, double p) : name(n), price(p) {}

    static bool compareByPrice(const Product& p1, const Product& p2) {
        return p1.price < p2.price;
    }

    static bool isExpensive(const Product& p, float threshold) {
        return p.price > threshold;
    }

    void print() const {
        std::cout << "- " << name << " ($" << price << ")\n";
    }

    friend class ShoppingCart;
};

class ShoppingCart {
private:
    std::vector<Product> products;

public:
    void addProduct(const Product& product);
    void removeProduct(const std::string& productName);
    double getTotalPrice() const;
    void sortByPrice();
    void sortByName();
    void applyDiscount(double discountRate);
    std::vector<Product> getExpensiveProducts(double threshold) const;
    std::vector<Product> getProductsInPriceRange(double minPrice, double maxPrice);

    void displayProducts() const {
        std::cout << "Products in the shopping cart:\n";
        for (const Product& product : products) {
            product.print();
        }
    }
};