#include <iostream>
#include <vector>
using namespace std;

class FenwickTree
{
public:
    vector<long long> Tree;
    long long n;

    FenwickTree(int size)
    {
        n = size;
        Tree.assign(n + 1, 0);
    }

    void add(long long i, long long x)
    {
        for (; i <= n; i += (i & -i))
        {
            Tree[i] += x;
        }
    }

    void update(long long l, long long r, long long x)
    {
        // Add till l...n
        add(l, x);
        // Subtract from r+1 ... n
        add(r + 1, -x);
    }

    long long get(long long i)
    {
        long long res = 0;
        for (; i > 0; i -= (i & -i))
        {
            res += Tree[i];
        }
        return res;
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
        tree.update(i, i, arr[i]);
    }

    while (q--)
    {
        long long t;
        cin >> t;

        if (t == 1)
        {
            long long a, b, u;
            cin >> a >> b >> u;
            tree.update(a, b, u);
        }
        else
        {
            long long k;
            cin >> k;
            cout << tree.get(k) << endl;
        }
    }

    return 0;
}
