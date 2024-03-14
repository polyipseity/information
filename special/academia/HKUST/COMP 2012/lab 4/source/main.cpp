#include <iostream>
#include "MemberOrder.h"
using namespace std;

int main() {

    std::cout << "[Task_1] ProductCollection class" << std::endl;
    ProductCollection* productCollection = new ProductCollection("#_collection_01", 2);
    productCollection->insert(10);
    productCollection->insert(15);
    productCollection->insert(40);
    std::cout << productCollection->getCollectionID() << ": capacity is " << productCollection->getCapacity() << std::endl;
    productCollection->printProducts();
    productCollection->increaseCapacity(2);
    productCollection->insert(40);
    productCollection->insert(50);
    productCollection->insert(60);
    productCollection->increaseCapacity(2);
    productCollection->insert(70);
    std::cout << productCollection->getCollectionID() << ": capacity is " << productCollection->getCapacity() << std::endl;
    productCollection->printProducts();

    std::cout << "\n[Task_2] OrdinaryOrder class" << std::endl;
    OrdinaryOrder* ordinaryOrder1 = new OrdinaryOrder("#_order_01", "Alice", ON_SITE, 10);
    OrdinaryOrder* ordinaryOrder2 = new OrdinaryOrder("#_order_02", "Bob", COURIER, 4);
    ordinaryOrder1->insert(50);
    ordinaryOrder1->insert(60);
    ordinaryOrder2->insert(70);
    ordinaryOrder2->printProducts();
    ordinaryOrder2->addFromOrder(ordinaryOrder1);
    ordinaryOrder2->printProducts();
    ordinaryOrder2->addFromOrder(ordinaryOrder1);
    ordinaryOrder2->printProducts();

    std::cout << "\n[Task_3] MemberOrder class" << std::endl;
    MemberOrder* memberOrder = new MemberOrder("#_order_03", "Carol", PICK_UP, 10);
    memberOrder->insert(10);
    memberOrder->insert(10);
    memberOrder->insert(10);
    memberOrder->insert(40);
    memberOrder->insert(50);
    memberOrder->insert(60);
    memberOrder->insert(70);
    memberOrder->remove(15);
    memberOrder->remove(10);
    memberOrder->printProducts();
    std::cout << memberOrder->getCollectionID() << ": reward points is " << memberOrder->getPoints() << std::endl;
    memberOrder->addFromOrder(ordinaryOrder2);
    memberOrder->printProducts();
    std::cout << memberOrder->getCollectionID() << ": reward points is " << memberOrder->getPoints() << std::endl;
    memberOrder->addFromOrder(ordinaryOrder2);
    memberOrder->printProducts();
    std::cout << memberOrder->getCollectionID() << ": reward points is " << memberOrder->getPoints() << std::endl;
    
    delete productCollection;
    delete ordinaryOrder1;
    delete ordinaryOrder2;
    delete memberOrder;
    
    return 0;
}
