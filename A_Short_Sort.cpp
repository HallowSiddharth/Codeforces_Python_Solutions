#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        string st;
        cin>>st;
        if (st[0] == 'a' || st[1] == 'b' || st[2] == 'c')
        cout<<"YES"<<endl;
        else
        cout<<"NO"<<endl;

    }
}