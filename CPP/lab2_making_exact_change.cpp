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

#include <cstdlib>

int main()
{
  // identification code block
  cout << "Nic Holaday\n\n";
  cout << "Lab 1, Console Programming Basics\n";
  cout << "Editor(s) used: Atom\n";
  cout << "Compiler(s) used: g++ (Xcode)\n";
  cout << "File: " << __FILE__ << "\n";
  cout << "Compiled: " << __DATE__ << " at " << __TIME__ << "\n\n";
  
  double purchase;
  double tendered;
  double diff;
  string buf;

  // Get purchase and tenedered amount from user on one line space separated
  cout << "Enter the purchase amount and the tendered amount (space separated): ";
  cin >> buf; purchase = atof(buf.c_str());
  cin >> buf; tendered = atof(buf.c_str());
  // display how much change should be given with 2 decimal places
  diff = tendered - purchase;
  cout.setf(ios::fixed);
  cout.precision(2);
  cout << "$" << diff << "\n";

  //initialize all the denominations to 0
  int bill100 = 0;
  int bill50 = 0;
  int bill20 = 0;
  int bill10 = 0;
  int bill5 = 0;
  int bill1 = 0;
  int coin50 = 0;
  int coin25 = 0;
  int coin10 = 0;
  int coin5 = 0;
  int coin1 = 0;

  // Increment each denomination and subtract it from the diff
  // starting with the largest denomination.
  while (diff > 99.999999)
  {
    diff -= 100;
    bill100++;
  }
  while (diff > 49.999999)
  {
    diff -= 50;
    bill50++;
  }
  while (diff > 19.999999)
  {
    diff -= 20;
    bill20++;
  }
  while (diff > 9.999999)
  {
    diff -= 10;
    bill10++;
  }
  while (diff > 4.999999)
  {
    diff -= 5;
    bill5++;
  }
  while (diff > 0.999999)
  {
    diff -= 1;
    bill1++;
  }
  while (diff > 0.499999)
  {
    diff -= 0.50;
    coin50++;
  }
  while (diff > 0.249999)
  {
    diff -= 0.25;
    coin25++;
  }
  while (diff > 0.099999)
  {
    diff -= 0.10;
    coin10++;
  }
  while (diff > 0.049999)
  {
    diff -= 0.05;
    coin5++;
  }
  while (diff > 0.009999)
  {
    diff -= 0.01;
    coin1++;
  }
  
  // Print how many of each bill of change there is.  Add an "s" if more than 1.
  if (bill100 == 1)
  {
    cout << bill100 << " $100 bill\n";
  }
  else if (bill100 > 1)
  {
    cout << bill100 << " $100 bills\n";
  } 
  if (bill20 == 1)
  {
    cout << bill20 << " $20 bill\n";
  }
  else if (bill20 > 1)
  {
    cout << bill20 << " $20 bills\n";
  } 
  if (bill10 == 1)
  {
    cout << bill10 << " $10 bill\n";
  }
  else if (bill10 > 1)
  {
    cout << bill10 << " $10 bills\n";
  } 
  if (bill5 == 1)
  {
    cout << bill5 << " $5 bill\n";
  }
  else if (bill5 > 1)
  {
    cout << bill5 << " $5 bills\n";
  } 
  if (bill1 == 1)
  {
    cout << bill1 << " $1 bill\n";
  }
  else if (bill1 > 1)
  {
    cout << bill1 << " $1 bills\n";
  } 
  
  // Print how many of each coin of change there is.  Add an "s" if more than 1.
  if (coin50 == 1)
  {
    cout << coin50 << " 50-cent coin\n";
  }
  else if (coin50 > 1)
  {
    cout << coin50 << " $ 50-cent coins\n";
  } 
  if (coin25 == 1)
  {
    cout << coin25 << " 25-cent coin\n";
  }
  else if (coin25 > 1)
  {
    cout << coin25 << " $ 25-cent coins\n";
  } 
  if (coin10 == 1)
  {
    cout << coin10 << " 10-cent coin\n";
  }
  else if (coin10 > 1)
  {
    cout << coin10 << " $ 10-cent coins\n";
  } 
  if (coin5 == 1)
  {
    cout << coin5 << " 5-cent coin\n";
  }
  else if (coin5 > 1)
  {
    cout << coin5 << " $ 5-cent coins\n";
  } 
  if (coin1 == 1)
  {
    cout << coin1 << " 1-cent coin\n";
  }
  else if (coin1 > 1)
  {
    cout << coin1 << " 1-cent coins\n";
  } 

  cout << "\n";
  return 0;
}