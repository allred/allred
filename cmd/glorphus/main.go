package main

// https://github.com/golang-standards/project-layout

import (
	"fmt"

	"github.com/riandyrn/go-knn"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func main() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	knn := knn.NewKNN(knn.Configs{
		VectorDimension: 5,
		NumHashTable:    3,
		NumHyperplane:   3,
		SlotSize:        5,
	})
	fmt.Println(knn)
	log.Print("loggy")
	/*
	imageDocs := []ImageDoc{
		{
			ID:     "image_1.jpeg",
			Vector: []float64{0, 0, 0, 0, 0},
		},
	}
	*/
}
