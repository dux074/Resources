package main

import (
	"bufio"
	"flag"
	"fmt"
	"net/url"
	"os"
	"strings"
)

func main() {
	helpPtr := flag.Bool("h", false, "Show usage.")
	flag.Parse()
	if *helpPtr {
		help()
	}
	input := ScanTargets()
	output := GetPaths(RemoveDuplicateValues(input))
	for _, elem := range output {
		fmt.Println(elem)
	}
}

//help shows the usage
func help() {
	var usage = `Take as input on stdin a list of urls/paths and print on stdout all the unique paths (at any level).
	$> cat input | cleanpath`
	fmt.Println()
	fmt.Println(usage)
	fmt.Println()
	os.Exit(0)
}

//ScanTargets return the array of elements
//taken as input on stdin.
func ScanTargets() []string {

	var result []string

	// accept domains on stdin
	sc := bufio.NewScanner(os.Stdin)
	for sc.Scan() {
		domain := strings.ToLower(sc.Text())
		result = append(result, domain)
	}
	return result
}

//RemoveDuplicateValues >
func RemoveDuplicateValues(strSlice []string) []string {
	keys := make(map[string]bool)
	list := []string{}

	// If the key(values of the slice) is not equal
	// to the already present value in new slice (list)
	// then we append it. else we jump on another element.
	for _, entry := range strSlice {
		if _, value := keys[entry]; !value {
			keys[entry] = true
			list = append(list, entry)
		}
	}
	return list
}

//GetPaths
func GetPaths(s []string) []string {
	var result []string
	for _, elem := range s {
		if len(elem) != 0 {
			var paths []string
			if HasProtocol(elem) {
				if GetPath(elem) != "" {
					paths = GetAllLevelsPaths(GetPath(elem))
				}
			} else {
				if elem[0] == '/' {
					elem = elem[1:]
				}
				paths = GetAllLevelsPaths(elem)
			}
			if len(paths) != 0 {
				result = append(result, paths...)
			}
		}
	}
	return RemoveDuplicateValues(result)
}

//HasProtocol
func HasProtocol(input string) bool {
	res := strings.Index(input, "://")
	return res >= 0
}

//RemoveProtocol
func RemoveProtocol(input string) string {
	res := strings.Index(input, "://")
	if res >= 0 {
		return input[res+3:]
	} else {
		return input
	}
}

//GetPath >
func GetPath(input string) string {
	u, err := url.Parse(input)
	if err != nil {
		return ""
	}
	if len(u.Path) > 1 {
		return u.Path[1:]
	} else {
		return ""
	}

}

//GetAllLevelsPaths
func GetAllLevelsPaths(input string) []string {
	if input == "" {
		return []string{}
	}
	var result []string
	if input[len(input)-1] != '/' {
		input = input + "/"
	}
	var elems = strings.Split(input, "/")
	if len(elems) == 2 {
		return []string{elems[0]}
	}
	for i := range elems {
		if elems[i] == "*" {
			break
		}
		for j := 1; j < i; j++ {
			if strings.Contains(elems[j], "*") || elems[j] == "*" {
				break
			}
			resTemp := strings.Join(elems[:j+1], "/")
			result = append(result, resTemp)
		}
	}
	return RemoveDuplicateValues(result)
}
