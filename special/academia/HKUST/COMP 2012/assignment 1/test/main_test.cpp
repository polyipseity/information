#include <iostream>
#include <string>

#include "Buyer.h"
#include "Food.h"
#include "Menu.h"
#include "Order.h"
#include "OrderList.h"

using namespace std;

void placeOrder(Order& order, Menu& menu);
static int orderIdCounter = 1;
static int buyerIDCounter = 1;

bool SELECT_PROMPT = false;

int main() {
    if (SELECT_PROMPT) std::cout << "Select testing module: ";
    int mode;
    std::cin >> mode;
    if (SELECT_PROMPT) std::cout << std::endl;
    std::cin.get();

    if (mode == 1) {
        std::cout << "Testing TODO 1: Buyer constructor/setters/getters" << std::endl;

        if (SELECT_PROMPT) std::cout << "Select test case: ";
        int caseNum;
        std::cin >> caseNum;
        if (SELECT_PROMPT) std::cout << std::endl;
        std::cin.get();

        switch (caseNum) {
            case 1:
                {
                    std::cout << "Test case 1 selected." << std::endl;
                    Buyer buyer;
                    std::cout<< buyer.getBuyerId()<<std::endl;
                    std::cout<<buyer.getBuyerName()<<std::endl;
                }
                break;
            case 2:
                {
                    std::cout << "Test case 2 selected." << std::endl;
					Buyer buyer(1, "John");
                    std::cout<<buyer.getBuyerId()<<std::endl;
                    std::cout<<buyer.getBuyerName()<<std::endl;
                }
                break;
            case 3:
                {
                    std::cout << "Test case 3 selected." << std::endl;
                    Buyer buyer;
                    buyer.setBuyerId(2);
                    buyer.setBuyerName("Usman");
                    std::cout<<buyer.getBuyerId()<<std::endl;
                    std::cout<<buyer.getBuyerName()<<std::endl;
                }
                break;
            default:
                std::cout << "Unrecognized test case." << std::endl;
                break;
        }
    }
    else if (mode == 2) {
    	std::cout << "Testing TODO 2: Food constructor/setters/getters" << std::endl;

        if (SELECT_PROMPT) std::cout << "Select test case: ";
        int caseNum;
        std::cin >> caseNum;
        if (SELECT_PROMPT) std::cout << std::endl;
        std::cin.get();

        switch (caseNum) {
            case 1:
                {
                    std::cout << "Test case 1 selected." << std::endl;
                    Food food;
                    std::cout<<food.getFoodId()<<std::endl;
                    std::cout<<food.getFoodName()<<std::endl;
                    std::cout<<food.getPrice()<<std::endl;
                }
                break;
            case 2:
                {
                    std::cout << "Test case 2 selected." << std::endl;
					Food food(1, "Burger", 50.0);
                    std::cout<<food.getFoodId()<<std::endl;
                    std::cout<<food.getFoodName()<<std::endl;
                    std::cout<<food.getPrice()<<std::endl;
                }
                break;
            case 3:
                {
                    std::cout << "Test case 3 selected." << std::endl;
                    Food food;
                    food.setFoodId(1);
                    food.setFoodName("Fries");
                    food.setPrice(20.0);
                    std::cout<<food.getFoodId()<<std::endl;
                    std::cout<<food.getFoodName()<<std::endl;
                    std::cout<<food.getPrice()<<std::endl;
                }
                break;
            default:
                std::cout << "Unrecognized test case." << std::endl;
                break;
        }
    }
    else if (mode == 3) {
    	std::cout << "Testing TODO 3: Menu class functions" << std::endl;
        Food a{1, "Cake", 50.0};
        Food b{2, "Chocolate", 10.0};
        if (SELECT_PROMPT) std::cout << "Select test case: ";
        int caseNum;
        std::cin >> caseNum;
        if (SELECT_PROMPT) std::cout << std::endl;
        std::cin.get();

        switch (caseNum) {
            case 1:
                {
                    std::cout << "Test case 1 selected." << std::endl;
                    Menu empty;
                    empty.displayMenu();
                }
                break;
            case 2:
                {
                    std::cout << "Test case 2 selected." << std::endl;
                    Menu m1;
                    m1.addFood(a);
                    m1.addFood(b);
                    m1.displayMenu();
                }
                break;
            case 3:
                {
                std::cout << "Test case 3 selected." << std::endl;
                int id = 1;
                Menu m1;
                m1.addFood(a);
                m1.addFood(b);
                std::cout << "Enter the ID of the food item to remove: ";
                // std::cin >> id;
                if (m1.removeFood(id)) {
                    std::cout << "Food item removed successfully." << std::endl;
                    }
                m1.displayMenu();
                }
                break;

                case 4:
                {
                std::cout << "Test case 4 selected." << std::endl;
                int id = 1;
                int nextFoodId = 1; // Track the next available food item ID
                Menu m1;
                m1.addFood(a);
                nextFoodId++;
                m1.addFood(b);
                nextFoodId++;
                std::cout << "Enter the ID of the food item to remove: ";
                // std::cin >> id;
                if (m1.removeFood(id)) {
                    std::cout << "Food item removed successfully." << std::endl;
                    }
                Food newFood(nextFoodId, "Pasta", 30.0);
                m1.addFood(newFood);
                m1.displayMenu();
                }
                break;
            default:
                std::cout << "Unrecognized test case." << std::endl;
                break;
        }
    }
    else if (mode == 4) {
    	std::cout << "Testing TODO 4: Order class functions" << std::endl;
        Food a{1, "Chicken", 50.0};
        Food b{2, "Cake", 100.0};
        Menu menu; // Assume initialized properly
        menu.addFood(a);
        menu.addFood(b);

        if (SELECT_PROMPT) std::cout << "Select test case: ";
        int caseNum;
        std::cin >> caseNum;
        if (SELECT_PROMPT) std::cout << std::endl;
        std::cin.get();
 
        switch (caseNum) {
            case 1:
                {
                    std::cout << "Test case 1 selected." << std::endl;
                    Order newOrder;
                    std::cout<< newOrder.getOrderId() <<std::endl;
                    std::cout<<newOrder.getcurrentNum() <<std::endl;
                }
                break;
            case 2:
                {
                    std::cout << "Test case 2 selected." << std::endl;
                    Order newOrder;
                    string buyerName = "Alex";
                    int buyerId = buyerIDCounter++;
                    newOrder.setBuyer(buyerId, buyerName);
                    std::cout << newOrder.getBuyer().getBuyerId()<<std::endl;
                    std::cout << newOrder.getBuyer().getBuyerName()<<std::endl;
                }
                break;
            case 3:
                {
                    std::cout << "Test case 3 selected." << std::endl;
                    Order newOrder;
                    newOrder.setOrderId(orderIdCounter++);
                    std::cout<< newOrder.getOrderId()<<std::endl;
                }
                break;
            case 4:
                {
                    std::cout << "Test case 4 selected." << std::endl;
                    Order newOrder;
                    placeOrder(newOrder, menu);
                }
                break;
            case 5:
                {
                    std::cout << "Test case 5 selected." << std::endl;
                    Order newOrder;
                    placeOrder(newOrder, menu);
                    newOrder.displayOrder();
                }
                break;
            default:
                std::cout << "Unrecognized test case." << std::endl;
                break;
        }
    }

    else if (mode == 5) {
    	std::cout << "Testing TODO 5: OrderList class functions" << std::endl;
        Food a{1, "Chicken", 50.0};
        Food b{2, "Cake", 100.0};
        Menu menu; // Assume initialized properly
        menu.addFood(a);
        menu.addFood(b);

        if (SELECT_PROMPT) std::cout << "Select test case: ";
        int caseNum;
        std::cin >> caseNum;
        if (SELECT_PROMPT) std::cout << std::endl;
        std::cin.get();

        switch (caseNum) {
            case 1:
            {
                std::cout << "Test case 1 selected." << std::endl;
                Order newOrder;
                OrderList orderList;
                placeOrder(newOrder, menu);
                orderList.addOrder(newOrder);
            }
            break;

            case 2:
            {
                std::cout << "Test case 2 selected." << std::endl;
                Order newOrder;
                OrderList orderList;
                placeOrder(newOrder, menu);
                orderList.addOrder(newOrder);
                orderList.displayOrderList();
            }
            break;

            case 3:
            {
                std::cout << "Test case 3 selected." << std::endl;
                int buyerId = 1;
                Order newOrder;
                OrderList orderList;
                placeOrder(newOrder, menu);
                orderList.addOrder(newOrder);
                orderList.displayOrdersForBuyer(buyerId);
            }
            break;

            case 4:
            {
                std::cout << "Test case 4 selected." << std::endl;
                Order newOrder;
                OrderList orderList;
                if (orderList.isEmpty()) 
                {
                    std::cout << "Order list is empty. No order to process." << std::endl;
                }
            }
            break;

            case 5:
            {
                std::cout << "Test case 5 selected." << std::endl;
                int orderId = 1;
                Order newOrder;
                OrderList orderList;
                placeOrder(newOrder, menu);
                orderList.addOrder(newOrder);
                if (orderList.isEmpty()) {
                    std::cout << "Order list is empty. No order to process." << std::endl;
                } 
            else {
                std::cout << "Enter OrderID to process it: ";
                if (orderList.removeOrder(orderId)) {
                std::cout << "Order ID " << orderId << " processed and removed from the list.\n";
                    } 
                    else{
                        std::cout << "Order ID " << orderId << " not found.\n";
                        }
                }
            }
            break;

            case 6:
            {
                std::cout << "Test case 6 selected." << std::endl;
                int buyerId; // Use this to store and use the correct buyer ID for actions
                int cOrderId; //Temp orderID to store and use it when copying order
                string buyerName;
                Order firstOrder;
                Order secondOrder;
                OrderList orderList;
                placeOrder(firstOrder, menu);
                orderList.addOrder(firstOrder);
                orderList.displayOrderList();

                std::cout << "Enter your name: ";
                std::cin >> buyerName;
                buyerId = buyerIDCounter++; 
                secondOrder.setBuyer(buyerId, buyerName);
                secondOrder.setOrderId(orderIdCounter++);
                std::cout << "Please enter the Order Id you want to copy: ";
                std::cin >> cOrderId;

                // Find the order to copy
                const Order* orderToCopy = orderList.findOrder(cOrderId);
                if (orderToCopy) {
                //call cloneOrder
                secondOrder.cloneOrder(*orderToCopy);

                // Add the copied order to the order list
                orderList.addOrder(secondOrder);

                std::cout << "Order with ID " << cOrderId << " copied successfully.\n";
                orderList.displayOrderList();
                } else {
                std::cout << "Order with ID " << cOrderId << " not found.\n";
                    }
                }
            break;
            
            default:
                std::cout << "Unrecognized test case." << std::endl;
                break;
    
        }
    }
    else {
        std::cout << "Unrecognized test case." << std::endl;
    }
    
return 0;
}

void placeOrder(Order& newOrder, Menu& menu) {
    string buyerName = "Alex";
    int buyerId = buyerIDCounter++; 
    
    newOrder.setBuyer(buyerId, buyerName);
    newOrder.setOrderId(orderIdCounter++);
    
    menu.displayMenu();
    bool addingItems = true;
    while (addingItems) {
        int foodId;
        std::cout << "Enter Food ID to add to your order (Enter 0 to stop): ";
        cin >> foodId;
        if (foodId == 0) {
            addingItems = false;
        } else {
            const Food* foodItem = menu.getFoodById(foodId);
            if (foodItem != nullptr) {
                newOrder.addItem(*foodItem);
                //foodId=0;
            } else {
                std::cout << "Invalid Food ID. Please try again." << std::endl;
            }
        }
    }
    std::cout << "Thank you for placing your order: "<<buyerName<<std::endl;
    std::cout << "Your Buyer ID is " << buyerId << ". Please note this down for viewing your orders in the future.\n";
}
