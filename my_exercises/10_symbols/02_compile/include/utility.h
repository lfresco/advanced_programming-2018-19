#include <string>
#include <algorithm>
#include <iostream>

#ifndef UTILITY_H__
#define UTILITY_H__

std::string to_upper(const std::string& s){
  static int n;
  ++n;
  auto z = s;
  std::transform(z.begin(), z.end(), z.begin(), ::toupper);
  std::cout << "function " << __func__ << " has been called " << n << " times\n";
  return z;
}

std::string to_lower(const std::string& os){
  auto s = os;
  std::transform(s.begin(), s.end(), s.begin(), ::tolower);
  return s;
}

#endif //UTILITY_H__
