#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n; // Read the number of elements

    int values[n+1]; // Array to store the values, using 1-based indexing

    // Read the input values, storing them in the array starting from index 1
    for(int i=1; i<=n; i++)
    {
        cin >> values[i];
    }

    values[0] = 0; // Set the base case: no elements give 0 value

    int dp[n+1]; // DP array to store the maximum sum up to each index
    dp[0] = 0; // No elements selected means a sum of 0
    dp[1] = values[1]; // If there's only one element, take it

    // Dynamic Programming: Compute the maximum sum possible without selecting adjacent elements
    for(int i=2; i<=n; i++)
    {
        // Either take the current element and the best sum up to i-2,
        // or skip the current element and take the best sum up to i-1.
        dp[i] = max(dp[i-1], dp[i-2] + values[i]);
    }

    cout << dp[n]; // Output the maximum sum possible
}
