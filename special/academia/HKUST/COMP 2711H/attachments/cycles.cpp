#include <iostream>
using namespace std;

const int MAXN = 1e5;

bool seen[MAXN];

int main()
{
  int p, a;
  cin>>p>>a;
  for(int i=0;i<p;++i)
    if(!seen[i])
      {
	for(int j=i;!seen[j];j*=a,j%=p)
	{
	  seen[j]=true;
	  cout<<j<<" ";
	}
      cout<<endl;
      }
  return 0;
}
