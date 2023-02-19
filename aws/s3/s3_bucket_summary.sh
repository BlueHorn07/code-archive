#!/usr/bin/env bash

S3_BUCKET="target-bucket-name"
PREFIX="prefix-path/"

aws s3 ls s3://$S3_BUCKET/$PREFIX --recursive --human-readable --summarize
