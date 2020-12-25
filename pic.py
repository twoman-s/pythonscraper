import pickle
import os.path

example = None

if os.path.isfile("dict.pickle"):
    print("Exist")
    pickle_in = open("dict.pickle", "rb")
    dicts = pickle.load(pickle_in)
    print(dicts)
    pickle_in.close()
    dicts[3] = "c"
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(dicts, pickle_out)
    pickle_out.close()
else:
    example = {1: "a", 2: "b"}
    pickle_out = open("dict.pickle", "wb")
    pickle.dump(example, pickle_out)
    pickle_out.close()
    print("No file exist")
