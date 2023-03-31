#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using std::cout;
using std::endl;
using std::ifstream;
using std::string;
using std::vector;


void readFile(ifstream& inputFile){
    vector<string> words;
    string line;
    string word;
    ifstream newFile;
    while (getline(inputFile, line)){
        std::istringstream iss(line);
        while (getline(iss, word, ' ')) {
            words.push_back(word);
        }
    }
    for (int i = 0; i < words.size(); i++){
        if (words[i][0] == '@'){
            string fileName = words[i];
            fileName.erase(0,1);
            newFile.open(fileName);
            if(newFile.is_open()){
                readFile(newFile);
            }
            else{
                cout << "Failed to open File: " << fileName << endl;
                continue;
            }
            continue;
        }
        cout << words[i] << endl;
    }
}

int main(int argc, char *argv[]){
    ifstream myFile;
    myFile.open(argv[1].erase(0,1));
    if (!myFile.is_open()){
        cout << "Failed to open file: " << argv[1] << endl;
        return 1;
    }
    readFile(myFile);


    return 0;
}