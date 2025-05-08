///////// Student Info/////////
//
//           Your Name: Zheng Mian
//      Your NTU Email: zhen0158@e.ntu.edu.sg
//
//
//
#include <iostream>
#include <list>
#include <string>

class PatientQueue
{
private:
    std::list<std::string> queue; // Stores patient names
public:
    // Constructor: Initializes an empty patient queue
    PatientQueue() : queue() {}
    ~PatientQueue() {}

    // TO-DO 1: Implement the function addPatient to add a new patient's name to the end of the queue
    void addPatient(const std::string &name)
    {
        queue.push_back(name);
    }

    // TO-DO 2: Implement the function servePatient: removes and returns the patient at the front of the queue
    // If the queue is empty, returns a reminder message
    std::string servePatient()
    {
        if (queue.empty())
        {
            return "Empty queue!";
        }
        std::string patient = queue.front();
        queue.pop_front();
        return patient;
    }

    // TO-DO 3: Implement the function isEmpty
    bool isEmpty() const
    {
        return queue.empty();
    }

    // TO-DO 4: Implement the function displayQueue to print out all patients in order
    void displayQueue() const
    {
        for (const std::string &name : queue)
        {
            std::cout << name << " ";
        }
        std::cout << std::endl;
    }
};

int main()
{
    PatientQueue clinicQueue;

    // Test 1: Add patients
    clinicQueue.addPatient("Alice");
    clinicQueue.addPatient("Bob");
    clinicQueue.addPatient("Charlie");

    std::cout << "Current queue: ";
    clinicQueue.displayQueue();
    std::cout << std::endl;

    // Test 2: Serve a patient
    std::cout << "Serving patient: " << clinicQueue.servePatient() << std::endl;
    std::cout << "Queue after serving: ";
    clinicQueue.displayQueue();
    std::cout << std::endl;

    // Test 3: Serve more until the queue is empty
    std::cout << "Serving patient: " << clinicQueue.servePatient() << std::endl;
    std::cout << "Serving patient: " << clinicQueue.servePatient() << std::endl;
    std::cout << std::endl;

    // Test 4: Check if it is empty
    if (clinicQueue.isEmpty())
    {
        std::cout << "No patient in the queue now" << std::endl;
    }
    std::cout << "Serving patient: " << clinicQueue.servePatient() << std::endl;

    return 0;
}
