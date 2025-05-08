///////// Student Info/////////
//
//           Your Name: ZHENG MIAN
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//
#include <iostream>
#include <map>
#include <string>

using namespace std;

class PhoneBook
{
private:
    map<string, string> contacts; // Maps names to phone numbers

public:
    // TO-DO: Implement the constructor
    PhoneBook()
    {
    }

    // TO-DO: Implement addContact(const string &name, const string &number)
    void addContact(const string &name, const string &number)
    {
        if (contacts.find(name) != contacts.end())
        {
            contacts[name] = number;
        }
        else
        {
            contacts.insert({name, number});
        }
    }

    // TO-DO: Implement removeContact(const string &name)
    void removeContact(const string &name)
    {
        contacts.erase(name);
    }

    // TO-DO: Implement findContact(const string &name)
    string findContact(const string &name)
    {

        auto it = contacts.find(name);
        if (it != contacts.end())
        {
            return it->second;
        }
        else
        {
            return "Not Found!";
        }
    }

    // TO-DO: Implement displayAllContacts()
    void const  displayAllContacts(){
        for(auto &entry: contacts){
            cout<<entry.first<< " -> " << entry.second<<endl;
        }
    }
};

int main()
{
    PhoneBook pb;
    pb.addContact("Alice", "12345678");
    pb.addContact("Bob", "23456789");
    pb.addContact("Charlie", "34567890");

    // Display contacts
    cout << "All Contacts:" << endl;
    pb.displayAllContacts();
    cout << endl;

    // Find a contact
    string searchName = "Charlie";
    cout << "The contact number of " << searchName << ": "
         << pb.findContact(searchName) << endl
         << endl;

    searchName = "David";
    cout << "The contact number of " << searchName << ": "
         << pb.findContact(searchName) << endl
         << endl;

    // Remove a contact
    pb.removeContact("Bob");
    cout << "After removing Bob, contacts are:" << endl;
    pb.displayAllContacts();

    return 0;
}
