#include <iostream>
#include <vector>
using namespace std;

class FenwickTree
{
public:
    vector<long long> Tree;
    long long n;

    FenwickTree(long long size)
    {
        n = size;
        Tree.assign(n + 1, 0);
    }

    void update(long long i, long long x)
    {
        for (; i <= n; i += (i & -i))
            Tree[i] += x;
    }

    long long sum(long long i)
    {
        long long sum = 0;
        for (; i > 0; i -= (i & -i))
        {
            sum += Tree[i];
        }

        return sum;
    }

    long long query(long long l, long long r)
    {
        return sum(r) - sum(l - 1);
    }
};

int main()
{
    long long n, q;
    cin >> n >> q;

    vector<long long> arr(n + 1);
    FenwickTree tree(n);

    for (long long i = 1; i <= n; i++)
    {
        cin >> arr[i];
        tree.update(i, arr[i]);
    }

    while(q--)
    {
        long long c, a, b;
        cin >> c >> a >> b;

        if(c == 1)
        {
            long long diff = b - arr[a];
            arr[a] = b;
            tree.update(a, diff);
        }
        else
        {
            cout << tree.query(a, b) << endl;
        }
    }

    return 0;
}