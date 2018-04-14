#include <cstdio>
#include <iostream>
#include <fstream>
#include <cctype>
#include <cstdlib>

using namespace std;

ofstream txt;


void read(int pos0,int pos1){
  
  // txt.seekg(0, is.end);
  // int length = is.tellg();
  // txt.seekg(5, is.beg);

}

void write(string data){
    txt << data;
}

void open(){    
  txt.open (".txt",std::ios::app);
}
void close(){
  txt.close();
}


int main(){
    open();
    // write("1111");
    
    
    
    close();
  return 0;
}
