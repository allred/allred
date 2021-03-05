package main
import (
    "context"
    "fmt"
    "github.com/influxdata/influxdb-client-go/v2"
    "log"
    "os"
    "time"
)

func influxdb_client() (c influxdb2.Client) {
    token := os.Getenv("DEV_INFLUXDB_TOKEN")
    url := os.Getenv("DEV_INFLUXDB_URL")
    fmt.Println("URL: ", url)
    client := influxdb2.NewClientWithOptions(url, token,
        influxdb2.DefaultOptions(),
            //.SetUseGZip(false),
    )
    //fmt.Println("client: ", client)
    return client
}

func main() {
    log.Println("START")
    client := influxdb_client()
    fmt.Println(client)
    //dur, some, err := client.Ping()
    org := os.Getenv("DEV_INFLUXDB_ORG")
    //bucket := os.Getenv("DEV_INFLUXDB_BUCKET")
    queryAPI := client.QueryAPI(org)
    //fmt.Println(queryAPI.queryURL())
    // let's point to a local clone
    // https://github.com/influxdata/influxdb-client-go/blob/master/api/query.go
    // https://github.com/influxdata/influxdb-client-go/blob/master/api/examples_test.go

    bucketsAPI := client.BucketsAPI()
    log.Println("BUCKET: ", bucketsAPI)

    log.Println("INFLUX: ", influxdb2)
    return

    /*
    query_test := `
    from(bucket:"mikejallred's Bucket")
      |> range(start:-1h)
      |> filter(fn:(r) =>

        r._measurement == "cpu"
      )
    `
    fmt.Println(queryAPI)
    fmt.Println(queryAPI.Query(context.Background(), query_test))
    */

    //query_flux := `from(bucket:"` + bucket + `")|> range(start: -1h) |> filter(fn: (r) => r._measurement == "stat")`

    /*
    query_flux := `from(bucket:"mikejallred's bucket")
      |> range(start: -1h)
      |> filter(fn:(r) =>
        r._measurement == "cpu"
        and r.cpu == "cpu-total"
        and r._field == "usage_user"
      )
    `
    */
    query_flux := `from(bucket:"mikejallred's bucket") |> range(start: -10m)`

    // it IS being parsing, add this to the end of the query to see syntax error
      //|> yield()

    //query_flux := `from(bucket:"mikejallred's bucket") |> range(start: -1h) |> filter(fn:(r) => r._measurement == "cpu" and r.cpu == "cpu-total" and r._field == "usage_user") `

    log.Println("DEBUG: ", query_flux)
    //result, err := queryAPI.Query(context.Background(), query_flux)
    //result, err := queryAPI.QueryRaw(context.Background(), query_flux, influxdb2.DefaultDialect())
    result, err := queryAPI.QueryRaw(context.Background(), `from(bucket:"my-bucket")|> range(start: -1h) |> filter(fn: (r) => r._measurement == "stat")`, influxdb2.DefaultDialect())

    log.Println("RESULT: ", result)
    if err == nil {
        log.Println("YAY: ", result)
    } else {
        panic(err)
    }
    //result, err := queryAPI.QueryRaw(context.Background(), `from(bucket:"my-bucket")|> range(start: -1h) |> filter(fn: (r) => r._measurement == "stat")`, influxdb2.DefaultDialect())

    log.Println("DEBUG: ", result)
    log.Println("DEBUG: ", err)
    client.Close()
    log.Println("ENDED: ", time.Now())
}
