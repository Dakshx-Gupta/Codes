#include <iostream>
using namespace std;
class A{
    public:
        virtual void show(){
            cout << "A show";
        }
};
class B: public A{
    public:
        void show() override{
            cout << "B show";
        }
};
int main(){
    A* ptr;
    B obj;
    ptr = &obj;
    ptr -> show();
}
