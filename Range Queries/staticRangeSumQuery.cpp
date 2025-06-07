#include <iostream>
#include <vector>
using namespace std;

/*
 * Given an array of n integers, your task is to process q queries of the form: what is the sum of values in range [a,b]?
 */

int main()
{
    long long n, q;
    cin >> n >> q;

    // Prefix sum array
    vector<long long> arr(n + 1, 0); 

    // 1 Based indexing, 0th index is always 0

    for (long long i = 1; i <= n; i++)
    {
        long long temp;
        cin >> temp;
        arr[i] = arr[i - 1] + temp;
    }

    while (q--)
    {
        long long a, b;
        cin >> a >> b;
        cout << arr[b] - arr[a - 1] << endl; 
    }

    return 0;
}