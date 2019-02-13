from datetime import datetime

import dateutil
from bson import ObjectId

from aquascope.webserver.data_access.db import Item


DUMMY_ITEMS = [
    Item({
        "_id": ObjectId('000000000000000000000000'),
        "file_size": 1.0,
        "aspect_ratio": 1.0,
        "maj_axis_len": 1.0,
        "min_axis_len": 1.0,
        "orientation": 1.0,
        "eccentricity": 1.0,
        "solidity": 1.0,
        "estimated_volume": 1.0,
        "area": 1.0,
        "intensity_gray_mass_displace_in_images": 0.008681178096776,
        "intensity_gray_moment_hu_4": 6.44407178777693e-12,
        "intensity_gray_moment_hu_5": 1.58949394588895e-22,
        "intensity_gray_moment_hu_6": 4.87549139791229e-15,
        "intensity_gray_moment_hu_7": 9.29907144602865e-23,
        "intensity_gray_std_intensity": 44.4518848935367,
        "intensity_gray_moment_hu_1": 0.00162911271992,
        "intensity_gray_moment_hu_2": 6.02185718988395e-07,
        "intensity_gray_moment_hu_3": 1.26728600174152e-10,
        "intensity_gray_median_intensity": 87.0,
        "intensity_gray_mass_displace_in_minors": 0.021203842389859,
        "intensity_gray_mean_intensity": 84.08,
        "intensity_gray_perc_25_intensity": 39.0,
        "intensity_gray_perc_75_intensity": 124.0,
        "intensity_red_mass_displace_in_images": 0.016106449593647,
        "intensity_red_moment_hu_4": 6.23065353203622e-12,
        "intensity_red_moment_hu_5": 2.82161622605635e-23,
        "intensity_red_moment_hu_6": 4.08980777153774e-15,
        "intensity_red_moment_hu_7": 2.18575645069997e-22,
        "intensity_red_std_intensity": 33.6895555570746,
        "intensity_red_moment_hu_1": 0.002005703596185,
        "intensity_red_moment_hu_2": 8.66777471825988e-07,
        "intensity_red_moment_hu_3": 2.00807713614223e-10,
        "intensity_red_median_intensity": 68.0,
        "intensity_red_mass_displace_in_minors": 0.039831665466914,
        "intensity_red_mean_intensity": 67.5858823529412,
        "intensity_red_perc_25_intensity": 34.0,
        "intensity_red_perc_75_intensity": 96.0,
        "intensity_green_mass_displace_in_images": 0.009051942893981,
        "intensity_green_moment_hu_4": 7.3328871508961e-12,
        "intensity_green_moment_hu_5": 1.61308614662726e-22,
        "intensity_green_moment_hu_6": 5.41478886935591e-15,
        "intensity_green_moment_hu_7": 1.46066546290528e-22,
        "intensity_green_std_intensity": 49.2534002268882,
        "intensity_green_moment_hu_1": 0.001597936986465,
        "intensity_green_moment_hu_2": 6.4019059128102e-07,
        "intensity_green_moment_hu_3": 1.20101695144045e-10,
        "intensity_green_median_intensity": 84.0,
        "intensity_green_mass_displace_in_minors": 0.020957246911431,
        "intensity_green_mean_intensity": 87.0611764705882,
        "intensity_green_perc_25_intensity": 37.0,
        "intensity_green_perc_75_intensity": 128.0,
        "intensity_blue_mass_displace_in_images": 0.003477996783235,
        "intensity_blue_moment_hu_4": 5.33414678545634e-12,
        "intensity_blue_moment_hu_5": 1.13689838407033e-22,
        "intensity_blue_moment_hu_6": 3.34282757211662e-15,
        "intensity_blue_moment_hu_7": -8.77804907314849e-24,
        "intensity_blue_std_intensity": 52.6562716093001,
        "intensity_blue_moment_hu_1": 0.001380066669561,
        "intensity_blue_moment_hu_2": 4.06557804086171e-07,
        "intensity_blue_moment_hu_3": 8.56701947118446e-11,
        "intensity_blue_median_intensity": 98.0,
        "intensity_blue_mass_displace_in_minors": 0.008827539385204,
        "intensity_blue_mean_intensity": 98.6188235294118,
        "intensity_blue_perc_25_intensity": 46.0,
        "intensity_blue_perc_75_intensity": 144.0,
        "empire": "prokaryota",
        "kingdom": "bacteria",
        "phylum": "cyanobacteria",
        "class": "cyanophyceae",
        "order": "nostocales",
        "family": "nostocaceae",
        "genus": "anabaena",
        "species": "sp",
        "with_eggs": None,
        "dividing": False,
        "dead": False,
        "with_epibiont": None,
        "with_parasite": None,
        "broken": False,
        "colony": False,
        "cluster": None,
        "eating": True,
        "multiple_species": False,
        "partially_cropped": False,
        "male": None,
        "female": None,
        "juvenile": None,
        "adult": None,
        "ephippium": None,
        "resting_egg": None,
        "heterocyst": None,
        "akinete": None,
        "with_spines": None,
        "beatles": None,
        "stones": None,
        "zeppelin": None,
        "floyd": None,
        "acdc": None,
        "hendrix": None,
        "alan_parsons": None,
        "allman": None,
        "dire_straits": None,
        "eagles": None,
        "guns": None,
        "purple": None,
        "van_halen": None,
        "skynyrd": None,
        "zz_top": None,
        "iron": None,
        "police": None,
        "moore": None,
        "inxs": None,
        "chilli_peppers": None,
        "acquisition_time": dateutil.parser.parse('2019-01-20 10:00:00'),
        "filename": 'image_000.jpeg',
        "image_width": 48,
        "image_height": 32,
        "extension": ".jpeg",
        "group_id": "processed"
    }),
    Item({
        "_id": ObjectId('000000000000000000000001'),
        "file_size": 1.0,
        "aspect_ratio": 1.0,
        "maj_axis_len": 1.0,
        "min_axis_len": 1.0,
        "orientation": 1.0,
        "eccentricity": 1.0,
        "solidity": 1.0,
        "estimated_volume": 1.0,
        "area": 1.0,
        "intensity_gray_mass_displace_in_images": 0.008681178096776,
        "intensity_gray_moment_hu_4": 6.44407178777693e-12,
        "intensity_gray_moment_hu_5": 1.58949394588895e-22,
        "intensity_gray_moment_hu_6": 4.87549139791229e-15,
        "intensity_gray_moment_hu_7": 9.29907144602865e-23,
        "intensity_gray_std_intensity": 44.4518848935367,
        "intensity_gray_moment_hu_1": 0.00162911271992,
        "intensity_gray_moment_hu_2": 6.02185718988395e-07,
        "intensity_gray_moment_hu_3": 1.26728600174152e-10,
        "intensity_gray_median_intensity": 87.0,
        "intensity_gray_mass_displace_in_minors": 0.021203842389859,
        "intensity_gray_mean_intensity": 84.08,
        "intensity_gray_perc_25_intensity": 39.0,
        "intensity_gray_perc_75_intensity": 124.0,
        "intensity_red_mass_displace_in_images": 0.016106449593647,
        "intensity_red_moment_hu_4": 6.23065353203622e-12,
        "intensity_red_moment_hu_5": 2.82161622605635e-23,
        "intensity_red_moment_hu_6": 4.08980777153774e-15,
        "intensity_red_moment_hu_7": 2.18575645069997e-22,
        "intensity_red_std_intensity": 33.6895555570746,
        "intensity_red_moment_hu_1": 0.002005703596185,
        "intensity_red_moment_hu_2": 8.66777471825988e-07,
        "intensity_red_moment_hu_3": 2.00807713614223e-10,
        "intensity_red_median_intensity": 68.0,
        "intensity_red_mass_displace_in_minors": 0.039831665466914,
        "intensity_red_mean_intensity": 67.5858823529412,
        "intensity_red_perc_25_intensity": 34.0,
        "intensity_red_perc_75_intensity": 96.0,
        "intensity_green_mass_displace_in_images": 0.009051942893981,
        "intensity_green_moment_hu_4": 7.3328871508961e-12,
        "intensity_green_moment_hu_5": 1.61308614662726e-22,
        "intensity_green_moment_hu_6": 5.41478886935591e-15,
        "intensity_green_moment_hu_7": 1.46066546290528e-22,
        "intensity_green_std_intensity": 49.2534002268882,
        "intensity_green_moment_hu_1": 0.001597936986465,
        "intensity_green_moment_hu_2": 6.4019059128102e-07,
        "intensity_green_moment_hu_3": 1.20101695144045e-10,
        "intensity_green_median_intensity": 84.0,
        "intensity_green_mass_displace_in_minors": 0.020957246911431,
        "intensity_green_mean_intensity": 87.0611764705882,
        "intensity_green_perc_25_intensity": 37.0,
        "intensity_green_perc_75_intensity": 128.0,
        "intensity_blue_mass_displace_in_images": 0.003477996783235,
        "intensity_blue_moment_hu_4": 5.33414678545634e-12,
        "intensity_blue_moment_hu_5": 1.13689838407033e-22,
        "intensity_blue_moment_hu_6": 3.34282757211662e-15,
        "intensity_blue_moment_hu_7": -8.77804907314849e-24,
        "intensity_blue_std_intensity": 52.6562716093001,
        "intensity_blue_moment_hu_1": 0.001380066669561,
        "intensity_blue_moment_hu_2": 4.06557804086171e-07,
        "intensity_blue_moment_hu_3": 8.56701947118446e-11,
        "intensity_blue_median_intensity": 98.0,
        "intensity_blue_mass_displace_in_minors": 0.008827539385204,
        "intensity_blue_mean_intensity": 98.6188235294118,
        "intensity_blue_perc_25_intensity": 46.0,
        "intensity_blue_perc_75_intensity": 144.0,
        "empire": "prokaryota",
        "kingdom": "bacteria",
        "phylum": "cyanobacteria",
        "class": "cyanophyceae",
        "order": "nostocales",
        "family": "nostocaceae",
        "genus": "anabaena",
        "species": None,
        "with_eggs": None,
        "dividing": False,
        "dead": False,
        "with_epibiont": None,
        "with_parasite": None,
        "broken": False,
        "colony": False,
        "cluster": None,
        "eating": True,
        "multiple_species": False,
        "partially_cropped": False,
        "male": None,
        "female": False,
        "juvenile": None,
        "adult": None,
        "ephippium": None,
        "resting_egg": None,
        "heterocyst": None,
        "akinete": None,
        "with_spines": None,
        "beatles": None,
        "stones": None,
        "zeppelin": None,
        "floyd": None,
        "acdc": None,
        "hendrix": None,
        "alan_parsons": None,
        "allman": None,
        "dire_straits": None,
        "eagles": None,
        "guns": None,
        "purple": None,
        "van_halen": None,
        "skynyrd": None,
        "zz_top": None,
        "iron": None,
        "police": None,
        "moore": None,
        "inxs": None,
        "chilli_peppers": None,
        "filename": "image_001.jpeg",
        "extension": ".jpeg",
        "group_id": "processed",
        "acquisition_time": dateutil.parser.parse('2019-01-20 06:00:00'),
        "image_width": 100,
        "image_height": 100
    }),
    Item({
        "_id": ObjectId('000000000000000000000002'),
        "file_size": 1.0,
        "aspect_ratio": 1.0,
        "maj_axis_len": 1.0,
        "min_axis_len": 1.0,
        "orientation": 1.0,
        "eccentricity": 1.0,
        "solidity": 1.0,
        "estimated_volume": 1.0,
        "area": 1.0,
        "intensity_gray_mass_displace_in_images": 0.008681178096776,
        "intensity_gray_moment_hu_4": 6.44407178777693e-12,
        "intensity_gray_moment_hu_5": 1.58949394588895e-22,
        "intensity_gray_moment_hu_6": 4.87549139791229e-15,
        "intensity_gray_moment_hu_7": 9.29907144602865e-23,
        "intensity_gray_std_intensity": 44.4518848935367,
        "intensity_gray_moment_hu_1": 0.00162911271992,
        "intensity_gray_moment_hu_2": 6.02185718988395e-07,
        "intensity_gray_moment_hu_3": 1.26728600174152e-10,
        "intensity_gray_median_intensity": 87.0,
        "intensity_gray_mass_displace_in_minors": 0.021203842389859,
        "intensity_gray_mean_intensity": 84.08,
        "intensity_gray_perc_25_intensity": 39.0,
        "intensity_gray_perc_75_intensity": 124.0,
        "intensity_red_mass_displace_in_images": 0.016106449593647,
        "intensity_red_moment_hu_4": 6.23065353203622e-12,
        "intensity_red_moment_hu_5": 2.82161622605635e-23,
        "intensity_red_moment_hu_6": 4.08980777153774e-15,
        "intensity_red_moment_hu_7": 2.18575645069997e-22,
        "intensity_red_std_intensity": 33.6895555570746,
        "intensity_red_moment_hu_1": 0.002005703596185,
        "intensity_red_moment_hu_2": 8.66777471825988e-07,
        "intensity_red_moment_hu_3": 2.00807713614223e-10,
        "intensity_red_median_intensity": 68.0,
        "intensity_red_mass_displace_in_minors": 0.039831665466914,
        "intensity_red_mean_intensity": 67.5858823529412,
        "intensity_red_perc_25_intensity": 34.0,
        "intensity_red_perc_75_intensity": 96.0,
        "intensity_green_mass_displace_in_images": 0.009051942893981,
        "intensity_green_moment_hu_4": 7.3328871508961e-12,
        "intensity_green_moment_hu_5": 1.61308614662726e-22,
        "intensity_green_moment_hu_6": 5.41478886935591e-15,
        "intensity_green_moment_hu_7": 1.46066546290528e-22,
        "intensity_green_std_intensity": 49.2534002268882,
        "intensity_green_moment_hu_1": 0.001597936986465,
        "intensity_green_moment_hu_2": 6.4019059128102e-07,
        "intensity_green_moment_hu_3": 1.20101695144045e-10,
        "intensity_green_median_intensity": 84.0,
        "intensity_green_mass_displace_in_minors": 0.020957246911431,
        "intensity_green_mean_intensity": 87.0611764705882,
        "intensity_green_perc_25_intensity": 37.0,
        "intensity_green_perc_75_intensity": 128.0,
        "intensity_blue_mass_displace_in_images": 0.003477996783235,
        "intensity_blue_moment_hu_4": 5.33414678545634e-12,
        "intensity_blue_moment_hu_5": 1.13689838407033e-22,
        "intensity_blue_moment_hu_6": 3.34282757211662e-15,
        "intensity_blue_moment_hu_7": -8.77804907314849e-24,
        "intensity_blue_std_intensity": 52.6562716093001,
        "intensity_blue_moment_hu_1": 0.001380066669561,
        "intensity_blue_moment_hu_2": 4.06557804086171e-07,
        "intensity_blue_moment_hu_3": 8.56701947118446e-11,
        "intensity_blue_median_intensity": 98.0,
        "intensity_blue_mass_displace_in_minors": 0.008827539385204,
        "intensity_blue_mean_intensity": 98.6188235294118,
        "intensity_blue_perc_25_intensity": 46.0,
        "intensity_blue_perc_75_intensity": 144.0,
        "empire": "prokaryota",
        "kingdom": "bacteria",
        "phylum": "cyanobacteria",
        "class": "cyanophyceae",
        "order": "nostocales",
        "family": "nostocaceae",
        "genus": "anabaena",
        "species": "sp",
        "with_eggs": None,
        "dividing": False,
        "dead": False,
        "with_epibiont": None,
        "with_parasite": None,
        "broken": False,
        "colony": False,
        "cluster": None,
        "eating": False,
        "multiple_species": False,
        "partially_cropped": False,
        "male": None,
        "female": True,
        "juvenile": None,
        "adult": None,
        "ephippium": None,
        "resting_egg": None,
        "heterocyst": None,
        "akinete": None,
        "with_spines": None,
        "beatles": None,
        "stones": None,
        "zeppelin": None,
        "floyd": None,
        "acdc": None,
        "hendrix": None,
        "alan_parsons": None,
        "allman": None,
        "dire_straits": None,
        "eagles": None,
        "guns": None,
        "purple": None,
        "van_halen": None,
        "skynyrd": None,
        "zz_top": None,
        "iron": None,
        "police": None,
        "moore": None,
        "inxs": None,
        "chilli_peppers": None,
        "filename": "image_002.jpeg",
        "extension": ".jpeg",
        "group_id": "processed",
        "acquisition_time": dateutil.parser.parse('2019-01-10 10:00:00'),
        "image_width": 100,
        "image_height": 100
    }),
    Item({
        "_id": ObjectId('000000000000000000000003'),
        "file_size": 1.0,
        "aspect_ratio": 1.0,
        "maj_axis_len": 1.0,
        "min_axis_len": 1.0,
        "orientation": 1.0,
        "eccentricity": 1.0,
        "solidity": 1.0,
        "estimated_volume": 1.0,
        "area": 1.0,
        "intensity_gray_mass_displace_in_images": 0.008681178096776,
        "intensity_gray_moment_hu_4": 6.44407178777693e-12,
        "intensity_gray_moment_hu_5": 1.58949394588895e-22,
        "intensity_gray_moment_hu_6": 4.87549139791229e-15,
        "intensity_gray_moment_hu_7": 9.29907144602865e-23,
        "intensity_gray_std_intensity": 44.4518848935367,
        "intensity_gray_moment_hu_1": 0.00162911271992,
        "intensity_gray_moment_hu_2": 6.02185718988395e-07,
        "intensity_gray_moment_hu_3": 1.26728600174152e-10,
        "intensity_gray_median_intensity": 87.0,
        "intensity_gray_mass_displace_in_minors": 0.021203842389859,
        "intensity_gray_mean_intensity": 84.08,
        "intensity_gray_perc_25_intensity": 39.0,
        "intensity_gray_perc_75_intensity": 124.0,
        "intensity_red_mass_displace_in_images": 0.016106449593647,
        "intensity_red_moment_hu_4": 6.23065353203622e-12,
        "intensity_red_moment_hu_5": 2.82161622605635e-23,
        "intensity_red_moment_hu_6": 4.08980777153774e-15,
        "intensity_red_moment_hu_7": 2.18575645069997e-22,
        "intensity_red_std_intensity": 33.6895555570746,
        "intensity_red_moment_hu_1": 0.002005703596185,
        "intensity_red_moment_hu_2": 8.66777471825988e-07,
        "intensity_red_moment_hu_3": 2.00807713614223e-10,
        "intensity_red_median_intensity": 68.0,
        "intensity_red_mass_displace_in_minors": 0.039831665466914,
        "intensity_red_mean_intensity": 67.5858823529412,
        "intensity_red_perc_25_intensity": 34.0,
        "intensity_red_perc_75_intensity": 96.0,
        "intensity_green_mass_displace_in_images": 0.009051942893981,
        "intensity_green_moment_hu_4": 7.3328871508961e-12,
        "intensity_green_moment_hu_5": 1.61308614662726e-22,
        "intensity_green_moment_hu_6": 5.41478886935591e-15,
        "intensity_green_moment_hu_7": 1.46066546290528e-22,
        "intensity_green_std_intensity": 49.2534002268882,
        "intensity_green_moment_hu_1": 0.001597936986465,
        "intensity_green_moment_hu_2": 6.4019059128102e-07,
        "intensity_green_moment_hu_3": 1.20101695144045e-10,
        "intensity_green_median_intensity": 84.0,
        "intensity_green_mass_displace_in_minors": 0.020957246911431,
        "intensity_green_mean_intensity": 87.0611764705882,
        "intensity_green_perc_25_intensity": 37.0,
        "intensity_green_perc_75_intensity": 128.0,
        "intensity_blue_mass_displace_in_images": 0.003477996783235,
        "intensity_blue_moment_hu_4": 5.33414678545634e-12,
        "intensity_blue_moment_hu_5": 1.13689838407033e-22,
        "intensity_blue_moment_hu_6": 3.34282757211662e-15,
        "intensity_blue_moment_hu_7": -8.77804907314849e-24,
        "intensity_blue_std_intensity": 52.6562716093001,
        "intensity_blue_moment_hu_1": 0.001380066669561,
        "intensity_blue_moment_hu_2": 4.06557804086171e-07,
        "intensity_blue_moment_hu_3": 8.56701947118446e-11,
        "intensity_blue_median_intensity": 98.0,
        "intensity_blue_mass_displace_in_minors": 0.008827539385204,
        "intensity_blue_mean_intensity": 98.6188235294118,
        "intensity_blue_perc_25_intensity": 46.0,
        "intensity_blue_perc_75_intensity": 144.0,
        "empire": "prokaryota",
        "kingdom": "bacteria",
        "phylum": "cyanobacteria",
        "class": "cyanophyceae",
        "order": "sphaeropleales",
        "family": "scenedesmaceae",
        "genus": "coelastrum",
        "species": None,
        "with_eggs": None,
        "dividing": False,
        "dead": False,
        "with_epibiont": None,
        "with_parasite": None,
        "broken": False,
        "colony": False,
        "cluster": None,
        "eating": None,
        "multiple_species": False,
        "partially_cropped": False,
        "male": None,
        "female": None,
        "juvenile": None,
        "adult": None,
        "ephippium": None,
        "resting_egg": None,
        "heterocyst": None,
        "akinete": None,
        "with_spines": None,
        "beatles": None,
        "stones": None,
        "zeppelin": None,
        "floyd": None,
        "acdc": None,
        "hendrix": None,
        "alan_parsons": None,
        "allman": None,
        "dire_straits": None,
        "eagles": None,
        "guns": None,
        "purple": None,
        "van_halen": None,
        "skynyrd": None,
        "zz_top": None,
        "iron": None,
        "police": None,
        "moore": None,
        "inxs": None,
        "chilli_peppers": None,
        "filename": "image_003.jpeg",
        "extension": ".jpeg",
        "group_id": "processed",
        "acquisition_time": dateutil.parser.parse('2019-01-05 10:00:00'),
        "image_width": 100,
        "image_height": 100
    }),
    Item({
        "_id": ObjectId('000000000000000000000004'),
        "file_size": 1.0,
        "aspect_ratio": 1.0,
        "maj_axis_len": 1.0,
        "min_axis_len": 1.0,
        "orientation": 1.0,
        "eccentricity": 1.0,
        "solidity": 1.0,
        "estimated_volume": 1.0,
        "area": 1.0,
        "intensity_gray_mass_displace_in_images": 0.008681178096776,
        "intensity_gray_moment_hu_4": 6.44407178777693e-12,
        "intensity_gray_moment_hu_5": 1.58949394588895e-22,
        "intensity_gray_moment_hu_6": 4.87549139791229e-15,
        "intensity_gray_moment_hu_7": 9.29907144602865e-23,
        "intensity_gray_std_intensity": 44.4518848935367,
        "intensity_gray_moment_hu_1": 0.00162911271992,
        "intensity_gray_moment_hu_2": 6.02185718988395e-07,
        "intensity_gray_moment_hu_3": 1.26728600174152e-10,
        "intensity_gray_median_intensity": 87.0,
        "intensity_gray_mass_displace_in_minors": 0.021203842389859,
        "intensity_gray_mean_intensity": 84.08,
        "intensity_gray_perc_25_intensity": 39.0,
        "intensity_gray_perc_75_intensity": 124.0,
        "intensity_red_mass_displace_in_images": 0.016106449593647,
        "intensity_red_moment_hu_4": 6.23065353203622e-12,
        "intensity_red_moment_hu_5": 2.82161622605635e-23,
        "intensity_red_moment_hu_6": 4.08980777153774e-15,
        "intensity_red_moment_hu_7": 2.18575645069997e-22,
        "intensity_red_std_intensity": 33.6895555570746,
        "intensity_red_moment_hu_1": 0.002005703596185,
        "intensity_red_moment_hu_2": 8.66777471825988e-07,
        "intensity_red_moment_hu_3": 2.00807713614223e-10,
        "intensity_red_median_intensity": 68.0,
        "intensity_red_mass_displace_in_minors": 0.039831665466914,
        "intensity_red_mean_intensity": 67.5858823529412,
        "intensity_red_perc_25_intensity": 34.0,
        "intensity_red_perc_75_intensity": 96.0,
        "intensity_green_mass_displace_in_images": 0.009051942893981,
        "intensity_green_moment_hu_4": 7.3328871508961e-12,
        "intensity_green_moment_hu_5": 1.61308614662726e-22,
        "intensity_green_moment_hu_6": 5.41478886935591e-15,
        "intensity_green_moment_hu_7": 1.46066546290528e-22,
        "intensity_green_std_intensity": 49.2534002268882,
        "intensity_green_moment_hu_1": 0.001597936986465,
        "intensity_green_moment_hu_2": 6.4019059128102e-07,
        "intensity_green_moment_hu_3": 1.20101695144045e-10,
        "intensity_green_median_intensity": 84.0,
        "intensity_green_mass_displace_in_minors": 0.020957246911431,
        "intensity_green_mean_intensity": 87.0611764705882,
        "intensity_green_perc_25_intensity": 37.0,
        "intensity_green_perc_75_intensity": 128.0,
        "intensity_blue_mass_displace_in_images": 0.003477996783235,
        "intensity_blue_moment_hu_4": 5.33414678545634e-12,
        "intensity_blue_moment_hu_5": 1.13689838407033e-22,
        "intensity_blue_moment_hu_6": 3.34282757211662e-15,
        "intensity_blue_moment_hu_7": -8.77804907314849e-24,
        "intensity_blue_std_intensity": 52.6562716093001,
        "intensity_blue_moment_hu_1": 0.001380066669561,
        "intensity_blue_moment_hu_2": 4.06557804086171e-07,
        "intensity_blue_moment_hu_3": 8.56701947118446e-11,
        "intensity_blue_median_intensity": 98.0,
        "intensity_blue_mass_displace_in_minors": 0.008827539385204,
        "intensity_blue_mean_intensity": 98.6188235294118,
        "intensity_blue_perc_25_intensity": 46.0,
        "intensity_blue_perc_75_intensity": 144.0,
        "empire": "prokaryota",
        "kingdom": "bacteria",
        "phylum": "cyanobacteria",
        "class": "cyanophyceae",
        "order": "sphaeropleales",
        "family": "scenedesmaceae",
        "genus": "coelastrum",
        "species": "reticulatum",
        "with_eggs": None,
        "dividing": False,
        "dead": False,
        "with_epibiont": None,
        "with_parasite": None,
        "broken": False,
        "colony": False,
        "cluster": None,
        "eating": None,
        "multiple_species": False,
        "partially_cropped": False,
        "male": None,
        "female": None,
        "juvenile": None,
        "adult": None,
        "ephippium": None,
        "resting_egg": None,
        "heterocyst": None,
        "akinete": None,
        "with_spines": None,
        "beatles": None,
        "stones": None,
        "zeppelin": None,
        "floyd": None,
        "acdc": None,
        "hendrix": None,
        "alan_parsons": None,
        "allman": None,
        "dire_straits": None,
        "eagles": None,
        "guns": None,
        "purple": None,
        "van_halen": None,
        "skynyrd": None,
        "zz_top": None,
        "iron": None,
        "police": None,
        "moore": None,
        "inxs": None,
        "chilli_peppers": None,
        "filename": "image_004.jpeg",
        "extension": ".jpeg",
        "group_id": "processed",
        "acquisition_time": dateutil.parser.parse('2019-01-01 10:00:00'),
        "image_width": 100,
        "image_height": 100
    })
]
