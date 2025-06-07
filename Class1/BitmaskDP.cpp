#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;

const int N = 3;
int dp[1 << N];

int BitMaskDP(int Cost[N][N])
{
    // ! Last mask i.e., 111 for N=3
    int fullMask = (1 << N) - 1;

    // Initialize DP array
    for (int i = 0; i <= fullMask; i++)
    {
        dp[i] = INT_MAX;
    }
    dp[0] = 0;

    // Iterate all possible masks, includes fullMask
    for (int mask = 0; mask <= fullMask; mask++)
    {
        // Count workers assigned, i.e., Number of set bits in mask
        int x = __builtin_popcount(mask);

        if (x >= N)
            continue;

        // Try assinging task to this worker
        for (int j = 0; j < N; j++)
        {
            // If task j is not assigned. i.e., jth bit is not set in mask
            if (!(mask & (1 << j)))
            {
                int newMask = mask | (1 << j);
                dp[newMask] = min(dp[newMask], dp[mask] + Cost[x][j]);
            }
        }
        cout << "DP Array at Iteration " << mask + 1 << ": ";
        for (int i = 0; i <= fullMask; i++)
        {
            if (dp[i] == INT_MAX)
                cout << -1 << " ";
            else
                cout << dp[i] << " ";
        }
        cout << endl;
    }

    return dp[fullMask];
}

int main()
{
    int Cost[N][N] = {
        {3, 2, 7},
        {5, 1, 3},
        {2, 7, 2}};

    int ans = BitMaskDP(Cost);

    cout << "Answer: " << ans << endl;
}