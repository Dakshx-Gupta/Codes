#include <iostream>
using namespace std;
class A{
    public:
        void show(int a, int b){
            cout<<a+b<<endl;
        }
        void show(double a, double b){
            cout<<a+b<<endl;
        }
        void show(int a){
            cout<<a<<endl;
        }
};
int main(){
    A obj;
    obj.show(10, 10);
    obj.show(5.0, 5.0);
    obj.show(35);
}
