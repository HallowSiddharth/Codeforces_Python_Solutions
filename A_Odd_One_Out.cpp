#include <stdio.h>
#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        if (a == b)
            cout << c << endl;
        else if (a == c)
            cout << b << endl;
        else
            cout << a << endl;
    }
    return 0;
}