// ! (https://cses.fi/problemset/)

#include <iostream>
#include <vector>
using namespace std;

/*
 You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
 Input
    The first input line contains an integer n.
    The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
 Output
    Print the missing number.
*/

int main()
{
    long long n;
    cin >> n;

    long long fullSum = n * (n+1) / 2;
    long long sum = 0;

    for(int i=1; i<n; i++)
    {
        long long temp;
        cin >> temp;
        sum += temp;
    }

    cout << (fullSum - sum);
}