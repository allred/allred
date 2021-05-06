package main

import (
	"fmt"

	"github.com/riandyrn/go-knn"
)

func main() {
	knn := knn.NewKNN(knn.Configs{
		VectorDimension: 5,
		NumHashTable:    3,
		NumHyperplane:   3,
		SlotSize:        5,
	})
	fmt.Println(knn)
}
