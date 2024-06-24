#include <iostream>
#include <algorithm>
#include "ShoppingCart.h"

int main() {

    int test;
    std::cin >> test;
    ShoppingCart cart1;
    ShoppingCart cart2;
    ShoppingCart cart3;
    ShoppingCart cart4;
    ShoppingCart cart5;
    ShoppingCart cart6;

    std::vector<Product> expensiveProducts4;
    std::vector<Product> expensiveProducts5;
    std::vector<Product> Products6;
    switch (test) {
        case 1:
            std::cout << "\n================================Case1================================\n";
            cart1.addProduct(Product("Shirt", 29.99));
            cart1.addProduct(Product("Jeans", 49.99));
            cart1.addProduct(Product("Shoes", 79.99));
            cart1.addProduct(Product("Watch", 99.99));
            cart1.addProduct(Product("Hat", 19.99));

            cart1.displayProducts();
            std::cout << "Total price: $" << cart1.getTotalPrice() << "\n";

            cart1.removeProduct("Shoes");
            cart1.displayProducts();
            std::cout << "Total price: $" << cart1.getTotalPrice() << "\n";
        break;
        case 2:
            std::cout << "\n================================Case2================================\n";

            cart2.addProduct(Product("Shirt", 29.99));
            cart2.addProduct(Product("Jeans", 49.99));
            cart2.addProduct(Product("Shoes", 79.99));
            cart2.addProduct(Product("Watch", 99.99));
            cart2.addProduct(Product("Hat", 19.99));

            cart2.sortByPrice();
            cart2.displayProducts();
            std::cout << "Total price: $" << cart2.getTotalPrice() << "\n";
        break;
        case 3:
            std::cout << "\n================================Case3================================\n";

            cart3.addProduct(Product("Shirt", 29.99));
            cart3.addProduct(Product("Jeans", 49.99));
            cart3.addProduct(Product("Shoes", 79.99));
            cart3.addProduct(Product("Watch", 99.99));
            cart3.addProduct(Product("Hat", 19.99));

            cart3.sortByName();
            cart3.displayProducts();
            std::cout << "Total price: $" << cart3.getTotalPrice() << "\n";

            cart3.removeProduct("Jeans");
            cart3.displayProducts();
            std::cout << "Total price: $" << cart3.getTotalPrice() << "\n";
        break;
        case 4:
            std::cout << "\n================================Case4================================\n";

            cart4.addProduct(Product("Shirt", 29.99));
            cart4.addProduct(Product("Jeans", 49.99));
            cart4.addProduct(Product("Shoes", 79.99));
            cart4.addProduct(Product("Watch", 99.99));
            cart4.addProduct(Product("Hat", 19.99));

            expensiveProducts4 = cart4.getExpensiveProducts(50);
            std::cout << "Expensive products in the shopping cart:\n";
            for (const Product& product : expensiveProducts4) {
                product.print();
                }
        break;
        case 5:
            std::cout << "\n================================Case5================================\n";

            cart5.addProduct(Product("Shirt", 29.99));
            cart5.addProduct(Product("Jeans", 49.99));
            cart5.addProduct(Product("Shoes", 79.99));
            cart5.addProduct(Product("Watch", 99.99));
            cart5.addProduct(Product("Hat", 19.99));
            cart5.displayProducts();
            std::cout << "Total price: $" << cart5.getTotalPrice() << "\n";

            cart5.applyDiscount(0.9);
            cart5.displayProducts();
            std::cout << "Total price: $" << cart5.getTotalPrice() << "\n";
            
            expensiveProducts5 = cart5.getExpensiveProducts(50);
            std::cout << "Expensive products in the shopping cart:\n";
            for (const Product& product : expensiveProducts5) {
                product.print();
                }
        break;
        case 6:
            std::cout << "\n================================Case6================================\n";

            cart6.addProduct(Product("Shirt", 29.99));
            cart6.addProduct(Product("Jeans", 49.99));
            cart6.addProduct(Product("Shoes", 79.99));
            cart6.addProduct(Product("Watch", 99.99));
            cart6.addProduct(Product("Hat", 19.99));
            cart6.displayProducts();
            std::cout << "Total price: $" << cart6.getTotalPrice() << "\n";
            Products6 = cart6.getProductsInPriceRange(50, 100);
            std::cout << "Products within a given price range in the shopping cart:\n";
            for (const Product& product : Products6) {
                product.print();
            }
        break;

        default:
            std::cout << "Unrecognized test case." << std::endl;
            break;
    }
    return 0;
}