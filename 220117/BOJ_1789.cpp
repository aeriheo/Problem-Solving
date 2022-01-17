#include <iostream>
using namespace std;

int main(){
    long long s;
    cin>>s;
    long long sum = 0;
    long long n = 0;
    long long number = 1;
    while (sum < s){
        sum += number;
        number ++;
        n ++;
    }
    if (sum>s){
        for (int i=0;i<2;i++){
            number --;
            n --;
            sum -= number;
        }
        n ++;
    }
    cout<<n;
    return 0;
}