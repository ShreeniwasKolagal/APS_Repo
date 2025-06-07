#include <iostream>
using namespace std;

int main()
{
    int n;

    cin >> n;

    if (n == 2 || n == 3)
    {
        cout << "No Solution";
        return 0;
    }

    // Even numbers first
    for (int i = 2; i <= n; i += 2)
        cout << i << " ";
    // Then odd numbers
    for (int i = 1; i <= n; i += 2)
        cout << i << " ";

    return 0;
}