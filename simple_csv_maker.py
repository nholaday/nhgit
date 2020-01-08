import csv

with open("myfile.csv", mode="w") as my_file:
    my_writer = csv.writer(my_file, delimiter=',')
    my_writer.writerow(['firstName','lastName','email'])
    my_writer.writerow(['Magneton','Vesuvius','magnewhat@gmail.com'])
