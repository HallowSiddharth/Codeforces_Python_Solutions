#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int MAX_SIZE = 9;
        int arr[MAX_SIZE];
        int n;
        cin >> n;
        for (int j = 0; j < n; j++)
        {
            cin >> arr[j];
        }
        int min_e = arr[0];
        int min_ind = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr[j] < min_e)
            {
                min_e = arr[j];
                min_ind = j;
            }
        }
        int ans = 1;
        arr[min_ind] += 1;
        for (int j = 0; j < n; j++)
        {
            ans *= arr[j];
        }
        cout << ans << endl;
    }
}