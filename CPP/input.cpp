#include <iostream>
using std::cout;
using std::cin;

#include <string>
using std::string;
using std::getline; // if using getline

#include <cstdlib>

void line()
{
  string sentence;
  cout << "Type a sentence\n";
  getline(cin, sentence);
  cout << sentence << "\n";
}

int main()
{
  string buf;
  int fav;
  int total = 0;
  
  while (true)
  {
    cout << "Input your favorite number (q to quit): ";
    cin >> buf;
    cin.ignore(200, '\n'); // use to clear buffer before geline
    if (buf == "Q" || buf == "q") break;

    fav = atoi(buf.c_str());
    total += fav * fav;
    cout << "Your number squared is: " << fav * fav << "\n";
    cout << "Your total is " << total << "\n";
  }
  
  line();

  return 0;
}