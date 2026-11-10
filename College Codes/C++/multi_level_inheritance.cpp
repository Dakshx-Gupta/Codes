// Multi-level inheritance
#include <iostream>
using namespace std;
class A{
    public:
        void showA(){
            cout<<"This is A"<<endl;
        }
};
class B: public A{
    public:
        void showB(){
            cout<<"This is B"<<endl;
        }
};
class C: public B{
    public:
        void showC(){
            cout<<"This is C"<<endl;
        }
};
int main(){
    C obj;
    obj.showA();
    obj.showB();
    obj.showC();
}
