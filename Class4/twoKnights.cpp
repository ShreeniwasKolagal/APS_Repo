#include <iostream>
using namespace std;

int twoKnights(int n)
{
    // Base Case
    if (n == 1)
        return 0;

    // Total Number of placements with Two Knights is Choose( n*n, 2 )
    int totalWays = (n * n) * (n * n - 1) / 2;

    // Total Number of attacking ways
    int attackWays = 4 * (n - 1) * (n - 2);

    return totalWays - attackWays;
}

int main()
{
    int k;
    cin >> k;

    // Solution from 1x1 to kxk Board
    for (int n = 1; n <= k; n++)
    {
        cout << twoKnights(n) << endl;
    }
}