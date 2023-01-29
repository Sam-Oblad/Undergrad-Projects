// soccerTeamRoster.cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int jerseyNum;
int rating;
int i;
int j = 1;
char menuChoice; 
vector<int> jerseyNums(5);
vector<int> ratings(5);
void facilitator(char input);
void addPlayer(int jN, int r);
void userMenu();

// initializes jersey nums and ratings to two vectors
void acquirePlayers() {
   for (i = 1; i < 6; ++i){
      cout << "Enter player " << i << "'s jersey number:" << endl;
      cin >> jerseyNum;
      jerseyNums.at(i - 1) = jerseyNum;

      cout << "Enter player " << i << "'s rating:" << endl;
      cin >> rating;
      ratings.at(i - 1) = rating;
      cout << endl;
   }
}

// prints out a complete roster
void outputRoster() {
   cout << "ROSTER" << endl;
   for (unsigned int i = 1; i < ratings.size() + 1; ++i){
        cout << "Player " << i << " -- Jersey number: " << jerseyNums.at(i - 1) << ", Rating: " << ratings.at(i - 1) << endl;
   }
   cout << endl;
}

// prints out menu for user input and gets menuChoice as user input char
void userMenu() {
   cout << "MENU" << endl;
   cout << "a - Add player" << endl;
   cout << "d - Remove player" << endl;
   cout << "u - Update player rating" << endl;
   cout << "r - Output players above a rating" << endl;
   cout << "o - Output roster" << endl;
   cout << "q - Quit" << endl;
   cout << endl;
   cout << "Choose an option:" << endl;
   cin >> menuChoice;
   facilitator(menuChoice);
}

// calls appropriate function depending on menuChoice
void facilitator(char input){
   if (input == 'a'){
      cout << "Enter a new player's jersey number:" << endl;
      cin >> jerseyNum;
      cout << "Enter the player's rating:" << endl;
      cin >> rating;
      addPlayer(jerseyNum, rating);
      cout << endl;
      userMenu();
   }
   else if (input == 'd') {
      cout << "Enter a jersey number:" << endl;
      cin >> jerseyNum;
      for (unsigned int i = 0; i < jerseyNums.size(); ++i){
         if (jerseyNums[i] == jerseyNum){
            jerseyNums.erase(jerseyNums.begin() + i);
            ratings.erase(ratings.begin() + i);
         }
      }
      userMenu();
   }
   else if (input == 'u') {
      cout << "Enter a jersey Number:" << endl;
      cin >> jerseyNum;
      cout << "Enter a new rating for player:" << endl;
      cin >> rating;
      for (unsigned int i = 0; i < jerseyNums.size(); ++i){
         if (jerseyNums[i] == jerseyNum){
            ratings[i] = rating;
         }
      }
      userMenu();
   }
   else if (input == 'r') {
      cout << "Enter a rating:" << endl;
      cin >> rating;
      cout << "ABOVE " << rating << endl;
      for (unsigned int i = 0; i < ratings.size(); ++i){
         if (ratings[i] > rating){
            cout << "Player " << i + 1 << " -- Jersey number: " << jerseyNums.at(i) << ", Rating: " << ratings.at(i) << endl;
         }
      }
      cout << endl;
      userMenu();
   }
   else if (input == 'o') {
      outputRoster();
      userMenu();
   }
   else if (input == 'q') {
   }
}

// adds a player to roster
void addPlayer(int jN,int r) {
   jerseyNums.push_back(jN);
   ratings.push_back(r);
}

int main() {
   acquirePlayers();
   outputRoster();
   userMenu();
   return 0;
}
