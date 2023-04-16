#ifndef VECTOR_H
#define VECTOR_H
#include <iostream>
#include <cstddef>
#include <stdexcept>  // for std::range_error

using std::endl;
using std::cout;
using std::size_t;
using std::range_error;


template <class T> class Vector {
    enum { CHUNK = 10 };
    size_t capacity;    // Size of the current array allocation (total number of Ts, in use or not)
    size_t n_elems;     // Number of T spaces currently in use, starting from position 0
    T* data_ptr;        // Pointer to the heap array
    void grow() {
        capacity += CHUNK;
        T* new_data_ptr = new T[capacity];
        std::copy(data_ptr, data_ptr + n_elems, new_data_ptr);
        delete[] data_ptr;
        data_ptr = new_data_ptr;
}
public:
    // Object Mgt.
    Vector() : capacity(CHUNK), n_elems(0), data_ptr(new T[capacity]) {} //Default constructor
    Vector(const Vector& v) : capacity(v.capacity), n_elems(v.n_elems), data_ptr(new T[capacity]){ // COPY Constructor
    for(size_t i = 0; i < n_elems; ++i){
        data_ptr[i] = v.data_ptr[i];
    }
}
 Vector<T>& operator=(const Vector& v){ //Copy Assignment Operator
    if (this != &v) {
        T* new_data_ptr = new T[v.capacity];
        for(size_t i = 0; i < v.n_elems; ++i){
            new_data_ptr[i] = v.data_ptr[i];
        }
        delete[] data_ptr;
        data_ptr = new_data_ptr;
        n_elems = v.n_elems;
        capacity = v.capacity;
    }
    return *this;
}

    ~Vector() { delete[] data_ptr; }

    // Accessors
    T& front() const{
        if (n_elems == 0) throw range_error("Empty Vector");
        return data_ptr[0];
}                  
    T& back() const{
        if (n_elems == 0) throw range_error("Empty Vector");
        return data_ptr[n_elems-1];
}                
    T& at(size_t pos) const{
        if (pos >= n_elems) throw range_error("Out of range");
        return data_ptr[pos];
}         
    size_t size() const{
        return n_elems;
}
    bool empty() const{
        return n_elems == 0;
}

    // Mutators
    T& operator[](size_t pos) {
        return data_ptr[pos];
}
    void push_back(T num) {
        if (n_elems == capacity) grow();
            data_ptr[n_elems++] = num;
}    
    void pop_back() {
    if (n_elems == 0) throw range_error("Empty Vector");
    --n_elems;
}
    void erase(size_t pos) {
        if (pos >= n_elems) throw range_error("Out of range");
            for (size_t i = pos + 1; i < n_elems; ++i){
                    data_ptr[i-1] = data_ptr[i];
            }
    --n_elems;
}   
    void insert(size_t pos, T item){
        if (pos > n_elems) throw range_error("Out of range");
        if (n_elems == capacity) grow();
        for (size_t i = n_elems; i > pos; --i){
            data_ptr[i] = data_ptr[i-1];
        }
        data_ptr[pos] = item;
        ++n_elems;
}    
void clear() { n_elems = 0; }        // n_elems = 0 (nothing else to do; keep the current capacity)

    // Iterators
    T* begin() {
        return n_elems == 0 ? nullptr : &data_ptr[0];
}                       
    T* end() {
        return n_elems == 0 ? nullptr : &data_ptr[n_elems];
}    

    // Comparators
    bool operator ==(const Vector& v) const {
    if (n_elems != v.n_elems) return false;
    for (size_t i; i < n_elems; ++i){
        if (data_ptr[i] != v.data_ptr[i]){
            return false;
        }
    }
    return true;
}
    bool operator !=(const Vector& v) const {
    return !(*this == v);
}
};

#endif