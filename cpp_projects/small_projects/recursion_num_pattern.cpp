//recursion_num_pattern.cpp
#include <iostream>

using namespace std;


void PrintNumPattern(int num1, int num2, bool hitZero = false){
   //Stores initial value of num1 in static form
   static int staticNum1 = num1;

   int tempNum1 = num1;
   cout << tempNum1 << ' ';
   
   //Checks if num1 has been negative before
   if (hitZero == true){
      //Increments num1 by num2 until num1 == staticNum1 (initial value of num1)
      if (num1 == staticNum1){
      }
      else{
         PrintNumPattern(num1 + num2, num2, true);
      }
   }
   //Decrements num1 by num2 until num1 goes negative one time
   else{
      if (num1 < 0){
         PrintNumPattern(num1 + num2, num2, true);
      }
      else{
         PrintNumPattern(num1 - num2, num2);
      }
   }
}

int main() {
   int num1;
   int num2;

   cin >> num1;
   cin >> num2;
   PrintNumPattern(num1, num2);
   cout << endl;
   return 0;
}