#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main()
{
  srand(time(0));
  int n;
  int h=0, t=0;
  cin>>n;
  for(int i=0;i<n;++i)
    if(rand()%2)
      {
	cout<<"H";
	h++;
      }
    else
      {
	cout<<"T";
	t++;
      }

  cout<<endl<<double(h)/n<<" "<<double(t)/n<<endl;
  
  return 0;
}
