#include "animal.h"
using namespace std;

string padTrimString(const string& str, unsigned int length) {
    string ret = str;
    if (str.length() < length) {
        ret += string(length - str.length(), ' ');
    }
    else if (str.length() > length) {
        ret = str.substr(0, length - 3) + "...";
    }
    return ret;
}

template<typename T>
string padTrimNumber(const T& val, unsigned int length) {
    return padTrimString(to_string(val), length);
}

ostream& operator<<(ostream& os, const Animal& a) {
    os << a.getID() << "\t" 
        << padTrimString(a.getSpecies(), 30) << "\t"
        << a.getAge() << "\t"
        << padTrimString(a.getHealthCondition().description, 15) << "\t"
        << a.getVaccinationStatus().numVaccines << " (" 
                << padTrimNumber(a.getVaccinationStatus().getTotalHashValue(), 5) << ")" << "\t"
        << padTrimString(a.getSpecialNeeds(), 25);
    return os;
}

void Animal::display(unsigned int& ignoreCount, unsigned int& displayCount) const
{
    if (ignoreCount)
        --ignoreCount;
    else if (displayCount) {
        cout << *(this) << endl;
        --displayCount;
    }
}
