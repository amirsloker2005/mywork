#include <iostream>
#include <limits>
#include <string>
#include <cctype>
#include <array>
using namespace std;
string polybiuscipher(string text, array<array<char, 5>, 5 > table, array<array<int, 5>, 5> keyorder, array<int,5> rows);
string low(string text);
bool textcheck(string text);
array<array<char, 5>, 5 > tablemaker(array<array<char, 5>, 5 > &table);
array<array<int, 5>, 5> keyordermaker(array<int, 5> order, array<array<int,5>, 5> &keys);
string polybiusdecipher(string text, array<array<char,5>,5> table, array<int,5> keysorder);
bool numcheck(string &text);
void orderinput(array<int, 5> &collector);
bool strdigitcheck(string text);
bool arrayfind(string value, array<int, 5> arr);
int main(){
    array<array<int, 5>, 5> keys;
    array<int, 5> keysinput;
    array<array<char, 5>, 5 > table;
    tablemaker(table);
    string choice;
    cout << "Choose what you want to do\n1) Cipher\n2) Decipher\n";
    cin >> choice;
    while (strdigitcheck(choice) || stoi(choice) < 1 || stoi(choice) > 2){
        cout << "invalid choice, Try again\nChoose what you want to do\n1) Cipher\n2) Decipher\n";
        cin >> choice;
    }
    if(stoi(choice) == 1){
        orderinput(keysinput);
        keyordermaker(keysinput, keys);
        cout << "  "<<keysinput[0]<<"  "<<keysinput[1]<<"  "<<keysinput[2]<<"  "<<keysinput[3]<<"  "<<keysinput[4]<<"\n"
             << keysinput[0]<<" A  B  C  D  E\n"
             << keysinput[1]<<" F  G  H  I/J K\n"
             << keysinput[2]<<" L  M  N  O  P\n"
             << keysinput[3]<<" Q  R  S  T  U\n"
             << keysinput[4]<<" V  W  X  Y  Z\n";
        string ciphertext;
        cout << "enter the text you want to cipher: ";
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        getline(cin, ciphertext);
        while(textcheck(ciphertext)){
            cout << "Enter a text that contains only letters and spaces: ";
            getline(cin, ciphertext);
        }
        ciphertext = low(ciphertext);
        cout << "The encryption for the following text \"" << ciphertext << "\"\nis \"" << polybiuscipher(ciphertext, table, keys, keysinput) << "\"\n" << endl;
    }else if(stoi(choice) == 2){
        orderinput(keysinput);
        keyordermaker(keysinput, keys);
        cout << "enter the numbers you want to decipher: ";
        cin.ignore();
        string deciphertext;
        getline(cin, deciphertext);
        while(numcheck(deciphertext)){
            cout << "Invalid input, write numbers only from 1 to 5.\nKeeping in mind that each two numbers next to each other are turned into a letter: ";
            cin.ignore();
            getline(cin, deciphertext);
        }
            cout << "The numbers you entered \""<< deciphertext << "\"\nis a Cipher for \"" << polybiusdecipher(deciphertext, table, keysinput) << "\"\n" << endl;
    }

    return 0;
}
string polybiuscipher(string text, array<array<char, 5>, 5 > table, array<array<int, 5>, 5> keyorder, array<int,5> rows){
    string result = ""; // to collect the ciphered characters
     for (char ch : text){
        if (ch == ' '){
            result += ch;
            continue;
        }else if (ch == 'j'){  // j is equal to i in this cipher
            ch = 'i';
        }
        for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++){
               if (table[i][j] == ch){
                result += to_string((rows[i]* 10) + keyorder[i][j]);
                break;
            }
            }
        }
     return result;
}
string low(string text){  // to turn any uppercase letter to lowercase
    string result = "";
    for(char ch : text){
        if(ch == ' '){
            result += " ";
        }else if ( 64 < (int)ch && (int)ch < 91 ){
            result += (char)(int)(ch + 32);
        }else if( 96 < (int)ch && (int)ch < 123 ){
            result += ch;
    }
    }
    return result;
}
bool textcheck(string text){  // numbers are not allowed in polybius cipher, so its ignored
    for(char ch : text){
        if(! isalpha(ch) && ch != ' '){
            return true;
        }
    }
    return false;
}
array<array<char, 5>, 5 > tablemaker(array<array<char, 5>, 5 > &table){  // a table that connect each letter to its meant row, number.
    array<array<char, 5>, 5> arr;
    int next = 0;
    for(int i = 0; i <5; i ++){
        for(int j = 0; j < 5; j++){
            if(i == 1 && j == 4){
                arr[i][j] = 'k';
                next += 2;
            }else {
                arr[i][j] = (char)(97 + next);
                next++;
            }
        }
    }
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            table[i][j] = arr[i][j];
        }
    }
    return table;
}
array<array<int, 5>, 5> keyordermaker(array<int,5> order, array<array<int, 5>, 5> &keys){  // to give each column in each row its meant number
    for(int i = 0; i < 5; i++){
        for(int j = 0; j < 5; j++){
            keys[i][j]= order[j];
        }
    }
    return keys;
}
bool numcheck(string &text){ // to check for input if it can be deciphered
    for(int i = 0;i < text.length(); i++){ // removes any spaces in the beginning
            if(isspace(text[i])){
            text = text.substr(i+1);
            i--;
            }else break;
    }
    int temp = 0;
    for(char ch: text){ // calculates the number of spaces between characters
        if(isspace(ch)){
            temp++;
            continue;
        }
        if(!isdigit(ch) || (isdigit(ch) && ((int)ch - 48 < 1 || (int)ch - 48 > 5))){ // checks if any charcter is within the range of 1 to 5
            return true;
        }
    }
    if((text.length() - temp) % 2 != 0){
        return true;
    }
    return false;
}
string polybiusdecipher(string text, array<array<char,5>,5> table,array<int,5> keysorder){
    string res = "";
    int row, column;
    for(int i = 0; i < (text.length() - 1); i++){
        if(isdigit(text[i]) && isdigit(text[i + 1])){
            for(int j = 0; j < 5; j++){
                if(keysorder[j] == stoi(string(1,text[i]))){
                    row = j;
                }
                if(keysorder[j] == stoi(string(1,text[i+1]))){
                    column = j;
                }
            }
            res.push_back(table[row][column]);
            i++;
        }else{
            res.push_back(' ');
        }
    }
    return res;
}
void orderinput(array<int, 5> &collector){ // to ask for five numbers for polybius cipher
        string keyinput;
    for(int i = 0; i < 5; i++){
        cout << "Type the key order no." << i+1 << ": ";
        cin >> keyinput;
        while (keyinput.length() > 1 || keyinput.length() == 0 || strdigitcheck(keyinput) || stoi(keyinput) < 1 || stoi(keyinput) > 5 || arrayfind(keyinput, collector)){
            cout << "Invalid input, type a valid integer from 1 to 5.\nKeeping in mind that you cannot choose the same number twice: ";
            cin >> keyinput;
        }
        collector[i] = stoi(keyinput);
    }
}
bool strdigitcheck(string text){ // to check if input is number or not
    for(char ch: text){
        if(!isdigit(ch))
            return true;
    }
    return false;
}
bool arrayfind(string value, array<int, 5> arr){  // to make sure that the number key is not put twice
    for(int ind : arr){
        if (stoi(value) == ind){
            return true;
        }
    }
    return false;
}
