#include<iostream>
using namespace std;
int main(){

    int t;
    int n;
    int arr[100];
    cin>>t;
    cout<<"\n";
    for (int i=0; i<t;i++){

        cin>>n;
        for (int j=0;j<n;j++){
            cin>>arr[j];
        }
        int sum=0;
        for (int k=0;k<n;k++){
            sum=sum+arr[k];
        }
        cout<<sum<<endl;
        if (sum%2 ==0){
            cout<<"YES"<<endl;
        }
        else{
            cout<<"NO"<<endl;
        }
    }
}