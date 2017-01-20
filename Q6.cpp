#include<iostream>
#include<math.h>
using namespace std;

int rot(long long A[3],int h)
{
    int j=0;
    j=A[((h+2)%3)]+A[((h+1)%3)];
    return j;
}

void output(long long A[3])
{
    for(int i=0;i<3;i++)
        cout<<A[i]<<endl;
}

int check(long long A[3],int j)
{
    int length=1;
    int Test=0;
    Test=A[j];
    cout<<" no:"<<A[j]<<endl;
    while ( Test /= 10 )
    length++;
    return length;
}

main()
{
    long long A[3]={1,1};
    int h=2;
    int access=0;
    while(access==0)
    {
        if(check(A,((h+2)%3))>=4)
        {
            break;
            //access=1;
        }
        A[h]=rot(A,h);
        h++;
        h=h%3;
        cout<<" length "<<check(A,((h+2)%3))<<endl;
    }
    output(A);
}
