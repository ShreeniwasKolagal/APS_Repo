#include<iostream>
#include<vector>
using namespace std;

int main()
{
    int t;
    cin >> t;

    vector<int> ans;
    while(t--)
    {
        int r, c;

        cin >> r >> c;

        if(r >= c)
            ans.push_back(r*r - (c-1));
        else
            ans.push_back(c*c - (r-1));

    }

    for(auto i : ans)
        cout << i << " ";
}