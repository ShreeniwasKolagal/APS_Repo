#include <iostream>
#include <vector>
using namespace std;

int main()
{
    long long n, q;
    cin >> n >> q;

    vector<long long> prefixXor(n + 1, 0);

    for (long long i = 1; i <= n; i++)
    {
        cin >> prefixXor[i];
        prefixXor[i] ^= prefixXor[i - 1];
    }

    while(q--)
    {
        long long a, b;
        cin >> a >> b;

        cout << (prefixXor[b] ^ prefixXor[a-1]) << endl;
    }

    return 0;
}