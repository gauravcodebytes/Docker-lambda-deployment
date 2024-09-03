# Docker-lambda-deployment
 ML model serverless deployment over lambda function using docker image

Serverless functions

Serverless technologies enable developers to write and deploy code without needing to worry about provisioning and maintaining servers. One of the most common uses of this technology is serverless functions, which makes it much easier to author code that can scale to match variable workloads. With serverless function environments, you write a function that the runtime supports, specify a list of dependencies, and then deploy the function to production. The cloud platform is responsible for provisioning servers, scaling up more machines to match demand, managing load balancers, and handling versioning.

Serverless functions are an excellent tool for rapidly moving from prototype to production for your predictive models

AWS and GCP

Serverless functions were first introduced on AWS in 2015 and GCP in 2016. Both of these systems provide a variety of triggers that can invoke functions and a number of outputs that the functions can trigger in response. While it’s possible to use serverless functions to avoid writing complex code for gluing different components together in a cloud platform, we’ll explore a much narrower use case in this chapter. We’ll write serverless functions that are triggered by an HTTP request, calculate a propensity score for the passed in feature vector, and return the prediction as JSON. For this specific use case, GCP’s Cloud Functions are much easier to get up and running, but we’ll explore both AWS and GCP solutions.

Benefit:

The main benefit of this new paradigm is that developers can write code in a staging environment and then push code to production with minimal concerns about operational overhead. The infrastructure required to match the required workload can be automatically scaled as needed. This enables both engineers and data scientists to be more active in DevOps, because much of the operational concerns of the infrastructure are managed by the cloud provider.

![image](https://github.com/user-attachments/assets/c446714f-843a-412d-8e46-f8901763872f)

Manually provisioning servers, where you ssh into the machines to set up libraries and code, is often referred to as hosted deployments. Whereas, in managed solutions, the cloud platform is responsible for abstracting away this concern from the user. we’ll cover examples in both of these categories. Here are some of the different use cases we’ll cover:

Web endpoints: single EC2 instance (hosted) vs. AWS Lambda (managed) (-> Use case in this repository)
Docker: single EC2 instance (hosted) vs ECS (managed)
Messaging: Kafka (hosted) vs. PubSub (managed)

Here are some of the main issues to consider when deciding between hosted and managed solutions:

Iteration: Are you rapidly prototyping on a product or iterating on a system in production?
Latency: Is a multi-second latency acceptable for your SLAs?
Scale: Can your system scale to match peak workload demands?
Cost: Are you willing to pay more for serverless cloud costs?

AWS provides an ecosystem for serverless functions called Lambda. AWS Lambda is useful for gluing different components within an AWS deployment together since it supports a rich set of triggers for function inputs and outputs. While Lambda does provide a powerful tool for building data pipelines, the current Python development environment is a bit clunkier than GCP.

Containers:
When deploying data science models, it’s important to be able to reproduce the same environment used both for training and serving. In Models as Web Endpoints, I used the same machine for both environments, and in Models as Serverless Functions I used a requirements.txt file to ensure that the serverless ecosystem used for serving the model matched our development environment. Container systems such as Docker provide a tool for building reproducible environments, and they are much lighter weight than alternative approaches such as virtual machines.

The idea of a container is that it is an isolated environment in which you can set up the dependencies that you need in order to perform a task. The goal of a container framework is to provide isolation between instances with a lightweight footprint. With a container framework, you specify the dependencies that your code needs and let the framework handle the legwork of managing different execution environments.

Some examples of tasks that are performed in a container are:
performing ETL work
serving ML models
standing up APIs
hosting interactive web applications

Docker  is the de facto standard for containers, and there is substantial tooling built on this platform.
