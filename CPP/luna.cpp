#include <iostream>
// using namespace std;
using std::cout;
using std::ios;

#include <string>
using std::string;

int multiPrinter(string word, int count)
{
    for (int i = 0; i < count; i++) {
        cout << word << "\n";
    }
    // cout << "Press ENTER or RETURN to continue..."; // use this instead
    // cin.get( ); 
    return count;
}

int main()
{
    cout << multiPrinter("luna", 13) << '\n';
    
    // cout.setf(ios::fixed);
    // cout.precision(2);
    // double d = 10.0/3.0;
    // cout << d << '\n';

    return 0;
}
