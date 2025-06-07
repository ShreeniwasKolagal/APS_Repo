// ! (https://cses.fi/problemset/)

#include <iostream>
#include <vector>
using namespace std;

int main()
{
    string in;
    cin >> in;

    long long n = in.size();
    char ch;
    long long ans = 0, cnt = 1;

    for (long long i = 1; i < n; i++)
    {
        if (in[i] == in[i - 1])
        {
            cnt++;
        }
        else
        {
            ans = max(ans, cnt);
            cnt = 1;
        }
    }
    ans = max(ans, cnt);

    cout << ans;
}