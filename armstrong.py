from fastapi import FastAPI
app = FastAPI()
def is_armstrong(num: int):
    num_str = str(num) 
    str_len = len(num_str) 
    sum_of_powers = sum(int(digit) ** str_len for digit in num_str)
    return num == sum_of_powers  
@app.get("/armstrong")
def check_armstrong(n: int):
    if is_armstrong(n):
        return {"number": n, "message": "IT IS AN ARMSTRONG NUMBER"}
    else:
        return {"number": n, "message": "IT IS NOT AN ARMSTRONG NUMBER"}