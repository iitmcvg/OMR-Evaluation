#include<iostream>
using namespace std;
main()
{

    long int k1=1;
    long int k2=1;
    long int k3=1;
    long int k=0;
    while(k3<4000000)
    {
        k3=k2+k1;
        k1=k2;
        k2=k3;
       if(k3%2==0)
       k+=k3;
    }
    cout<<" the ans :"<<k;




}
