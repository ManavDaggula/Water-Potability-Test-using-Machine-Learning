import pandas as pd
import numpy as np
import pickle as pkl

with open("model.pkl","rb") as file:
    model = pkl.load(file)

def get_pred(ph,hardness,solids,chloramines,sulfates,conductivity,carbon,trihalomethanes,turbidity):
    input_values = pd.DataFrame.from_dict({
        "ph":[np.float64(ph)],
        "Hardness":[np.float64(hardness)],
        "Solids":[np.float64(solids)],
        "Chloramines":[np.float64(chloramines)],
        "Sulfate":[np.float64(sulfates)],
        "Conductivity":[np.float64(conductivity)],
        "Organic_carbon":[np.float64(carbon)],
        "Trihalomethanes":[np.float64(trihalomethanes)],
        "Turbidity":[np.float64(turbidity)]
    })
    output = model.predict(input_values)[0]

    mean_range = [7.11, 195.91, 22344.92, 7.17, 332.46, 425.01, 14.29, 66.58, 3.99]
    std_range = [1.44, 35.28, 8886.06, 1.73, 47.42, 81.9, 3.26, 16.29, 0.78]

    if(output==1):
        return ("Safe for drinking.","")
    else:
        # reasons = ""
        for i in range(9):
            if(abs(input_values.values[0][i]-mean_range[i])>std_range[i]):
                return ("Not safe for drinking",input_values.columns[i])
        return ("Not safe for drinking","Unknown")
