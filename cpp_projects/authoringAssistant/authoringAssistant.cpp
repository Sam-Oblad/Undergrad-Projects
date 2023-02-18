#include <iostream>
#include <string>
#include <tuple>
#include <vector>

using namespace std;
//function declaration
void mainMenu(string givenText);

//shortens the string by removing excess spaces, passes by reference
void ShortenSpace(string& myString){
   for (unsigned int i = 0; i < myString.size(); i++){
      if (myString[i] == ' ' && myString[i-1] == ' '){
         myString.erase(i, 1);
         i -= 1; // This line ensures that all extra spaces are removed by backtracking i
      }
   }
}

//Replaces all '!' with '.', passes by reference
void ReplaceExclamation(string& myString){
   for (unsigned int i = 0; i < myString.size(); i++){
      if (myString[i] == '!'){
         myString[i] = '.';  
      }
   }
}

//finds the occurences of a given string (searchStr) within a given string (givenText) returns the amount of occurrences
int FindText(string searchStr, string givenText){
   vector <size_t> positions;
   size_t pos = givenText.find(searchStr, 0);
   while(pos != string::npos){
      positions.push_back(pos);
      pos = givenText.find(searchStr,pos+1);
   }
   return positions.size();
}

//Gets number of chars that are not white space
int GetNumOfNonWSCharacters(string myString){
   int nonWhiteSpace = 0;
   for (unsigned int i = 0; i < myString.size(); i++){
      if (myString[i] != ' '){
         nonWhiteSpace += 1;  
      }
   }
   return nonWhiteSpace;  
}

//gets the number of words in a string
int GetNumOfWords(string myString){
   int words = 0; 
   for (unsigned int i = 0; i < myString.size(); i++){
      if (myString[i] == ' ' && myString[i -1] != ' ')
      words += 1;
      }
   return words + 1;
}

//prints out user menu 
void PrintMenu(){
   cout << "MENU" << endl;
   cout << "c - Number of non-whitespace characters" << endl;
   cout << "w - Number of words" << endl;
   cout << "f - Find text" << endl;
   cout << "r - Replace all !'s" << endl;
   cout << "s - Shorten spaces" << endl;
   cout << "q - Quit" << endl;
   cout << endl;
}

//main algorithm that organizes all user choices and calls appropriate functions above
void ExecuteMenu(char userChoice, string myString, string searchStr = ""){
   if (userChoice == 'q'){
      ;
   }
   if (userChoice == 'c'){
      int countNonWhite = GetNumOfNonWSCharacters(myString);
      cout << "Number of non-whitespace characters: " << countNonWhite << endl;
      cout << endl;
   }
   if (userChoice == 'w'){
      int numWords = GetNumOfWords(myString);
      cout << "Number of words: " << numWords << endl;
      cout << endl;
   }
   if (userChoice == 'f'){
      int numAppearances = FindText(searchStr, myString);
      cout << '"' << searchStr << "\" " << "instances: " << numAppearances << endl;
      cout << endl;
   }
   if (userChoice == 'r'){
      ReplaceExclamation(myString);
      cout << "Edited text: " << myString << endl;
      cout << endl;
   }
   if (userChoice == 's'){
      ShortenSpace(myString);
      cout << "Edited text: " << myString << endl;
      cout << endl;
   }
} 

//Main - program starts here
int main() {
   string givenText;
   char userChar = 'z';
   cout << "Enter a sample text:" << endl;
   cout << endl;
   getline(cin, givenText);
   cout << "You entered: "<< givenText << endl;
   cout << endl;
   PrintMenu();
   cout << "Choose an option:" << endl;

   cin >> userChar;
   while (userChar != 'q' || userChar == ' '){
      if (userChar == 'q' || userChar == 'c' || userChar == 'w' || userChar == 'r' || userChar == 's'){
         ExecuteMenu(userChar, givenText);
         PrintMenu();
         cout << "Choose an option:" << endl;
         cin >> userChar;
      }
      else if (userChar == 'f'){
         string searchStr;
         cout << "Enter a word or phrase to be found:" << endl;
         getline(cin, searchStr);
         getline(cin, searchStr);
         ExecuteMenu(userChar, givenText, searchStr);
         PrintMenu();
         cout << "Choose an option:" << endl;
         cin >> userChar;
      }
      else{
         cin >> userChar;
      }
   }
   return 0;
}