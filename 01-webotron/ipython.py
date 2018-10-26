# coding: utf-8
import boto3
import click

session = boto3.Session(profile_name='python')
s3 = session.resource('s3')
