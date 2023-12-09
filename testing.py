import pickle

# Load the pickle file
with open('notebooks\\vector_index.pkl', 'rb') as file:
    data = pickle.load(file)

# Now 'data' contains the object you saved in the pickle file

        
if __name__ == "__main__":
    print(data)