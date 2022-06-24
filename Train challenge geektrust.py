import sys


# Function that will return the arrival of train at HYB station excluding all the bogies that lies before HYB
def arrivingHYB(Train, station_dict):

    # making the list of arrival train now contains only ["ARRIVAL", "TRAIN_A" or "Train_B", "ENGINE"]
    arrival = ["ARRIVAL"] + Train[:2]
    HYB = station_dict["HYB"]

    # Inserting only all the bogies that travel to HYB and after HYB
    for bogie in Train[2:]:
        if bogie not in station_dict or station_dict[bogie] >= HYB:
            arrival.append(bogie)

    return arrival

# Function that will return the assembled train that depart from HYB 
def departHYB(Train_A, Train_B, station_after_HYB):

    # list to store the boggies of Train_A and Train_B that depart HYB excluding HYB bogie or bogies,
    #  deleting individual HYB bogies of from Train_A and Train_B variable will take more time than storing all bogies that depart from HYB
    # excluding  HYB  
    bogies_that_depart_HYB = list()


    # Example list of Train_A = ["ARRIVAL", "TRAIN_A", "ENGINE", "NDL", "NDL", "GHY", "NJP", "NGP"]
    # iterating only boggies of Train_A that is from index 3 excluding unnecessary iteration
    for bogie in Train_A[3:]:
        if bogie != "HYB":
            bogies_that_depart_HYB.append(bogie)


    # iterating only boggies of Train_B that is from index 3 excluding unnecessary iteration
    for bogie in Train_B[3:]:
        if bogie != "HYB":
            bogies_that_depart_HYB.append(bogie)


    # Checking if there is no boggies to travel after HYB than the function will return None
    if len(bogies_that_depart_HYB) < 1:
        return None


    # sorting all the boggies in descending order 
    departure = sorted(bogies_that_depart_HYB, key= lambda x : station_after_HYB[x], reverse=True)

    # returns the output value
    return (["DEPARTURE", "TRAIN_AB", "ENGINE", "ENGINE"]+departure)


def main():
    # sys.argv[1] should give the absolute path to the input file
    input_file = sys.argv[1]

    # parse the file and process the command
    input_data = open(input_file, 'r')
    Train_A, Train_B = input_data.read().split("\n")
    Train_A = Train_A.strip().split()
    Train_B = Train_B.strip().split()

    # ALL station names with their distance from source station
    station_dictA = {"CHN": 0, "SLM": 350, "BLR": 550, "KRN": 900, "HYB": 1200,
                     "NGP": 1600, "ITJ": 1900, "BPL": 2000, "AGA": 2500, "NDL": 2700}

    station_dictB = {"TVC": 0, "SRR": 300, "MAQ": 600, "MAO": 1000, "PNE": 1400, "HYB": 2000,
                     "NGP": 2400, "ITJ": 2700, "BPL": 2800, "PTA": 3800, "NJP": 4200, "GHY": 4700}

    # ALL station names with their distance from HYB station till BPL and after BPL the station and distance are from their source station
    # so that the sorting can be done properly
    station_after_HYB = {"HYB": 0, "NGP": 400, "ITJ": 700, "BPL": 800,
                         "AGA": 2500, "NDL": 2700, "PTA": 3800, "NJP": 4200, "GHY": 4700}

    # print the output

    Train_A = arrivingHYB(Train_A, station_dictA)
    Train_B = arrivingHYB(Train_B, station_dictB)

    # printing values for arrival of Train_A in HYB
    print(" ".join(Train_A))

    # printing values for arrival of Train_B in HYB
    print(" ".join(Train_B))
    departure = departHYB(Train_A, Train_B, station_after_HYB)

    # Not sure what to print if there is no boggies to travel after HYB so therefore printing nothing for None value
    if departure!=None:

        # printing values for departure of both train from HYB
        print(" ".join(departure))


if __name__ == "__main__":
    main()