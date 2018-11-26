import json
import sys
import os


def create_dict_from_json(file_name):
    with open(file_name, 'r') as json_list_file:
        parsed_input = json.load(json_list_file)
    return parsed_input


def create_bucket_ranges(buckets_list):
    buckets_list.sort()
    buckets_ranges = []
    print(buckets_list)
    for inx in range(len(buckets_list)-1):
        buckets_ranges.append(str(buckets_list[inx]) + '-' + str(buckets_list[inx + 1]))
    return buckets_ranges

def sort_data_to_buckets(data, buckets_list):
    result_dict = {}
    for bucket in buckets_list:
        result_dict[bucket] = []

    for key in data:
        for bucket in buckets_list:
            min, _, max = bucket.partition('-')
            if int(min) <= data[key] < int(max):
                result_dict[bucket].append(key)

    return result_dict

def write_output_file(file_name, data):
    new_file_name = file_name + '.yaml'
    with open(new_file_name, 'w') as new_file:
        new_file.write("----\n")
        for key in data:
            new_file.write(key + "\n")
            for i in data[key]:
                new_file.write("- :" + i + "\n")



def main():
    print("Start")
    json_file = sys.argv[1]
    parsed_dict = create_dict_from_json(json_file)

    ppl_ages = parsed_dict['ppl_ages']
    buckets = parsed_dict['buckets']

    bucket_ranges = create_bucket_ranges(buckets)
    result = sort_data_to_buckets(ppl_ages, bucket_ranges)
    print(result)
    write_output_file("new", result)


if __name__=='__main__':
    main()