#include <iostream>
#include <random>
#include <string> // to get string length

using namespace std;

// function to perform random monkey
// current is current best: intialized to all " "
void doMonkey(string &current, string &target, int &count){
    srand(time(nullptr));
    string new_guess = "";
    // build guess
    for (int i = 0; i < target.size(); i++){
        new_guess += 'a' + rand()%26;
    }
    cout << "trying guess " << new_guess << endl;

    // compare and save correct guesses
    for (int i = 0; i < new_guess.size(); i++){
        if (new_guess[i] == target[i]){
            // save
            current[i]=new_guess[i];
        }
    }

    // if we have the correct current, then print true
    if (current == target){
        cout << "monkey successful: " << current << endl;
        cout << "took " << count << " tries"<< endl;
    }

    else {
        count+=1; // increment number of tries
        cout << "current: " << current << endl;
        cout << "iteration: " << count << endl;
    }
}

int main(){
    string target = "life could be a dream";
    string current = "";
    for (int i = 0; i < target.size(); i++){
        current+=" ";
    }
    int count = 0;
    
    while (current != target){ // now to loop
        doMonkey(current, target, count);
    }
    
    return 0;
}