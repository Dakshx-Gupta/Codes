#include <iostream>
using namespace std;
class A{
    public:
        void show(){
            cout << "A show";
        }
};
class B: public A{
    public:
        void show(){
            cout << "B show"; // here the show function of A is being overriden
        }
};
int main(){
    B obj;
    obj.show();
}
