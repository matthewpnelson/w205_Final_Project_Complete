# Zip Lookup by GeoTag
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))



# Function to Take a list of latlong polygons with associated zip codes and turn into a dictionary with key = zipcode
def import_zip_polygons(filename = '/home/w205/w205_Final_Project_Complete/evaluation1/San_Francisco_ZIP_Codes.csv'):
    import csv
    with open(filename, 'rt') as fin:
    # with open(os.path.join(__location__, filename),'rt') as fin:
        reader = csv.reader(fin, delimiter=',')
        latlong = []
        zipcode = []
        for row in reader:
            if row[0][0:7] == 'POLYGON':
                latlong.append(row[0][10:-2].split(","))
                zipcode.append(row[12])

        new_latlong = {}
        i = 0
        while i < len(zipcode):
            entry = []
            for LL in latlong[i]:
                str_tup = tuple(float(item) for item in LL.strip().split(" "))
                entry.append(str_tup)
            new_latlong[zipcode[i]] = entry
            i += 1

        return new_latlong

# Function to get min and max lat long from each box (to approximate a square...)
def zip_boxes(zip_polygons = import_zip_polygons()):
    BOXES = {}
    for zipcode, polygon in import_zip_polygons().items():
        for entry in polygon:
            running_min_lat = entry[-1]
            running_max_lat = entry[-1]
            running_min_long = entry[0]
            running_max_long = entry[0]
            break
        for entry in polygon:
            if entry[0] < running_min_long and entry[0] <= -120 and entry[0] > -123:
                running_min_long = entry[0]
            if entry[0] > running_max_long and entry[0] <= -120 and entry[0] > -123:
                running_max_long = entry[0]
            if entry[-1] < running_min_lat and entry[-1] <= 39 and entry[-1] > 36:
                running_min_lat = entry[-1]
            if entry[-1] > running_max_lat and entry[-1] <= 39 and entry[-1] > 36:
                running_max_lat = entry[-1]


        BOXES[zipcode] = [[running_min_lat, running_max_long], #min lat & max long = top right corner
                         [running_max_lat, running_min_long]] #max lat & min long = bottom left corner
    return BOXES

BOXES = zip_boxes()

# Function to check if a geotag is in a bounding box
def in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

def zip_lookup_by_geotag(geotag):
    for zipcode, coords in BOXES.items():
        if in_box(geotag, coords):
            zippy = zipcode
            return zippy
    return None         #Should build some error handling here?
