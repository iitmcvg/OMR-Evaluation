#include<iostream>
#include<math.h>
using namespace std;

const int limit=1000;

struct node
{
    int data;
    struct node *next;
};


class stack
{
    struct node *top;
    public:
    stack() // constructor
    {
        top=NULL;
    }
    struct node *A[1000];
    int h=0;
    //int value,i;
    void push(int);// to insert an element
    void pop();// to delete an element
    void show(); // to show the stack
    int lencheck(int);
    int digitno();
    int digitfinder();
    node* showaddress(int);
    void stackdelete();
~stack()
{
    node *current = top;
    while( current!= NULL )
    {
        node *temp = current->next;
        delete current;
        current = temp;
    }
    top=NULL;
}

};



void stack::stackdelete()
{
   node *current = top;
    while( current!= NULL )
        {
            node *temp = current->next;
            delete current;
            current = temp;
        }
    top=NULL;
h=0;

}



int stack::digitno(){
    return h;}

node* stack::showaddress(int i){
     return A[i-1];   }

void stack::push(int value)
{

    struct node *ptr;
    //cout<<"Enter a number to insert: ";
    ptr=new node;
    ptr->data=value;
    ptr->next=NULL;
    if(top!=NULL)
        ptr->next=top;
    top=ptr;
    A[h]=top;
    h++;
    //cout<<"nNew item is inserted to the stack!!!";

}

void stack::pop()
{
    struct node *temp;
    if(top==NULL)
    {
        cout<<"nThe stack is empty!!!";
    }
    temp=top;
    top=top->next;
    //cout<<"nPOP Operation........nPoped value is "<<temp->data;
    delete temp;
}


void stack::show()
{
    struct node *ptr1=top;
    cout<<"The no: is ";
    while(ptr1!=NULL)
    {
        cout<<ptr1->data;
        ptr1=ptr1->next;
    }
    cout<<endl;
}


int stack::lencheck(int data){

    int length=1;
    int Test=0;
    Test=data;
    cout<<" no:"<<data<<endl;
    while ( Test /= 10 )
    length++;
    return length;
}


int stack::digitfinder(){
    int a;
    cout<<"type digit no:";
    cin>>a;
    node *temp;
    temp=showaddress(a);
    cout<<temp->data;
    return temp->data;

}


void adder(stack A1, stack A2, stack &A3)
{
    int i,j=0;
    if(A1.digitno()<A2.digitno())
    {
        for(j=0;j<A1.digitno();j++)
        {
            node *temp1,*temp2,*temp3;
            temp1=A1.showaddress(j+1);
            temp2=A2.showaddress(j+1);

            if(A3.digitno()<=j+1)
            {
                A3.push(((temp1->data)+(temp2->data))%10);
                if(((temp1->data)+(temp2->data))>=10)
                   {
                     if(j+1==A2.digitno())
                        A3.push(1);
                      if((j+1<=A1.digitno()))
                      {
                        temp2=A2.showaddress(j+2);
                        temp2->data++;

                      }
                   }
            }
        }

    while(j<A2.digitno() )
    {
        node *temp2;
        temp2=A2.showaddress(j+1);
        if(temp2->data>=10)
        {
            A3.push((temp2->data)%10);
            if(j+1<A2.digitno())
            {
            temp2=A2.showaddress(j+2);
            temp2->data++;
            }
            if(j+1==A2.digitno())
                A3.push(1);

        }
        else
            A3.push((temp2->data));
        j++;

    }


  }
    if(A2.digitno()<=A1.digitno())
    {
        for(i=0;i<A2.digitno();i++)
        {
            node *temp1,*temp2,*temp3;
            temp1=A1.showaddress(i+1);
            temp2=A2.showaddress(i+1);

            if(A3.digitno()<=i+1)
            {
                A3.push(((temp1->data)+(temp2->data))%10);
                if(((temp1->data)+(temp2->data))>=10)
                   {
                     if(A1.digitno()==A2.digitno())
                     {
                         if(i+1==A1.digitno())
                        A3.push(1);
                     //if(((i+2)==A1.digitno())&&((i+2)==A2.digitno()))
                       // A3.push(1);
                      if((i+1<A2.digitno()))
                      {
                        temp1=A1.showaddress(i+2);
                        temp1->data++;
                      }
                     }
                      if(A1.digitno()!=A2.digitno())
                     {
                         if(i+1==A1.digitno())
                        A3.push(1);
                     //if(((i+2)==A1.digitno())&&((i+2)==A2.digitno()))
                       // A3.push(1);
                      if((i+1<=A2.digitno()))
                      {
                        temp1=A1.showaddress(i+2);
                        temp1->data++;
                      }
                     }
                   }
            }
        }
        while(i<A1.digitno() )
        {
            node *temp1;
            temp1=A1.showaddress(i+1);
            cout<<endl<<"data temp1 :"<<temp1->data<<endl;
            if(temp1->data>=10)
            {
                A3.push((temp1->data)%10);
                if(i+1<A1.digitno())
                {
                    temp1=A1.showaddress(i+2);
                    temp1->data++;
                }
                if(i+1==A1.digitno())
                 A3.push(1);

            }
            else
                A3.push((temp1->data));
            i++;
        }
    }
}



void Fibonacci(stack &A1,stack &A2,stack &A3, long long int &counter)
{
 int key=0;
 stack A4,A5;
 while(key==0)
 {
     int access=0;
     if(A3.digitno()==0)
     {
         int h=A1.digitno();
         for(long long int i=0;i<h;i++)
        {
            node *new1;
            cout<<"1";
            new1=A1.showaddress(i+1);
            A4.push(new1->data);
        }
          h=A2.digitno();
        for(long long int i=0;i<h;i++)
        {
            node *new2;
            new2=A2.showaddress(i+1);
            A5.push(new2->data);
        }
         A4.show();
         A5.show();
         adder(A4,A5,A3);
         access=1;
         cout<<"access"<<access<<"A31"<<endl;
         A3.show();
         counter++;
         if((A1.digitno()>=limit)||(A2.digitno()>=limit)||(A3.digitno()>=limit))
            key=1;

     }

      if(A2.digitno()==0)
     {
          int h=A3.digitno();
        for(long long int i=0;i<h;i++)
        {
           cout<<"2a";
            node *new1;
            new1=A3.showaddress(i+1);
            A4.push(new1->data);

        }
          h=A1.digitno();
        for(long long int i=0;i<h;i++)
        {
            node *new2;
            new2=A1.showaddress(i+1);
            A5.push(new2->data);
        }
        A4.show();
        A5.show();
         adder(A4,A5,A2);
         access=2;
           cout<<"access"<<access<<"A32"<<endl;
         A3.show();
         counter++;
          if((A1.digitno()>=limit)||(A2.digitno()>=limit)||(A3.digitno()>=limit))
            key=1;

     }

     if(A1.digitno()==0)
     {
          int h=A2.digitno();
        for(long long int i=0;i<h;i++)
        {
            node *new1;
            new1=A2.showaddress(i+1);
            A4.push(new1->data);
        }
          h=A3.digitno();
        for(long long int i=0;i<h;i++)
        {
            node *new2;
            new2=A3.showaddress(i+1);
            A5.push(new2->data);
        }
       A4.show();
       A5.show();
         adder(A4,A5,A1);
         access=3;
          cout<<"access"<<access<<"A33"<<endl;
         A3.show();
         counter++;
          if((A1.digitno()>=limit)||(A2.digitno()>=limit)||(A3.digitno()>=limit))
            key=1;
     }

     A4.stackdelete();
     A5.stackdelete();
     if(access==1)
        A1.stackdelete();
     if(access==2)
        A3.stackdelete();
     if(access==3)
        A2.stackdelete();

   }
  cout<<" the index is :"<<counter<<endl;

}


main()
{
    int choice;
    stack A1,A2,A3,A4;
    long long int counter=2;
   do
    {
        int val;

        cout<<"1)digit enter:A1  2)digit enter:A2  3)Fibonacci  4)show no:  5)exit"<<endl;
        cin>>choice;
        if(choice==1)
        {  cin>>val;
            A1.push(val);
        }
        if(choice==2)
        {   cin>>val;
            A2.push(val);
        }
        if(choice==3)
         Fibonacci(A1,A2,A3,counter);

        if(choice==4)

        {
          if(A1.digitno()==0)
          {
              cout<<"A2:";
              A2.show();
              cout<<"A3:"<<endl;
              A3.show();
          }
           if(A2.digitno()==0)
          {
               cout<<"A1:";
              A1.show();
              cout<<"A3:"<<endl;
              A3.show();
          }
           if(A3.digitno()==0)
          {
              cout<<"A1:";
              A1.show();
              cout<<"A2:"<<endl;
              A2.show();
          }
        }

    }
    while(choice!=5);



}









