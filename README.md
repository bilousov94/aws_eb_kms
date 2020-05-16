# aws_eb_kms
This repo is source code for article [How to hide your security credentials in AWS Elastic Beanstalk environment with KMS and S3 bucket](https://medium.com/@valentynbilousov/how-to-hide-your-security-credentials-in-aws-elastic-beanstalk-environment-with-kms-and-s3-bucket-2159448d73ee)
 
 <strong>master</strong> branch contains source code for default flask app from [aws docs](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
 
 <strong>secret_display</strong> branch contains modified code to read data from existing s3 bucket and decrypt it with kms
