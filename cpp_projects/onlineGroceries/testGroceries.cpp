
bool testCustomers(){
    string cust1 = "810003,Kai Antonikov,31 Prairie Rose Street,Philadelphia,PA,19196,215-975-7421,kantonikov0@4shared.com";
    assert (customers[0].customer_ID == "810003");
    assert (customers[0].name == "Kai Antonikov");
    assert (customers[0].street == "31 Prairie Rose Street");
    assert (customers[0].city == "Philadelphia");
    assert (customers[0].state == "PA");
    assert (customers[0].zipcode == "19196");
    assert (customers[0].phone == "215-975-7421");
    assert (customers[0].email == "kantonikov0@4shared.com");

    string cust2 = "731318,Chic Thunnerclef,2 School Circle,Lexington,KY,40596,859-105-6560,cthunnerclef1@youtube.com";
    assert (customers[1].customer_ID == "731318");
    assert (customers[1].name == "Chic Thunnerclef");
    assert (customers[1].street == "2 School Circle");
    assert (customers[1].city == "Lexington");
    assert (customers[1].state == "KY");
    assert (customers[1].zipcode == "40596");
    assert (customers[1].phone == "859-105-6560");
    assert (customers[1].email == "cthunnerclef1@youtube.com");

    string cust3 = "738434,Danna Kingdom,0 Gale Circle,Columbia,SC,29240,803-858-2969,dkingdom2@unicef.org";
    assert (customers[2].customer_ID == "738434");
    assert (customers[2].name == "Danna Kingdom");
    assert (customers[2].street == "0 Gale Circle");
    assert (customers[2].city == "Columbia");
    assert (customers[2].state == "SC");
    assert (customers[2].zipcode == "29240");
    assert (customers[2].phone == "803-858-2969");
    assert (customers[2].email == "dkingdom2@unicef.org");
    return true;
}

bool testItems(){
    string item1 = "57464,Almonds Ground Blanched,2.99";
    assert (items[0].item_id == 57464);
    assert (items[0].description == "Almonds Ground Blanched");
    assert (items[0].price == 2.99);

    string item2 = "23242,Apricots - Halves,0.89";
    assert (items[1].item_id == 23242);
    assert (items[1].description == "Apricots - Halves");
    assert (items[1].price == 0.89);


    string item3 = "55222,Artichoke - Fresh,2.39";
    assert (items[2].item_id == 55222);
    assert (items[2].description == "Artichoke - Fresh");
    assert (items[2].price == 2.39);
    return true;
}