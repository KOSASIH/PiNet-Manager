package main

import (
	"context"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/iam"
)

func main() {
	sess, err := session.NewSession(&aws.Config{Region: aws.String("us-west-2")}, nil)
	if err!= nil {
		log.Fatal(err)
	}

	iamSvc := iam.New(sess)

	ctx := context.Background()
	input := &iam.CreatePolicyInput{
		PolicyName: aws.String("VisionSecurityPolicy"),
		PolicyDocument: aws.String(`{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "security:*",
					"Resource": "*"
				}
			]
		}`),
	}

	_, err = iamSvc.CreatePolicyWithContext(ctx, input)
	if err!= nil {
		log.Fatal(err)
	}

	fmt.Println("Vision Security Policy created")
}
