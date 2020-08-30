// identification comments code block
// Nic Holaday
// Lab 1, Console Programming Basics
// Editor(s) used: Atom
// Compiler(s) used: g++ (Xcode)

#include <iostream>
using std::cout;
using std::cin;
using std::ios;

#include <string>
using std::string;

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
  int age;
  string name;
  double tempF;
  string city;
  string buf;

  // Get input of user information
  cout << "Enter your age: ";
  cin >> buf; age = atoi(buf.c_str());
  cin.ignore(200, '\n'); // clear the buffer to use getline

  cout << "Enter your name: ";
  getline(cin, name);

  cout << "Enter the temperature outside right now (degrees F): ";
  cin >> buf; tempF = atof(buf.c_str());
  cin.ignore(200, '\n');
  double tempC = (tempF - 32.0) * 5.0 / 9.0;

  cout << "What city are you in right now? ";
  getline(cin, city);
  
  // format, modify and display input back
  cout << name << " is " << age << " years old now, and will be "
  << age + 2 << " two years from now.\n";
  
  cout << "It's " << tempF << " degrees F in " << city << " -- thats ";
  cout.setf(ios::fixed);
  cout.precision(1); // display floats with 1 decimal 
  cout << tempC << " degrees C!\n";
  
  return 0;
}