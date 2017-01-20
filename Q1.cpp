#include<iostream>
using namespace std;
main()
{
    int k=0;
    for(int x=1;x<1000;x++)
    {
        if((x%3==0)||(x%5==0))
        k+=x;

    }
    cout<<" the ans :"<<k;
}
