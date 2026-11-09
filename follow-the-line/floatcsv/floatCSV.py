import csv
import matplotlib.pyplot

with open('testData.csv','r',newline='') as csvFile:
    reader=csv.reader(csvFile,delimiter=',')
    Depth = []
    Pressure = []
    index=0
    for row in reader:
        
        Depth.append(row[0])
        Pressure.append(row[1])
        index+=1
    print(Depth)
    print(Pressure)
    matplotlib.pyplot.plot(Depth,Pressure,marker="o", color="b")
    matplotlib.pyplot.grid(True, linestyle="--", alpha=0.6)
    
    matplotlib.pyplot.title("Depth vs Pressure", fontsize=16)
    matplotlib.pyplot.xlabel("Pressure", fontsize=12)
    matplotlib.pyplot.ylabel("Depth", fontsize=12)
   
    matplotlib.pyplot.savefig("bagel.png",dpi=150,pil_kwargs={'compress_level': 3})
    print('idek')