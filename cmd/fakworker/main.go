package main

import (
	"context"
	//"github.com/rs/zerolog"
	worker "github.com/contribsys/faktory_worker_go"
	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"
)

func someFunc(ctx context.Context, args ...interface{}) error {
  help := worker.HelperFor(ctx)
	log.Printf("Working on job %s\n", help.Jid())
  return nil
}

func bluetoothFunc(ctx context.Context, args ...interface{}) error {
  help := worker.HelperFor(ctx)
	log.Printf("Working on job %s\n", help.Jid())
  return nil
}

func main() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	//fmt.Println("vim-go")
	mgr := worker.NewManager()
	mgr.Register("SomeJob", someFunc)
	mgr.Register("BluetoothJob", bluetoothFunc)
	mgr.Concurrency = 1
	mgr.ProcessStrictPriorityQueues("critical", "default", "bulk")
	mgr.Run()
}
