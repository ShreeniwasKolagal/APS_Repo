#include <iostream>
#include <vector>
using namespace std;

#define N 3

int c[N] = {2, 3, 5}; // Coin Denominations
int Sum = 9;          // Sum to be achieved

vector<int> dp(Sum + 1);

int main()
{
    // Initialize DP Array
    for (int i = 0; i <= Sum; i++)
    {
        dp[i] = 0;
    }
    dp[0] = 1; // For sum = 0, 1 solution exists

    for (int i = 0; i <= Sum; i++)
    {
        if (dp[i] != 0)
        {
            for (int j = 0; j < N; j++)
            {
                dp[i + c[j]] = dp[i] + dp[i + c[j]];
            }
            cout << "\nDP Array: ";
            for(int x = 0; x<=Sum; x++)
            {
                cout << dp[x] << " ";
            }
        }
    }

    cout << endl << dp[Sum] << endl;
}