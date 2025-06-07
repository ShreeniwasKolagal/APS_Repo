#include<iostream>
using namespace std;

bool subset_sum(int a[], int n, int sum) {
    if (sum == 0)
        return true;
    if (n == 0)
        return false;
    
    if (a[n - 1] > sum)
        return subset_sum(a, n - 1, sum);
    
    return subset_sum(a, n - 1, sum) || subset_sum(a, n - 1, sum - a[n - 1]);
}

int main() {
    int n = 5, sum = 7;
    int a[] = {1, 2, 3, 4, 5};
    
    if (subset_sum(a, n, sum))
        cout << "subset with the given sum found";
    else
        cout << "no required subset found";
    
    cout << endl; 
    return 0;
}
