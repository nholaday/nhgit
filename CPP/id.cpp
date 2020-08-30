// identification comments code block
// Nic Holaday
// Lab 1, Console Programming Basics
// Editor(s) used: Atom
// Compiler(s) used: g++ (Xcode)

#include <iostream>
using std::cout;

void identification()
{
    // identification code block
    cout << "Nic Holaday\n\n";
    cout << "Lab 1, Console Programming Basics\n";
    cout << "Editor(s) used: Atom\n";
    cout << "Compiler(s) used: g++ (Xcode)\n";
    cout << "File: " << __FILE__ << "\n";
    cout << "Compiled: " << __DATE__ << " at " << __TIME__ << "\n\n";
}

int main()
{
    identification();
    return 0;
}
