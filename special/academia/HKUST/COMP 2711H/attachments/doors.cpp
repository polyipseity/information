#include <iostream>
#include <ctime>
#include <cstdlib>
#include <algorithm>
using namespace std;

int p1, p2;

void run_experiment()
{
  int door[3] = {0, 0, 0};
  door[rand()%3]=1;

  //player chooses a door
  int choice = rand()%3;

  //host opens another door
  int opened_door;
  for(int i=0;i<3;++i)
    if(i==choice)
      continue;
    else if(door[i]==1)
      continue;
    else
      opened_door = i;

  int rem_choice;
  for(int i=0;i<3;++i)
    if(i!=choice && i!=opened_door)
      rem_choice = i;

  if(door[choice]==1)
    {
      cout<<"1";
      p1++;
    }

  if(door[rem_choice]==1)
    {
      cout<<"2";
      p2++;
    }
  
}

int main()
{
  srand(time(0));
  int n;
  cin>>n;
  for(int i=0;i<n;++i)
    run_experiment();

  cout<<endl<<double(p1)/n<<" "<<double(p2)/n<<endl;
  
  return 0;
}
