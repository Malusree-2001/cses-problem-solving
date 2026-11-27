#include <iostream>
int main() {
    std::string s;
    std::cin >> s;
    int n = s.length();
    char m = s[0];
    int count = 1;
    int best = 1;
    for (int i = 1; i <n; i++){
        if (s[i] == m){
            count++;
        } else {
            m = s[i];
            count = 1;
        }
        if (count > best){
            best = count;
        }
    }
    std::cout << best;
}