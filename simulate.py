import geopandas
import pandas as pd
import numpy as np

data = geopandas.read_file(r"C:\Users\mbici\Desktop\Portfolio Ptojects\Spatial peoject\data\hotosm_ken_roads_lines.shp")

def simulate_data(n = len(data["geometry"])):
    data_dict ={
        "accidents":np.random.randint(100,size=n),
        "amounts":np.random.randint(low= 40000,high = 1000000,size=n),

    }
    
    df = pd.DataFrame(data_dict,columns=["accidents","amounts"])
    simulated_data = data[["name","geometry","highway","oneway"]].join(df)
    return simulated_data
simulated_data = simulate_data()
simulated_data.to_csv("roads.csv")
