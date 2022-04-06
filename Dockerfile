# Pull base image
FROM python:3.9-alpine
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt
# Copy project
COPY . /code/
ENTRYPOINT ["python", "/code/manage.py"]
CMD ["runserver", "0.0.0.0:1234"]