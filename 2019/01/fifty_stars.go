package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readLines(path string) ([]string, error) {

	file, err := os.Open(path)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	var lines []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func fuel_mass(mass int) int {
	sum := 0
	for mass > 0 {
		extra_fuel := int(mass/3) - 2
		if extra_fuel < 0 {
			mass = 0
		} else {
			sum += extra_fuel
			mass = extra_fuel
		}

	}
	return sum
}

func main() {
	fmt.Println("vim-go")

	path := "input.txt"
	lines, err := readLines(path)
	check(err)

	// Sum of fuel requirements for all modules
	sum := 0
	for i, line := range lines {
		num, err := strconv.Atoi(line)
		check(err)

		input_mass := int(num/3) - 2
		input_mass += fuel_mass(input_mass)

		sum += input_mass
		fmt.Println(i, line)
	}
	fmt.Printf("sum: %d", sum)

}
