from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"App is running"}

@app.get("/items/{itemId}")
def read_item(itemId: int):
    #fetch from db or do any calculation
    return {"itemId": itemId}



# Asyncio : It allows python to handle multiple operations efficiently

# Call several api
# wait till a api gets resolved
# process multiple requests

async def fetch_data(name: str):
    await asyncio.sleep(delay)
    return f"Hello {name}"


# Numpy : a python library computation. Provides multidimensional array and tools to work with the array.

# pip install numpy
# import numpy as np

# np.array([1,2,3]) - creates a simple array
# np.zeros((3,3)) /np.ones((2,4))
import numpy as np

vec1 = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5]
], dtype=np.float32)

vec2 = np.array([
    [9, 6, 7],
    [2, 3, 4],
    [3, 4, 5]
], dtype=np.float32)

# operations

vec1 + vec2
vec1 - vec2

# indexing & slicing
vec1[0]
vec2[1, 2]
vec2[:, 1]


# Langchain

