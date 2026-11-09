import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

#planned csv format is depth, pressure, temp, lumens


with open('testData.csv','r',newline='') as csvFile:
    reader=csv.reader(csvFile,delimiter=',')
    Depth = []
    Pressure = []
    Temp = []
    Lumens = []

    #index is used to skip headings
    #add data to a list that contains all related data (all depth or pressure)
    index=0
    for row in reader:
        if(index==0):
            index+=1
            continue
        Depth.append(float(row[0]))
        Pressure.append(float(row[1]))
        Temp.append(float(row[2]))
        Lumens.append(float(row[3]))
        
    #plot data
    plt.plot(Depth,Pressure,marker="o", color="b",label="Pressure")
    plt.plot(Depth,Temp,marker="o",color="r",label="Temperature")
    plt.plot(Depth,Lumens,marker="o",color="y",label="Lumens")

    #formatting
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.title("Pressure vs Depth", fontsize=16)
    plt.xlabel("Depth", fontsize=12)
    plt.ylabel("Pressure", fontsize=12)
    plt.legend()

    #save as png and close files
    plt.savefig("graph.png",dpi=150,pil_kwargs={'compress_level': 3})
    plt.close("all")
    csvFile.close()