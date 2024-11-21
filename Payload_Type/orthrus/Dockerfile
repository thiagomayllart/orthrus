# pull in the appropriate language's payload container from itsafeaturemythic on dockerhub
FROM itsafeaturemythic/mythic_python_base:latest
RUN pip3 install requests
WORKDIR /Mythic/
CMD ["python3", "main.py"]