#include <iostream>
using namespace std;
class Channel{
    int subs;
    public:
        Channel(int s){
            subs = s;
        }
    void operator++(){
        subs++;
    }
    void display(){
        cout<<subs;
    }
};
int main(){
    Channel d(100);
    ++d;
    d.display();
}
