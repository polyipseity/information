#include <iostream>
#include <string>

#include "Food.h"
#include "Menu.h"
#include "Order.h"
#include "OrderList.h"
#include "Buyer.h"
using namespace std;


// Static variables for counter
static int orderIdCounter = 1;
static int buyerIDCounter = 1;
// Function prototypes for user interaction functions
void displayMainMenu();
void handleSellerActions(Menu& menu, OrderList& orderList);
void handleBuyerActions(Menu& menu, OrderList& orderList);
void placeOrder(Menu& menu, OrderList& orderList);

int main() {
    Menu menu; // Assume initialized properly
    OrderList orderList; // Assume initialized properly
    Buyer buyer; // Assume exists and is initialized properly
    //Adding food items to menu
    Food pizza(1, "Pizza", 70.0);
    Food burger(2, "Burger", 50.0);
    Food fries(3, "Fries", 7.5);
    Food drink(4, "Pepsi", 4.5);
    menu.addFood(pizza);
    menu.addFood(burger);
    menu.addFood(fries);
    menu.addFood(drink);

    bool running = true;
    while (running) {
        displayMainMenu();
        int choice;
        cin >> choice;

        switch (choice) {
            case 1:
                handleSellerActions(menu, orderList);
                break;
            case 2:
                handleBuyerActions(menu, orderList);
                break;
            case 3:
                running = false;
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
                break;
        }
    }
    return 0;
}

void displayMainMenu() {
    cout << "\n** Main Menu **\n";
    cout << "1. Seller Actions\n";
    cout << "2. Buyer Actions\n";
    cout << "3. Exit\n";
    cout << "Enter your choice: ";
}

void handleSellerActions(Menu& menu, OrderList& orderList) {
    int choice;
    int pOrderID;
    do {
        cout << "\n** Seller Menu **\n"
                  << "1. View Menu\n"
                  << "2. Update Menu\n"
                  << "3. View Orders\n"
                  << "4. Process Orders\n"
                  << "5. Exit\n"
                  << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                menu.displayMenu();;
                break;
            case 2:
                menu.manageFoodItems();
                break;
            case 3:
                orderList.displayOrderList();
                break;
            case 4:
            if (orderList.isEmpty()) {
                    cout << "Order list is empty. No order to process." << endl;
                } 
            else {
                    orderList.displayOrderList();
                    cout << "Enter OrderID to process it: ";
                    cin >> pOrderID;
                    if (orderList.removeOrder(pOrderID)) {
                cout << "Order ID " << pOrderID << " processed and removed from the list.\n";
                    } 
                    else {
                        cout << "Order ID " << pOrderID << " not found.\n";
                        }
                    }
                break;    
            case 5:
                cout << "Exiting seller actions.\n \n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
        }
    } while (choice != 5);
}


void handleBuyerActions(Menu& menu, OrderList& orderList) {
    int choice;
    int buyerId; // Use this to store and use the correct buyer ID for actions
    int cOrderId; //Temp orderID to store and use it when copying order
    string buyerName;
    do {
        cout << "\n** Buyer Menu **\n"
             << "1. View Menu\n"
             << "2. Place Order\n"
             << "3. View My Orders\n"
             << "4. Copy an Order\n"
             << "5. Exit\n"
             << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                menu.displayMenu();
                break;
            case 2:
                cout << "Placing an order\n";
                placeOrder(menu, orderList); // This function now should ask for buyer name or ID and set it correctly in the Order object
                break;
            case 3:
                cout << "Enter your Buyer ID: "; // Ask for buyer ID each time
                cin >> buyerId;
                cout << "Viewing buyer's orders\n";
                orderList.displayOrdersForBuyer(buyerId);
                break;
            case 4:
            if (orderList.isEmpty()) {
                    cout << "Order list is empty. No order to copy." << endl;
                } 
            else {
                Order newOrder; // Create a new order
                orderList.displayOrderList();
                
                cout << "Enter your name: ";
                cin >> buyerName;
                buyerId = buyerIDCounter++; 
                newOrder.setBuyer(buyerId, buyerName);
                newOrder.setOrderId(orderIdCounter++);
                cout << "Please enter the Order Id you want to copy: ";
                cin >> cOrderId;

                // Find the order to copy
                const Order* orderToCopy = orderList.findOrder(cOrderId);
                if (orderToCopy) {
                //call cloneOrder (assuming functions exist)
                newOrder.cloneOrder(*orderToCopy);

                // Add the copied order to the order list
                orderList.addOrder(newOrder);

                cout << "Order with ID " << cOrderId << " copied successfully.\n";
                } else {
                cout << "Order with ID " << cOrderId << " not found.\n";
                    }
                }   
                break;
            case 5:
                cout << "Exiting buyer actions.\n";
                break;
            default:
                cout << "Invalid choice. Please try again.\n";
    }
  } while (choice != 5);
}

void placeOrder(Menu& menu, OrderList& orderList) {
    Order newOrder;
    string buyerName;
    cout << "Enter your name: ";
    cin >> buyerName;
    int buyerId = buyerIDCounter++; 
    
    newOrder.setBuyer(buyerId, buyerName);
    newOrder.setOrderId(orderIdCounter++);
    
    menu.displayMenu();
    bool addingItems = true;
    while (addingItems) {
        int foodId;
        cout << "Enter Food ID to add to your order (Enter 0 to stop): ";
        cin >> foodId;
        if (foodId == 0) {
            addingItems = false;
        } else {
            const Food* foodItem = menu.getFoodById(foodId);
            if (foodItem != nullptr) {
                newOrder.addItem(*foodItem);
            } else {
                cout << "Invalid Food ID. Please try again." << endl;
            }
        }
    }
    cout << "Thank you for placing your order: "<<buyerName<<endl;
    cout << "Your Buyer ID is " << buyerId << ". Please note this down for viewing your orders in the future.\n";

    orderList.addOrder(newOrder);
}