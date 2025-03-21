#include <iostream>
#include <chrono>
#include <thread>

void collatz(unsigned long long n) {
    unsigned long long orig = n;
    
    while (n > orig) {
        if (n % 2 == 0)
            n /= 2;
        else
            n = 3 * n + 1;
    }
}

void calc(int low, int high) {
    for (unsigned long long n = low; n <= high; n += 2) {
        collatz(n);
    }   
}

int main() {

    std::cout << "Launch? ";
    int x;
    std::cin >> x;

    auto start = std::chrono::high_resolution_clock::now();

    unsigned long long limit = 1'000'000'000;
    unsigned long long r = limit / 10; // number of simulatenous threads that CPU can run

    // for (unsigned long long n = 1; n <= limit; n += 2) {
    //     collatz(n);
    // }
    
    std::thread t1(calc, 1, r);
    std::thread t2(calc, r + 1, r * 2);
    std::thread t3(calc, 2 * r + 1, r * 3);
    std::thread t4(calc, 3 * r + 1, r * 4);
    std::thread t5(calc, 4 * r + 1, r * 5);
    std::thread t6(calc, 5 * r + 1, r * 6);
    std::thread t7(calc, 6 * r + 1, r * 7);
    std::thread t8(calc, 7 * r + 1, r * 8);
    std::thread t9(calc, 8 * r + 1, r * 9);
    std::thread t10(calc, 9 * r + 1, r * 10);

    t1.join();
    t2.join();
    t3.join();
    t4.join();
    t5.join();
    t6.join();
    t7.join();
    t8.join();
    t9.join();
    t10.join();

    auto end = std::chrono::high_resolution_clock::now();
    auto timeNS = std::chrono::duration_cast<std::chrono::nanoseconds>(end - start);
    
    std::cout << "Time taken: " << timeNS.count() << " ns | " << timeNS.count() / 1e9 << " s";
    return 0;
}
/*
*/
