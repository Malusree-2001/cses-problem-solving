#include <iostream>
using namespace std;
int main(){
    long long n;
    cin >> n;
    long long sum = n * (n + 1) / 2;
    long long total = 0;
    for (long long i = 0; i < n - 1; i++)
    {
        long long x;
        cin >> x;
        total += x;
    
    }
    
    cout << sum - total;
}
