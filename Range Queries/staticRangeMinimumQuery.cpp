#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const long long MAXN = 200000;  // Maximum input size
const long long LOG = 18;       // log2(200000) ≈ 18

long long st[MAXN][LOG]; 
vector<long long> arr;

void buildSparseTable(long long n)
{
    for (long long i = 0; i < n; i++)
        st[i][0] = arr[i];

    for (long long j = 1; (1 << j) <= n; j++)
    {
        for (long long i = 0; i + (1 << j) <= n; i++)
        {
            st[i][j] = min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
        }
    }
}

long long query(long long l, long long r)
{
    long long j = log2(r - l + 1);
    return min(st[l][j], st[r - (1 << j) + 1][j]);
}

int main()
{
    long long n, q;
    cin >> n >> q;

    arr.resize(n);
    for (long long i = 0; i < n; i++)
        cin >> arr[i];

    buildSparseTable(n);

    while (q--)
    {
        long long a, b;
        cin >> a >> b;
        cout << query(a - 1, b - 1) << endl; // Convert to 0-based index
    }

    return 0;
}
