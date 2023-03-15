#include <iostream>
#include <assert.h>
#include <bitset>
using std::bitset;

class Bits {
    using IType = unsigned long long; // We only have to change the integer type here, if desired
    enum {NBITS = sizeof(IType)*8};
    IType bits = 0;
public:
    Bits() = default;
    Bits(IType n) {
        bits = n;
    }
    static int size() {
        return NBITS;
    }
    bool at(int pos) const {  // Returns (tests) the bit at bit-position pos
        assert(0 <= pos && pos < NBITS);
        return bits & (IType(1) << pos);
    }
    void display() const{
        std::cout << "DECIMAL: " << bits << std::endl;
        std::cout << "BINARY: " << bitset<NBITS>(bits) << std::endl;
    }

    void set(int pos){ // Sets the bit at position pos
        assert(0 <= pos && pos < NBITS);
        bits |= (IType(1) << pos);
    }        
        
    void set(){ // Sets all bits 
        bits |= ~IType(0);
    }      

    void reset(int pos){ // Resets (makes zero) the bit at position pos
        assert(0 <= pos && pos < NBITS);
        bits &= ~(IType(1) << pos);
    }

    void reset(){ // Resets all bits
        bits &= IType(0);
    }

    void assign(int pos, bool val){ // Sets or resets the bit at position pos depending on val
        assert(0 <= pos && pos < NBITS);
        if (val == true){
            set(pos);
        }
        else{
            reset(pos);
        }


    }

    void assign(IType n){ // Replaces the underlying integer with n
        bits = n;
    }

    void toggle(int pos){ // Flips the bit at position pos
        assert(0 <= pos && pos < NBITS);
        bool val = at(pos);
        assign(pos, !val);
    }

    void toggle(){  // Flips all bits
        for (int pos = 0; pos < NBITS; pos++) {
            toggle(pos);
        }
    }

    void shift(int n){ // If n > 0, shifts bits right n places; if n < 0, shifts left
        if (n == 0){
            return;
        }
        else if (n > 0){
            bits >>= n;
        }
        else {
            bits <<= -n; //abs of n
        }
    }

    void rotate(int n){ // If n > 0, rotates right n places; if n < 0, rotates left
        if (n == 0){
            return;
        }
        else if (n > 0){
            bits = (bits >> n) | (bits << (NBITS - n));
        }
        else {
            bits = (bits << -n) | (bits >> (NBITS + n));
        }
    }

    int ones() const { // Returns how many bits are set in the underlying integer
        int i = 0;
        for (int pos = 0; pos < NBITS; pos++) {
            if (at(pos) == true){
                i++;
            }
        }
        return i;
    }

    int zeroes() const {      // Returns how many bits are reset in the underlying integer
        return NBITS - ones();
    }
    IType to_int() const {
        return bits;
    }
    friend bool operator==(const Bits& b1, const Bits& b2) {
        return b1.bits == b2.bits;
    }
    friend bool operator!=(const Bits& b1, const Bits& b2) {
        return b1.bits != b2.bits;
    }
    friend std::ostream& operator<<(std::ostream& os, const Bits& b) {
        return os << bitset<NBITS>(b.bits);    // Be sure to #include <bitset>
    }
};