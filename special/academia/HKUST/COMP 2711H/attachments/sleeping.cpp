#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int totalW;
int totalH;
int totalT;

void run_experiment()
{
  int coin = rand()%2;
  if(coin==1)
    {
      totalW++;
      totalH++;
      cout<<"H";
    }
  else
    {
      totalW+=2;
      totalT+=2;
      cout<<"TT";
    }
}

int main()
{
  srand(time(0));
  int n;
  cin>>n;
  for(int i=0;i<n;++i)
    run_experiment();

  cout<<endl;

  cout<<totalW<<"  "<<double(totalH)/totalW<<" "<<double(totalT)/totalW<<endl;
  
  return 0;
}
