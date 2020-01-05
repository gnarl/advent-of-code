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

		sum += int(num/3) - 2
		fmt.Println(i, line)
	}
	fmt.Printf("sum: %d", sum)

}
