#include <iostream>
#include <fstream>
#include <vector>
#include<string>
#include "split.h"
#include <list>
#include <iomanip>
#include <sstream>
#include <algorithm>
using std::cout;
using std::cin;
using std::ofstream;
using std::ifstream;
using std::ios;
using std::endl;
using std::string;
using std::vector;
using std::list;

struct Customer{
    string customer_ID;
    string name;
    string street;
    string city;
    string state;
    string zipcode;
    string phone;
    string email;
};

struct Item{
    int item_id;
    string description;
    double price;
};

vector <Customer> customers;
vector <Item> items;

struct LineItem{
    int item_id;
    int qty;
    double subtotal(){
        //Calls Find price using and passes self.item_id as a parameter, multiplies self.qty by the returned price and returns subtot
        double subtot;
        double price = findPrice(item_id);
        subtot = price * qty;
        return subtot;
    }
    double findPrice(int itemID){
        //Loops through global items list and extracts/returns the matching price
        for (int i = 0; i < items.size(); i++){
            if (items[i].item_id == itemID){
                return items[i].price;
            }
        }
        return 0;
    }
    string getDesc(int itemID){
        //loops through global items list and extracts/returns the matching description
        for (int i = 0; i < items.size(); i++){
            if (items[i].item_id == itemID){
                return items[i].description;
            }
        }
        return 0;
    }
    friend bool operator<(const LineItem& a, const LineItem& b){
        //operator overloader to sort LineItems list by item id
        return a.item_id < b.item_id;
    }
};

class Payment{
    //abstract payment class
public:
    double amount = 0;
    virtual string printDetail(){
        //virtual method
        return "Payment Detals:";
    }
};

class Credit: public Payment{
public:
    string card_Num;
    string expiration;
    string printDetail() override{
        return "Paid by Credit card " + card_Num + ", Exp: " + expiration; 
    }
};

class PayPal: public Payment{
public:
    string paypalID;
    string printDetail() override{
        return "Paid by Paypal ID: " + paypalID;
    }
};

class WireTransfer: public Payment{
public:
    string bankID;
    string accountID;
    string printDetail() override{
        return "Paid by Wire Transfer from Bank ID " + bankID + ", Account ID: " + accountID;
    }
};

class Order{
public:
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;
    Order(int orderID, string orderDate, int custID, vector<LineItem> lineItems, Payment* payMeth){
        //constructor:Payment is a pointer to allow for printdetail() override
        order_id = orderID;
        order_date = orderDate;
        cust_id = custID;
        sort(lineItems.begin(), lineItems.end());
        line_items = lineItems;
        payment = payMeth;
        total();
    }
    ~Order(){
        //deconstructor for payment pointer
        payment = nullptr;
    }
    string printOrder(){
        //uses stream to coordinate output of each order and returns a string
        std::stringstream stream;
        stream << "===========================" << endl;
        stream << "Order #" << order_id << ", Date: " << order_date << endl;
        stream << "Amount: $" << std::fixed << std::setprecision(2) << "Total: $" << payment->amount << ", ";
        stream << payment->printDetail() << endl << endl;
        stream << "Customer ID: " << cust_id << ':' << endl;
        stream << findCust(cust_id) << endl;
        stream << "Order Detals: " << endl;
        for (int i = 0; i < line_items.size(); i++){
            stream << "Item " << line_items[i].item_id << ": '" << line_items[i].getDesc(line_items[i].item_id)<< "', ";
            stream << line_items[i].qty << " @ " << line_items[i].findPrice(line_items[i].item_id) << endl;
        }
        return stream.str();
    }
    string findCust(int custID){
        for (int i = 0; i < customers.size(); i++){
            if (stoi(customers[i].customer_ID) == custID){
                std::stringstream stream;
                stream << customers[i].name << ", ph. " << customers[i].phone << ", email: "<< customers[i].email << endl;
                stream << customers[i].street << endl;
                stream << customers[i].city << ", " << customers[i].state << ' ' <<customers[i].zipcode << endl;
                return stream.str();
            } 
        }
        return 0;
    }

    void total(){
        //called during construction, calculates the total for the entire order and stores it in payment->amount;
        double runningTot = 0;
        for (int i = 0; i < line_items.size(); i++){
            runningTot += line_items[i].subtotal();
        }
        payment->amount = runningTot;
    }
};

list <Order> orders;

void readCustomers(string fileName){
    vector <string> lines;
    ifstream myFile(fileName);
    if (myFile.is_open()){
        string line;    
        while(getline(myFile, line)){
            lines.push_back(line);
        }
        myFile.close();
        for (int i =0; i < lines.size(); i++){
            Customer currCustomer;
            vector <string> custData;
            custData = (split(lines[i], ','));
            currCustomer.customer_ID = custData[0];
            currCustomer.name = custData[1];
            currCustomer.street = custData[2];
            currCustomer.city = custData[3];
            currCustomer.state = custData[4];
            currCustomer.zipcode = custData[5];
            currCustomer.phone = custData[6];
            currCustomer.email = custData[7];
            customers.push_back(currCustomer);
        }
    }
    else{
        cout << "Error opening file: " << fileName << endl;
    }
    cout << "There are " << customers.size() << " customers" << endl;
}

void readItems(string fileName){
    ifstream myFile(fileName);
    vector <string> lines;
    if (myFile.is_open()){
        string line;
        while(getline(myFile, line)){
            lines.push_back(line);
        }
        myFile.close();
        for (int i = 0; i < lines.size(); i++){
            vector <string> itemData;
            Item currItem;
            itemData = (split(lines[i], ','));
            currItem.item_id = stoi(itemData[0]);
            currItem.description = itemData[1];
            currItem.price = stod(itemData[2]);
            items.push_back(currItem);
        }
    }
    else{
        cout << "Error opening file: " << fileName << endl;
    }
    cout << "There are " << items.size() << " items" << endl;
}

void readOrders(string fileName){
    ifstream myFile(fileName);
    vector <string> lines;
    if (myFile.is_open()){
        string line;
        while(getline(myFile, line)){
            lines.push_back(line);
        }
        myFile.close();
    }
    else{
        cout << "Unable to open file " << fileName << endl;
    }
    for (int i = 0; i < lines.size(); i++){
        //main extracting algorithm
        vector <string> currOrder;
        vector <LineItem> lineItems;
        vector <string> paymentMeth;

        currOrder = split(lines[i], ',');

        int custID = stoi(currOrder[0]);
        int orderNum = stoi(currOrder[1]);
        string date = currOrder[2];

        for (int j = 3; j < currOrder.size(); j++){
            vector <string> currItem;
            currItem = split(currOrder[j], '-');
            LineItem newItem;
            newItem.item_id = stoi(currItem[0]);
            newItem.qty = stoi(currItem[1]);
            lineItems.push_back(newItem);
        }
        paymentMeth = split(lines[i+1], ',');
        for (int k = 0; k < paymentMeth.size(); k++){
            if (paymentMeth[k] == "1"){ //CC
                Credit *creditCard = new Credit(); // new creates the Credit object on the heap, *creditCard keeps track of the address.
                creditCard->card_Num = paymentMeth[k + 1];
                creditCard->expiration = paymentMeth[k + 2];
                Order newOrder(orderNum, date, custID, lineItems, creditCard);
                orders.push_back(newOrder);
                //Note that there is no "Delete creditCard" needed as we have a deconstructor in our order class that will prevent memory leaks
            }
            else if (paymentMeth[k] == "2"){ //PP
                PayPal *payPal = new PayPal();
                payPal->paypalID = paymentMeth[k + 1];
                Order newOrder(orderNum, date, custID, lineItems, payPal);
                orders.push_back(newOrder);
            }
            else if (paymentMeth[k] == "3"){ //WT
                WireTransfer *wire = new WireTransfer();
                wire->bankID = paymentMeth[k + 1];
                wire->accountID = paymentMeth[k + 2];
                Order newOrder(orderNum, date, custID, lineItems, wire);
                orders.push_back(newOrder);
            }
        }
        i++;
    }
}

int main(){
    readCustomers("customers.txt");
    readItems("items.txt");
    readOrders("orders.txt");
    ofstream ofs("order_report.txt");
    for (auto& order: orders){ofs << order.printOrder() << endl;}
    return 0;
}
