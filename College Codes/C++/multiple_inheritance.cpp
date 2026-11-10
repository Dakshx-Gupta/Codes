// Multiple inheritance
#include <iostream>
using namespace std;
class A{
    public:
        void showA(){
            cout<<"This is A"<<endl;
        }
};
class B{
    public:
        void showB(){
            cout<<"This is B"<<endl;
        }
};
class C: public A, public B{
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
