#include <iostream>
#include "bits.h"
using std::cout;
using std::endl;

void test_set(Bits& obj, int pos){
    cout << "Position to set: " << pos << endl;
    cout << "Bit before set: " << obj.at(pos) << endl;
    cout << "Testing Set Bit" << endl;
    obj.set(pos);
    cout << "Bit after set: " << obj.at(pos) << endl;
    cout << "Current binary representation: " << endl;
    obj.display();
    cout << endl;
    cout << "Setting all bits . . . " << endl;
    obj.set();
    cout << "New binary representation: " << endl;
    obj.display();
    cout << endl;
    cout << endl;

}

void test_reset(Bits& obj, int pos){
    cout << "Position to reset: " << pos << endl;
    cout << "Bit before reset: " << obj.at(pos) << endl;
    cout << "Testing Reset Bit" << endl;
    obj.reset(pos);
    cout << "Bit after Reset: " << obj.at(pos) << endl;
    cout << endl;
    cout << "Current binary representation: " << endl;
    obj.display();
    cout << "Resetting all bits . . . " << endl;
    obj.reset();
    cout << "New binary representation: " << endl;
    obj.display();
    cout << endl;
    cout << endl;
}

void tSetandReset(){
    Bits bits1(1);
    Bits bits2(2);
    Bits bits3(4);
    Bits bits4(8);
    Bits bits5(16);
    Bits bits6(32);
    test_set(bits1, 1);
    test_set(bits2, 2);
    test_set(bits3, 3);
    test_set(bits4, 4);
    test_set(bits5, 5);
    test_set(bits6, 6);
    test_reset(bits1, 15);
    test_reset(bits2, 20);
    test_reset(bits3, 30);
    test_reset(bits4, 40);
    test_reset(bits5, 50);
    test_reset(bits6, 60);
}

void tAssign(){

    Bits bits1(1);
    Bits bits2(2);
    Bits bits3(4);
    Bits bits4(8);
    Bits bits5(16);
    Bits bits6(32);
    bits1.reset();
    bits2.set();
    bits3.reset();
    bits4.set();
    bits5.reset();
    bits6.set();

    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();
    cout << "Starting true test: " << endl;

    bits1.assign(10, true);
    bits2.assign(10, true);
    bits3.assign(10, true);
    bits4.assign(10, true);
    bits5.assign(10, true);
    bits6.assign(10, true);

    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();
    cout << "RESETTING" << endl;
    bits1.reset();
    bits2.set();
    bits3.reset();
    bits4.set();
    bits5.reset();
    bits6.set();
    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();
    cout << "Starting false test:" << endl;
    bits1.assign(10, false);
    bits2.assign(10, false);
    bits3.assign(10, false);
    bits4.assign(10, false);
    bits5.assign(10, false);
    bits6.assign(10, false);

    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();

}

void tAssign2(int n){
    Bits bits1(1);
    Bits bits2(2);
    Bits bits3(4);
    Bits bits4(8);
    Bits bits5(16);
    Bits bits6(32);

    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();
    cout << endl;
    cout << "Starting test: " << endl;
    cout << endl;
    bits1.assign(45);
    bits2.assign(45);
    bits3.assign(45);
    bits4.assign(45);
    bits5.assign(45);
    bits6.assign(45);

    bits1.display();
    bits2.display();
    bits3.display();
    bits4.display();
    bits5.display();
    bits6.display();
}

void testToggle(int pos){
    Bits myBit(0);
    Bits ourBit(18446744073709551615);
    cout << "First Bit: " << endl;
    myBit.display();
    cout << endl;
    cout << "Second Bit: " << endl;
    ourBit.display();

    myBit.toggle(pos);
    ourBit.toggle(pos);

    cout << "First Bit: " << endl;
    myBit.display();
    cout << endl;
    cout << "Second Bit: " << endl;
    ourBit.display();

    cout << endl;
    cout << "Toggling all bits: " << endl;
    myBit.toggle();
    ourBit.toggle();

    cout << "First Bit: " << endl;
    myBit.display();
    cout << endl;
    cout << "Second Bit: " << endl;
    ourBit.display();
}

void testShift(int n){
    Bits bits1(5674909000001);
    Bits bits2(10000000);

    cout << "Initial values: " << endl;
    bits1.display();
    bits2.display();
    cout << endl;

    bits1.shift(-9);
    bits2.shift(9);

    cout << endl;
    cout << "Returned values: " << endl;
    bits1.display();
    bits2.display();
    cout << endl;
}

void testRotate(int n){
    Bits bits1(5674909000001);
    Bits bits2(10000000);

    cout << "Initial values: " << endl;
    bits1.display();
    bits2.display();
    cout << endl;

    bits1.rotate(9);
    bits2.rotate(9);

    cout << endl;
    cout << "Returned values: " << endl;
    bits1.display();
    bits2.display();
    cout << endl;
}

void testOnesAndZeroes(){
    Bits myBits(69420);
    myBits.display();
    cout << endl;
    cout << "Number of 1's: " << myBits.ones() << endl;
    cout << endl;
    cout << "Number of 0's: " << myBits.zeroes() << endl;
}

int main(){
    tSetandReset();
    tAssign();
    tAssign2(45);
    testToggle(32);
    testShift(1);
    testRotate(1);
    testOnesAndZeroes();
    return 0;
}