FROM python  
COPY . /src  
CMD ["python", "/src/app.py"]