

def query_station(country: str):
    """ query for extracting stations from country x
    Args:
        country (str): x country name in English as an argument for the query

    Returns:
        str : query for overpass
    """
    station_query = f"""
        // set output to json file
        [out:json];
        // set search area to x country in English
        ( area[int_name="{country}"]; )->.searchArea;
        // perform union with parenthesis
        (
        // AND statement by [key1=value1](and)[key2=value2]
        node["railway"="stop"]["subway"!="yes"]["station"!="subway"]["station"!="light_rail"]["light_rail"!="yes"](area.searchArea);
        node["railway"="station"]["subway"!="yes"]["station"!="subway"]["station"!="light_rail"]["light_rail"!="yes"](area.searchArea);
        node["public_transport"="stop_position"]["train"="yes"]["subway"!="yes"]["station"!="subway"]["station"!="light_rail"]["light_rail"!="yes"](area.searchArea);
        );
        (._;);
        out geom;
        """ 
    return station_query


def query_rail(country: str):
    """ query for extracting railways from country x
    Args:
        country (str): x country name in English as an argument for the query

    Returns:
        str : query for overpass
    """
    rail_query = f"""
        // set output to json file
        [out:json];
        // set search area to x country in English
        ( area[int_name="{country}"]; )->.searchArea;
        // perform union with parenthesis (unionpart1; unionpart2)
        (
        // AND statement by [key1=value1](and)[key2=value2]
        way["railway"="narrow_gauge"]["disused:railway"!="rail"]["service"!~"."]["usage"!="military"]["usage"!="industrial"]["usage"!="freight"]["usage"!="tourism"](area.searchArea);
        way["railway"="rail"]["disused:railway"!="rail"]["service"!~"."]["usage"!="military"]["usage"!="industrial"]["usage"!="freight"]["usage"!="tourism"](area.searchArea);
        );
        (._;);
        out geom;
        """
    return rail_query


def query_city(country: str):
    """ query for extracting cities from country x
    Args:
        country (str): x country name in English as an argument for the query

    Returns:
        str : query for overpass
    """
    city_query = f"""
        // set output to json file
        [out:json];
        // set search area to x country in English
        ( area[int_name="{country}"]; )->.searchArea;
        // perform union with parenthesis
        (
        // AND statement by [key1=value1](and)[key2=value2]
        node["place"="city"](area.searchArea);
        node["place"="town"](area.searchArea);
        );
        (._;);
        out geom;
        """
    return city_query
