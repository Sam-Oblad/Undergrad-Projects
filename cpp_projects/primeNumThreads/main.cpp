#include <iostream>
#include <thread>
#include <fstream>
#include <chrono>
using namespace std::chrono;
using namespace std;
mutex m;
int totalCount = 0;
int t1count = 0;
int t2count = 0;
int t3count = 0;
int t4count = 0;

ofstream myFile("Primes.dat");

bool isPrime(int num){
    if (num <= 1){
        return false;
    }
    for (int i = 2; i < num; i++){
        if (num % i == 0){
            return false;
        }
    }
    return true;
}

void numGenerator(int bottom, int top, int& t_counter){
    for (int i = bottom; i< top; i++){
        if (isPrime(i)){
            lock_guard<mutex> lck(m);
            totalCount++;
            myFile << i << endl;
            t_counter++;
        }
    }
}

int main(){
    //4 Threads: time = 24 sec
    auto start = high_resolution_clock::now();
    thread t1{numGenerator, 0,250000, ref(t1count)};
    thread t2{numGenerator, 250001,500000, ref(t2count)};
    thread t3{numGenerator, 500001,750000, ref(t3count)};
    thread t4{numGenerator, 750001,1000000, ref(t4count)};
    t1.join();
    t2.join();
    t3.join();
    t4.join();
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<seconds>(stop - start);
    cout << "Duration: " << duration.count() << " seconds" << endl;
    cout << "Total Primes Found: " << totalCount << endl;
    cout << "T1 Total primes found: " << t1count << endl;
    cout << "T2 Total primes found: " << t2count << endl;
    cout << "T3 Total primes found: " << t3count << endl;
    cout << "T4 Total primes found: " << t4count << endl;

    // SIMPLE LOOP: time = 56 sec
    // auto start = high_resolution_clock::now();
    // numGenerator(0, 1000000, t1count);
    // auto stop = high_resolution_clock::now();
    // auto duration = duration_cast<seconds>(stop - start);
    // cout << "Duration " << duration.count() << " seconds" << endl;

    return 0;
}
