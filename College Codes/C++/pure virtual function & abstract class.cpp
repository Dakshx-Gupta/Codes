#include <iostream>
using namespace std;

class Employee{
    public:
        virtual void pay() = 0;
};

class Payroll: public Employee{
    public:
        void pay() override{
            cout << "Salary credited to your bank";
        }
};

int main(){
    Employee *s;
    Payroll p;
    s = &p;
    // s = new Payroll();
    s -> pay();
    // delete s;
    return 0;
}
