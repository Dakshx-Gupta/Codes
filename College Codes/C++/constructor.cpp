#include <iostream>
using namespace std;
class A{
    public:
        A(){
            cout<<"A constructor"<<endl;
        }
        ~A(){
            cout<<"Destructor called of A"<<endl;
        }
};
class B: public A{
    public:
        B(){
            cout<<"B constructor"<<endl;
        }
        ~B(){
            cout<<"Destructor called of B"<<endl;
        }
};
int main(){
    B obj;
    return 0;
}
