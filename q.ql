[out:json][timeout:120];
(area["name"="Nashville-Davidson"]["admin_level"="8"];area["name"="Denver"]["admin_level"="8"];area["name"="Austin"]["admin_level"="8"]["is_in:state"!~"x"];area["name"="Charlotte"]["admin_level"="8"];area["name"="Minneapolis"]["admin_level"="8"];area["name"="Portland"]["admin_level"="8"];area["name"="Columbus"]["admin_level"="8"];area["name"="Kansas City"]["admin_level"="8"];area["name"="Raleigh"]["admin_level"="8"];area["name"="Phoenix"]["admin_level"="8"];area["name"="Scottsdale"]["admin_level"="8"];)->.a;
(nwr(area.a)["shop"~"^(boutique|clothes|gift|florist|hairdresser|beauty|cosmetics|jewelry)$"]["email"];
 nwr(area.a)["shop"~"^(boutique|clothes|gift|florist|hairdresser|beauty|cosmetics|jewelry)$"]["contact:email"];
 nwr(area.a)["amenity"="cafe"]["email"];nwr(area.a)["amenity"="cafe"]["contact:email"];
 nwr(area.a)["leisure"="fitness_centre"]["email"];nwr(area.a)["leisure"="fitness_centre"]["contact:email"];);
out tags;
