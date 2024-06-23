package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/cloudwatch"
)

func main() {
	sess, err := session.NewSession(&aws.Config{Region: aws.String("us-west-2")}, nil)
	if err!= nil {
		log.Fatal(err)
	}

	cw := cloudwatch.New(sess)

	ctx := context.Background()
	input := &cloudwatch.PutMetricDataInput{
		Namespace: aws.String("PiNet-Manager/Security"),
		MetricData: []*cloudwatch.MetricDatum{
			{
				MetricName: aws.String("SecurityServiceBus"),
				Unit:       aws.String("Count"),
				Value:      aws.Float64(1.0),
			},
		},
	}

	_, err = cw.PutMetricDataWithContext(ctx, input)
	if err!= nil {
		log.Fatal(err)
	}

	fmt.Println("Security Service Bus metric sent to CloudWatch")
}
