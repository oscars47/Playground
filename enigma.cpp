#include <iostream>
#include <cmath>
using namespace std;

// functions to generate lucas numbers
int lucas(double x){
    return int(pow(((1+pow(5.0, 0.5)) / 2 ), x) + pow(((1-pow(5.0, 0.5)) / 2 ), x));
}

// function to do encryption 
void encrypt(const string input[], string output[], const int key[]){
    cout<<'hello'<<endl;
}


int main(){
    string ALPHABET[] = {"a", "b", "c", "d", "e", "f", "g", "h", "i", 
"j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
"v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", 
"H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
"T", "U", "V", "W", "X", "Y", "Z", ".", ",", ";", ":", "—", "!", "#", 
"$", "%", "&", """, ", "(", ")", "*", "/", "?", "@", "[", 
"]", "^", "-", "_", "{", "|", "}"};

    
    return 0;
}