import json

class SatData:
    def __init__(self):
        with open('sat.json', 'r') as infile:
            self._csv_data = json.load(infile)

    def save_as_csv(self, dbn_lst):
        new_row_lst = []
        new_row_lst.append("DBN, School Name, Number of Test Takers, Critical Reading Mean, Mathematics Mean, Writing Mean" )
        # sort the dbn rows in ascending order
        sorted_dbns = sorted(dbn_lst)
        # check if dbns are in the _csv_data
        for i, dbn in enumerate(self._csv_data["data"]):
            if self._csv_data["data"][i][8] in sorted_dbns:
        # save that row in a list along
                    new_row_lst.append(f"{self._csv_data["data"][i][8]}, {self._csv_data["data"][i][9]}, {self._csv_data["data"][i][10]}, {self._csv_data["data"][i][11]}, {self._csv_data["data"][i][12]}, {self._csv_data["data"][i][13]}")
        # write a new csv with file with the header and dbn rows
        with open('output.csv', 'w') as outfile:
            for row in new_row_lst:
                outfile.write(row + '\n')
        # print(new_row_lst)
        

sd = SatData()
dbns = ["02M303", "02M294", "01M450", "02M418"]
sd.save_as_csv(dbns)