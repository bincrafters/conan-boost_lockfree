#include <boost/lockfree/queue.hpp>
#include <iostream>

boost::lockfree::queue<int> queue(128);

int main(int argc, char* argv[])
{
    using namespace std;
    cout << "boost::lockfree::queue is ";
    if (!queue.is_lock_free())
        cout << "not ";
    cout << "lockfree" << endl;
}