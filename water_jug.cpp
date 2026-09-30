#include <iostream>
using namespace std;

int main() {
    int jug1 = 0;
    int jug2 = 0;

    cout << "Initial State: (" << jug1 << ", " << jug2 << ")" << endl;

    // Fill Jug 1 (4 liters)
    jug1 = 4;
    cout << "Fill Jug 1:    (" << jug1 << ", " << jug2 << ")" << endl;

    // Pour Jug 1 into Jug 2
    jug2 = 3;
    jug1 = 1;
    cout << "Pour Jug 1 -> Jug 2: (" << jug1 << ", " << jug2 << ")" << endl;

    // Empty Jug 2
    jug2 = 0;
    cout << "Empty Jug 2:   (" << jug1 << ", " << jug2 << ")" << endl;

    // Pour Jug 1 into Jug 2
    jug2 = jug1;
    jug1 = 0;
    cout << "Pour Jug 1 -> Jug 2: (" << jug1 << ", " << jug2 << ")" << endl;

    // Fill Jug 1 again
    jug1 = 4;
    cout << "Fill Jug 1:    (" << jug1 << ", " << jug2 << ")" << endl;

    // Pour Jug 1 into Jug 2
    jug1 = 2;
    jug2 = 3;
    cout << "Pour Jug 1 -> Jug 2: (" << jug1 << ", " << jug2 << ")" << endl;

    cout << "\nTarget achieved: 2 liters" << endl;

    return 0;
}