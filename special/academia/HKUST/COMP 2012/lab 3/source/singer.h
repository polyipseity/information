#include <string>
using namespace std;

class Singer {
private:
    string name;
    string nationality;
public:
    Singer(const string& name , const string& nationality);
    Singer(const Singer&) = delete;
    string getName() const;
    string getNationality() const;
};