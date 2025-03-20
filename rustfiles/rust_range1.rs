//Rust Range Program

use std::time::Instant;

fn collatz(n: u64) -> u64 {
    let mut count = 0;
    let mut num = n;

    while num != 1 {
        if num % 2 != 0 {
            num = (num * 3 + 1) / 2; // Optimized step for odd numbers
        } else {
            num /= 2; // Step for even numbers
        }
        count += 1;
    }
    count
}

fn main() {
    let mut lower_bound = String::new();
    let mut upper_bound = String::new();

    println!("Enter the lower bound:");
    std::io::stdin().read_line(&mut lower_bound).expect("Failed to read line");
    //let lower_bound: u64 = lower_bound.trim().parse().expect("Please enter a valid number");

    println!("Enter the upper bound:");
    std::io::stdin().read_line(&mut upper_bound).expect("Failed to read line");
    //let upper_bound: u64 = upper_bound.trim().parse().expect("Please enter a valid number");

    let start_time = Instant::now();

    for i in lower_bound..=upper_bound {
        let steps = collatz(i);
        // println!("Number: {}, Steps: {}", i, steps);
    }

    let duration = start_time.elapsed();
    println!("Time taken: {:?}", duration);
}
