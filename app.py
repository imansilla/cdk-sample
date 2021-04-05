#!/usr/bin/env python3

from aws_cdk import core

from sample.sample_stack import SampleStack


app = core.App()
SampleStack(app, "sample", env={'region': 'us-west-2'})

app.synth()
