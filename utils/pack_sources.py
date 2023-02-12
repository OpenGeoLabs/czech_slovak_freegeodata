import os
import configparser
import json

def get_url(config):
    if config['general']['type'].upper() == 'WMS':
        # TODO check CRS? Maybe.
        url = 'url=' + config['wms']['url']
        layers = config['wms']['layers'].split(',')
        for layer in layers:
            url += "&layers=" + layer
        styles = config['wms']['styles'].split(',')
        for style in styles:
            url += "&styles=" + style
        url += "&" + config['wms']['params']
        return url

    elif config['general']['type'].upper() == 'TMS':
        return "type=xyz&url=" + config['tms']['url']

    elif config['general']['type'].upper() == 'WMTS':
        url = config['wmts']['url']
        tilematrixset = config['wmts']['tilematrixset']
        layer = config['wmts']['layer']
        frmt = config['wmts']['format']
        crs = config['wmts']['crs']
        url = "contextualWMSLegend=0&featureCount=10&crs={crs}&format={frmt}&layers={layer}&styles=default&tileMatrixSet={tilematrixset}&url={url}".format(
            url=url, tilematrixset=tilematrixset, layer=layer,
            crs=crs, frmt=frmt)
        if 'SmoothPixmapTransform' in config['wmts'].keys():
            spt = config['wmts']['SmoothPixmapTransform']
            url = "SmoothPixmapTransform=" + str(spt) + "&" + url
        return url

def convert_sources_into_json(full=True):

    data_statuses = {}
    data_sources = []
    paths = []

    sources_dir = os.path.join(os.path.dirname(__file__), '..', 'data_sources')

    for name in os.listdir(sources_dir):
        if os.path.isdir(os.path.join(sources_dir, name)) and name[:2] != "__":
            paths.append(name)

    paths.sort()
    print(len(paths))

    for path in paths:
        # config neads to be initializen in loop, otherwise it may
        # retain values that are unititialized in current source,
        # but were initiarized in some of the previous
        config = configparser.ConfigParser()
        config_file = os.path.join(sources_dir, path, 'metadata.ini')

        try:
            config.read(config_file, 'UTF-8')
        except (UnicodeDecodeError, configparser.DuplicateOptionError) as e:
            print("Unable load {}: {}".format(config_file, e))
            continue

        url = ""
        proc_class = None
        service_name = None
        try:
            if "WMS" in config['general']['type'] or "TMS" in config['general']['type']:
                url = get_url(config)

                if config['general']['type'].upper() == 'WMS' and config.has_option("wms", "service_name"):
                    service_name = config["wms"]["service_name"]

            elif "WMTS" in config['general']['type']:
                url = get_url(config)

                if config.has_option("wmts", "service_name"):
                    service_name = config["wmts"]["service_name"]


        except KeyError as e:
            print("Invalid metadata {} (missing key {})".format(config_file, e))
            continue

        try:
            key_word = config['ui']['keywords'].split(',')
        except KeyError:
            key_word = []

        if full:
            data_sources.append(
                {
                    "logo": os.path.join(sources_dir, path, config['ui']['icon']),
                    "path": path,
                    "group": config['ui']['group'],
                    "type": config['general']['type'],
                    "alias": config['ui']['alias'],
                    "url": url,
                    "checked": config['ui']['checked'],
                    "proc_class": proc_class,
                    "service_name": service_name,
                    "keywords": key_word
                }
            )
        else:
            data_statuses[path] = "green"

    if full:
        with open("sources.json", "w") as out:
            out.write(json.dumps(data_sources))
            # print(json.dumps(data_sources))
    else:
        with open("statuses.json", "w") as out:
            out.write(json.dumps(data_statuses))

convert_sources_into_json(False)
