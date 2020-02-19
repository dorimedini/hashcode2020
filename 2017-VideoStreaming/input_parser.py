def line_to_int_tuple(line):
    return (int(x) for x in line.strip().split(' '))


def line_to_int_list(line):
    return list(line_to_int_tuple(line))


def parse(filename):
    result = {
        # Basic parameters
        'V': None, 'E': None, 'R': None, 'C': None, 'X': None,
        # List of video sizes
        'video_size': [],
        # List of latencies (maps endpoint IDs to the datacenter latency)
        'endpoint_ds_lat': [],
        # Maps endpoint IDs to map of latencies per cache (cache ID ==> latency)
        'endpoint_cache_lat': {},
        # Maps endpoint IDs to maps between video IDs to number of requests
        'endpoint_reqs': {},
        # Provides the inverse map - video IDs map to mappings from endpoint IDs to number of requests
        # for that video
        'video_reqs': {}
    }
    with open(filename, 'r') as file:
        # Basic parameters
        result['V'], result['E'], result['R'], result['C'], result['X'] = line_to_int_tuple(file.readline())
        # Video sizes
        result['video_size'] = line_to_int_list(file.readline())
        # Endpoint parameters
        for eID in range(result['E']):
            ds_lat, num_caches = line_to_int_tuple(file.readline())
            result['endpoint_ds_lat'].append(ds_lat)
            result['endpoint_cache_lat'][eID] = {}
            for _ in range(num_caches):
                cID, lat = line_to_int_tuple(file.readline())
                result['endpoint_cache_lat'][eID][cID] = lat
        # Requests
        for r in range(result['R']):
            vID, eID, num_reqs = line_to_int_tuple(file.readline())
            if eID not in result['endpoint_reqs']:
                result['endpoint_reqs'][eID] = {}
            result['endpoint_reqs'][eID][vID] = num_reqs
            if vID not in result['video_reqs']:
                result['video_reqs'][vID] = {}
            result['video_reqs'][vID][eID] = num_reqs
        return result
