# Use the official AWS Lambda Python 3.11 base image
FROM public.ecr.aws/lambda/python:3.11

# Copy requirements file and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model file
COPY logit.py .
COPY logit.pkl .

# Set the default command to your handler
CMD ["logit.lambda_handler"]

