#include <iostream>
#include <ctime>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int p, c;
vector<bool> hasC;

int totalPositive;
int totalCancer;

void run_experiment()
{
  int me = rand()%p;

  int result;

  if(hasC[me])
    {
      if(rand()%10==0)
	result = 0;
      else
	{
	  result = 1;
	  totalPositive++;
	  totalCancer++;
	}
    }

  if(!hasC[me])
    {
      if(rand()%10==0)
	{
	  result=1;
	  totalPositive++;
	}
      else
	result=0;
    }

}

int main()
{
  srand(time(0));
  cin>>p>>c; //p is the population, c is the number of people with cancer
  hasC.resize(p);
  for(int i=0;i<c;++i)
    hasC[i]=true;
  random_shuffle(hasC.begin(), hasC.end());

  for(auto i:hasC)
    cout<<i;
  cout<<endl;

  int n;
  cin>>n;

  while(n--)
    run_experiment();

  cout<<double(totalCancer)/totalPositive<<endl;

  return 0;
}
