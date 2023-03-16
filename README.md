# SageMaker SDK Sandbox

[![MIT License](https://img.shields.io/github/license/cvpaperchallenge/Ascender?color=green)](LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Code style: flake8](https://img.shields.io/badge/code%20style-flake8-black)](https://github.com/PyCQA/flake8)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Typing: mypy](https://img.shields.io/badge/typing-mypy-blue)](https://github.com/python/mypy)

# Prerequisite

## (Optional) IAM role for SageMaker

If you want to run SageMaker jobs (e.g. training job) from your local PC, IAM role which SageMaker assume is needed. For detail please check offical docs: https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html

In this repo, we provide AWS CDK code which create the IAM for SageMaker jobs. If you use CDK to create IAM role please follow following instruction. You can also create IAM role from AWS console by following above official docs.

First, install AWS CDK as follows:

```bash
# Install AWS CDK
$ npm i -g aws-cdk

# Install AWS Cloud Development Kit Library
$ pip3 install aws-cdk-lib
```

You can check installed AWS CDK version by cdk --version.

Then let's deploy IAM role for SageMaker jobs.

```bash
% export AWS_PROFILE=<YOUR_AWS_PROFILE>

% cdk synth -c env=dev
% cdk bootstrap -c env=dev
% cdk deploy -c env=dev

# When you want to delete role, please execute:
% cdk destroy -c env=dev
```

# How to test code

```bash
% export AWS_PROFILE=<YOUR_AWS_PROFILE>
% export SAGEMAKER_ROLE_ARN=<YOUR_SAGEMAKER_ROLE_ARN>

% poetry install
% poetry run python scripts/<PY_FILE_NAME>
```

## Links

- ML Enablement Series

  - [Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/tag/ml-enablement-series/)

- AWS Black Belt Amazon SageMaker Trainingで機械学習のモデル開発を楽にする

  - [YouTube](https://www.youtube.com/watch?v=byEawTm4O4E)
  - [GitHub](https://github.com/aws-samples/aws-ml-jp/tree/main/sagemaker/sagemaker-traning/tutorial)
  - [Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/tag/ml-enablement-series/)

- AWS Black Belt Amazon SageMaker Training ハンズオン編

  - [YouTube](https://www.youtube.com/watch?v=tgo2F2OY5bU)
  - [PDF](https://d1.awsstatic.com/webinars/jp/pdf/services/Dark_03_Training_Job_Handson.pdf)

- [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/)

- [Prior SageMaker Framework Container Versions](https://github.com/aws/deep-learning-containers/blob/master/available_images.md#prior-sagemaker-framework-container-versions)
