#include "Vector.h"
#include <stdexcept>
#include<iostream>

using std::cout;
using std::endl;
using std::range_error;

//Object management
Vector::Vector() : capacity(CHUNK), n_elems(0), data_ptr(new int[capacity]) {} //Default constructor

Vector::Vector(const Vector& v) : capacity(v.capacity), n_elems(v.n_elems), data_ptr(new int[capacity]){ // COPY Constructor
    for(size_t i = 0; i < n_elems; ++i){
        data_ptr[i] = v.data_ptr[i];
    }
}

Vector& Vector::operator=(const Vector& v){ //Copy Assignment Operator
    if (this != &v) {
        int* new_data_ptr = new int[v.capacity];
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

Vector::~Vector() { //Deconstructor
    delete[] data_ptr;
}

//Grow
void Vector::grow() {
    capacity += CHUNK;
    int* new_data_ptr = new int[capacity];
    std::copy(data_ptr, data_ptr + n_elems, new_data_ptr);
    delete[] data_ptr;
    data_ptr = new_data_ptr;
    cout << "Grow" << endl;
}

//Accessors
int Vector::front() const{
    if (n_elems == 0) throw range_error("Empty Vector");
    return data_ptr[0];
}

int Vector::back() const{
    if (n_elems == 0) throw range_error("Empty Vector");
    return data_ptr[n_elems-1];
}

int Vector::at(size_t pos) const{
    if (pos >= n_elems) throw range_error("Out of range");
    return data_ptr[pos];
}

size_t Vector::size() const{
    return n_elems;
}

bool Vector::empty() const{
    return n_elems == 0;
}

// Mutators
int& Vector::operator[](size_t pos) {
    return data_ptr[pos];
}

void Vector::push_back(int num) {
    if (n_elems == capacity) grow();
    data_ptr[n_elems++] = num;
}

void Vector::pop_back() {
    if (n_elems == 0) throw range_error("Empty Vector");
    --n_elems;
}

void Vector::erase(size_t pos) {
    if (pos >= n_elems) throw range_error("Out of range");
    for (size_t i = pos + 1; i < n_elems; ++i){
        data_ptr[i-1] = data_ptr[i];
    }
    --n_elems;
}

void Vector::insert(size_t pos, int item){
    if (pos > n_elems) throw range_error("Out of range");
    if (n_elems == capacity) grow();
    for (size_t i = n_elems; i > pos; --i){
        data_ptr[i] = data_ptr[i-1];
    }
    data_ptr[pos] = item;
    ++n_elems;
}

void Vector::clear() {
    n_elems = 0;
}

// Iterators
int* Vector::begin() {
    return n_elems == 0 ? nullptr : &data_ptr[0];
}

int* Vector::end() {
    return n_elems == 0 ? nullptr : &data_ptr[n_elems];
}

// Comparators
bool Vector::operator ==(const Vector& v) const {
    if (n_elems != v.n_elems) return false;
    for (size_t i; i < n_elems; ++i){
        if (data_ptr[i] != v.data_ptr[i]){
            return false;
        }
    }
    return true;
}

bool Vector::operator !=(const Vector& v) const {
    return !(*this == v);
}

