from test.map_view_test import test_maps
from test.drivers_test import test_drivers
from test.vehicles_test import test_vehicles
from test.report_trips_test import test_gen_report_trips
import sys, json
def read_configuration():
    if(len(sys.argv) > 1):
        config_argv1 = sys.argv[1]
        print("argv 1 = " + config_argv1)
        json_file_path = "env_config.json"
        with open(json_file_path, "r") as file:
            env_data = json.load(file)
        config = env_data[config_argv1]
        return config

try:
    config = read_configuration()
    # test_maps(config)
    # test_drivers(config)
    # test_vehicles(config)
    test_gen_report_trips(config)
except Exception as e:
    print("\nAn error occured: ",e)